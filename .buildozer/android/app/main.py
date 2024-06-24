#__version__ = “2.3.0”
from kivy.lang import Builder
from kivy.utils import platform
from kivy.properties import BooleanProperty, ListProperty
from kivy.clock import Clock
from kivy.graphics import Canvas, PopMatrix, PushMatrix, Rotate
from kivy.uix.camera import Camera
from kivy.core.window import Window
from collections import deque
#from kivy.core.camera import CameraBase
#from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.widget import Widget
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer

from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label.label import MDLabel
from kivymd.uix.button.button import MDFloatingActionButton, MDTextButton, MDRectangleFlatButton


from plyer import storagepath, filechooser, camera

import paho.mqtt.client as mqtt
import sqlite3
import re
import datetime

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# current servers database id
current_id = ""
# the server connected to
current_server = None
# a que for messages From Mqtt To App
q = deque()

# ask for android permissions
if platform == "android":
    from android.permissions import request_permissions, Permission, check_permission # pylint: disable=import-error # type: ignore
    PERMISSION = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA]
    request_permissions(PERMISSION)


# the Main Class of the app 
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

    def on_resume(self):
        pass

    def on_pause(self):
        return True

    # method for switching screens
    def go_to(self, screen, transition): 
        self.root.ids.screen_manager.transition.direction = transition   
        self.root.ids.screen_manager.current = screen
    
    # app call to subscribe method
    def sub(self):
        subscribe_to(self.root.ids.sub_mqtt_topic.text)


# file selection on choose face screen
class FileChoose(MDFloatingActionButton):
    '''
    Button that triggers 'filechooser.open_file()' and processes
    the data response from filechooser Activity.
    '''
    selection = ListProperty([])
    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        if platform == "android":
            if check_permission(Permission.CAMERA) == False:
                pass
        else:
            filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        MDApp.get_running_app().root.ids.result.text = str(self.selection)


