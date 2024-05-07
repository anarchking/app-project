#__version__ = “2.3.0”
from kivy.lang import Builder
from kivy.utils import platform
from kivy.properties import BooleanProperty, ListProperty
from kivy.graphics import Canvas, PopMatrix, PushMatrix, Rotate
from kivy.uix.camera import Camera
from kivy.core.window import Window
#from kivy.core.camera import CameraBase
#from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.widget import Widget
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label.label import MDLabel
from kivymd.uix.button.button import MDFloatingActionButton

import inspect

from plyer import storagepath, filechooser, camera
#from camera4kivy import Prewiew

import paho.mqtt.client as mqtt
import sqlite3
import re
import time
from os import listdir
from os.path import join



if platform == "android":
    from android.permissions import request_permissions, Permission, check_permission # pylint: disable=import-error # type: ignore
    PERMISSION = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA]
    request_permissions(PERMISSION)


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        window = Window.size

    def on_resume(self):
        pass

    def on_pause(self):
        return True

    # function for switching screens
    def go_to(self, screen, transition): 
        self.root.ids.screen_manager.transition.direction = transition   
        self.root.ids.screen_manager.current = screen
   

    #Function to capture the images and give them the names
    #according to their captured time and date.


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


class Received_msg(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Server_Button(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):
        app = MDApp.get_running_app()
        server_address = app.root.ids.server_address.text
        port = app.root.ids.port.text
        username = app.root.ids.username.text
        password = app.root.ids.password.text
        print(server_address, port, username, password)
        if server_to_db(server_address, port, username, password):
            if server_address == None:
                pass
                #connect_server(ip, port)
            else:
                pass
                #connect_server(ip, port, username, password)
        else:
            print("Error Could not save to database.")
# load page with inputs converted to labels and a label that says connected with a check mark icon

    
class Camera_Check(MDScreen):
    cam_state = BooleanProperty(True)
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
            

        self.cam = Camera(
            resolution = (1920, 1080),
            play = True,
            size_hint_y = 2.3,
            size_hint_x = 1.75,
            pos_hint = {"center_x": .5, "center_y": .5},
        )
        self.cam = self.rotations(self.cam)
        self.add_widget(self.cam)

        self.arrow = MDFloatingActionButton(
            icon = "arrow-left",
            icon_color = "#ffffff",
            halign = "center",
            pos_hint = {"center_x": .92, "center_y": .90},
        )
        self.arrow = self.rotations(self.arrow)
        self.arrow.bind(on_release = self.go_back)
        self.add_widget(self.arrow)

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
  

    def click(self, instance):
        self.cam.play = not bool(self.cam.play)
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.cam.export_to_png("IMG_{}.png".format(timestr))
        return self
        
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
         


def main():
    MyApp().run()


def server_to_db(server_ip, port, username, password):
    # make sure ip address numbers are 0-255
    if re.search(r"^(([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))\.){3}([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))$", server_ip):
        # port number between 0 and 65536
        if int(port) >= 0 and int(port) <= 65536:
            try:
                conn = sqlite3.connect("data.db")
                db = conn.cursor()
                value = [                    
                    server_ip,   
                    port,
                    username,
                    password
                    ]
                db.execute("INSERT INTO servers(server_ip, server_port, mqtt_username, mqtt_password) VALUES (?, ?, ?, ?)", value)
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
    


'''
def load_server():
    # get code from cs50 regit project
    db = sqlite3.connect("data.db")
    servers = db.execute("SELECT server_ip, server_port FROM servers ORDER BY server_id DESC LIMIT 10")   
    pass
    # return server    
'''

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))             
        

def connect_server(server, port):
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    try:
        mqttc.connect(f"{server}", f"{port}")
    except:
        #return snackbar
        pass
    mqttc.loop_forever()
    #return mqttc



if __name__ == "__main__":
    main()

    