# button at top of server screen that loads last config if one exists
class Last_Server(MDRectangleFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load()

    # loads the info to buton text
    def load(self):
        self.text = f"{load_last_server()}"
        self.theme_text_color = "Custom"
        self.text_color = "#00ff00"
        return self
    
    # when pressed connect with saved info
    def press(self):
        conn = sqlite3.connect("data.db")
        db = conn.cursor()
        server = db.execute("SELECT server_ip, server_port, mqtt_username, mqtt_password, server_id FROM servers ORDER BY server_id DESC LIMIT 1")
        server = server.fetchall()
        conn.commit()
        conn.close()
        if not server[0][2] or server[0][2] == None:
            # only server and port
            connect_server(server[0][0], server[0][1])
        else:
            # server, port, username, password
            connect_server(server[0][0], server[0][1], server[0][2], server[0][3])
        global current_id
        current_id = server[0][4]    


# label for desplaying connected server info
class Server_Status(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def load_status(self):
        if mqttc.is_connected():
            conn = sqlite3.connect("data.db")
            db = conn.cursor()
            server = db.execute("SELECT server_ip, server_port FROM servers ORDER BY server_id DESC LIMIT 1")
            server = server.fetchall()
            self.text = f"[b]Connected to {server[0][0]} on port {server[0][1]}[b]"
        else:
            self.text = "No Connection to a Server"


# Button in server screen for submitting new info 
class Server_Button(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):
        app = MDApp.get_running_app()
        server_address = app.root.ids.server_address.text
        port = app.root.ids.port.text
        username = app.root.ids.username.text
        password = app.root.ids.password.text
        autostart = app.root.ids.auto_start.active
        print(server_address)
        if server_to_db(server_address, port, username, password, autostart):
            if not username or username == None:
                connect_server(server_address, port)
            else:
                connect_server(server_address, port, username, password)
        else:
            print("Error Could not save to database.")



# Listen Screen
class Listen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self):
        app = MDApp.get_running_app()
        #print(self.ids.server_status)
        app.root.ids.server_status.load_status()


# Label for incoming Messages
class Received_Messages(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.add_message, 0.5)

    def add_message(self, instance):
        if q and q != None:
            self.text = f"{q.pop()}" + "\n" + "-------------------\n" + self.text
            

# Publish Screen
class Publish(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self):
        app = MDApp.get_running_app()
        #print(self.ids.server_status)
        if current_server and current_server != None:
            app.root.ids.server_status_pub.text = f"[b]Connected to {current_server} on port {current_port}[b]"
        else:
            app.root.ids.server_status_pub.text = "No Connection to a Server"


# Button on Publish screen for publishing to the entered topic
class Pub_Button(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):
        app = MDApp.get_running_app()
        topic = app.root.ids.pub_mqtt_topic.text
        payload = app.root.ids.pub_mqtt_payload.text
        on_publish(topic, payload)
        dt = datetime.datetime.now()
        app.root.ids.sent_messages.add_message(f"{topic} {payload}  {dt.strftime('%c')}")


# Label for Outgoing Messages
class Sent_Messages(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def add_message(self, new_pub):
        self.text = new_pub + "\n" + "-------------------\n" + self.text


# Camera Screen
class Camera_Check(MDScreen):
    cam_state = BooleanProperty(True)
    # Dont load camera til permission is checked
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDFloatLayout()
        self.load = MDLabel(
                text = "LOADING",
                text_color = "#ffffff",
                text_size = "100dp",
                halign = "center",
                pos_hint = {"center_x": .5, "center_y": .5},)
        
        return self.layout.add_widget(self.load)
    
    # check permission on entering
    def on_enter(self):
        self.clear_widgets()
        if platform == "android":
            if check_permission(Permission.CAMERA) == False:
                '''restart = MDLabel(
                    text = "Please restart app and grant Camera Permissions.",
                    text_color = "#ffffff",
                    text_size = "100dp",
                    halign = "center",
                    pos_hint = {"center_x": .5, "center_y": .5},)'''
                self.restart = MDFloatingActionButton(
                    icon = "camera-outline",
                    icon_color = "#ffffff",
                    halign = "center",
                    pos_hint = {"center_x": .1, "center_y": .7},
                    #md_bg_color = "Blue",
                    #icon_size = "100dp",
                )
                self.add_widget(self.restart)
                #layout = self.rotations(layout)
                return self
            
        # we have camera permissions
        self.cam = Camera(
            resolution = (1920, 1080),
            play = True,
            size_hint_y = 2.3,
            size_hint_x = 1.75,
            pos_hint = {"center_x": .5, "center_y": .5},
        )
        self.cam = self.rotations(self.cam)
        self.add_widget(self.cam)

        # back button
        self.arrow = MDFloatingActionButton(
            icon = "arrow-left",
            icon_color = "#ffffff",
            halign = "center",
            pos_hint = {"center_x": .92, "center_y": .90},
        )
        self.arrow = self.rotations(self.arrow)
        self.arrow.bind(on_release = self.go_back)
        self.add_widget(self.arrow)

        # button for taking picture
        self.click_icon = MDFloatingActionButton(
            icon = "camera-outline",
            icon_color = "#ffffff",
            halign = "center",
            pos_hint = {"center_x": .5, "center_y": .1},
        )
        self.click_icon = self.rotations(self.click_icon)
        self.click_icon.bind(on_release = self.click)
        self.add_widget(self.click_icon)
        return self

    # rotation for camera image and icons
    def rotations(self, wid):
        with wid.canvas.before:
            PushMatrix()
            rotate = Rotate(angle=-90)
        with wid.canvas.after:
            PopMatrix()
        def update_rotate(w, center):
            rotate.origin = center
        wid.bind(center=update_rotate)
        return wid
  

    #Function to capture the images and give them the names
    #according to their captured time and date.
    def click(self, instance):
        self.cam.play = not bool(self.cam.play)
        dt = datetime.datetime.now()
        time = dt.strftime("%Y%m%d_%H%M%S")
        self.cam.export_to_png("IMG_{}.png".format(time))
        return self
    
    # back button only for camera screen
    def go_back(self, instance):
        app = MDApp.get_running_app()
        app.root.ids.screen_manager.transition.direction = "down"
        app.root.ids.screen_manager.current = "face"

    #def capture(self):
        #print(self.root.ids)
        #camera = self.cam

        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        #camera.take_picture(filename=filepath, on_complete=self.camera_callback)
 
        #camera.export_to_png("IMG_{}.png".format(timestr))
        #self.go_to("up", "save_pic")      
         

# main loop
def main():
    MyApp().run()


# method for saving server creds to database
def server_to_db(server_ip, port, username=None, password=None, autostart=False):
    # make sure ip address numbers are 0-255
    if re.search(r"^(([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))\.){3}([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))$", server_ip):
        # port number between 0 and 65536
        if int(port) >= 1 and int(port) <= 65536:
            try:
                conn = sqlite3.connect("data.db")
                db = conn.cursor()
                value = [                    
                    server_ip,   
                    port,
                    username,
                    password,
                    autostart
                    ]
                db.execute("INSERT INTO servers(server_ip, server_port, mqtt_username, mqtt_password, auto_start) VALUES (?, ?, ?, ?, ?)", value)
                conn.commit()
                conn.close()
                return True
            except ValueError:
                print("ERROR in Database")
                return False
        else:
            print("Not a valid Port Number")
            return False
    else:
        print("Not a valid IP Address") 
    return False

    # true if all was good
    # and false if not a valid ip     


# loads last server from database and returns a string
def load_last_server():
    conn = sqlite3.connect("data.db")
    db = conn.cursor()
    server = db.execute("SELECT server_id, server_ip, server_port FROM servers ORDER BY server_id DESC LIMIT 1")
    server = server.fetchall()
    conn.commit()
    conn.close()
    if not server or server == None:
        return "No saved Servers"
    return f"Connect to Server {server[0][1]} on Port {server[0][2]}?"


# method for subscribing to Mqtt 
def subscribe_to(topic):
    if mqttc.is_connected():
        mqttc.subscribe(topic)
        #mqttc.reconnect() 


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and


# on disconnection from mqtt server
def on_disconnect(client, userdata,rc=0):
    client.loop_stop()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    dt = datetime.datetime.now()
    q.append(f"{msg.topic} {str(msg.payload)}  {dt.strftime('%c')} ")
    conn = sqlite3.connect("data.db")
    db = conn.cursor()
    db.execute(
        "INSERT INTO sub_messages (server_id, message) VALUES(?, ?)",
        (current_id, msg.topic + " " + str(msg.payload) + dt.strftime('%c'))
    )
    conn.commit()
    conn.close()

# method for publishing Mqtt
def on_publish(topic, payload):
    dt = datetime.datetime.now()
    mqttc.publish(topic, payload)
    conn = sqlite3.connect("data.db")
    db = conn.cursor()
    db.execute(
        "INSERT INTO post_messages (server_id, message) VALUES(?, ?)",
        (current_id, topic + " " + payload + dt.strftime('%c')))
    conn.commit()
    conn.close()
        

# method for connecting to the server
def connect_server(server, port, username=None, password=None):
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_disconnect = on_disconnect
    if username != None:
        mqttc.username_pw_set(username=username, password=password)
    try:
        mqttc.connect(server, int(port))
    except:
        pass
    mqttc.loop_start()
    global current_server
    global current_port
    current_server = server
    current_port = port


if __name__ == "__main__":
    main()

    