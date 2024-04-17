#__version__ = “2.3.0”
from kivy.lang import Builder

from kivy.properties import BooleanProperty
from kivy.graphics import Canvas, PopMatrix, PushMatrix, Rotate
from kivy.uix.camera import Camera
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

from kivy import platform
from plyer import storagepath, filechooser, camera
#from camera4kivy import Prewiew

#import paho.mqtt.client as mqtt
#import sqlite3
#import re
from os import listdir
from os.path import join


if platform == "android":
    from android.permissions import request_permissions, Permission, check_permission # pylint: disable=import-error # type: ignore
    request_permissions(Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA)

    
class Camera_Check(MDScreen):
    cam_state = BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDFloatLayout()
        load = MDLabel(
                text = "LOADING",
                text_color = "#ffffff",
                text_size = "100dp",
                halign = "center",
                pos_hint = {"center_x": .5, "center_y": .5},)
        
        return layout.add_widget(load)
    

    def on_enter(self):
        self.clear_widgets()
        if platform == "android":
            if check_permission(Permission.CAMERA) == True:
                cam = Camera(
                    resolution = (1920, 1080),
                    play = self.cam_state,
                    size_hint_y = 2.3,
                    size_hint_x = 1.75,
                    pos_hint = {"center_x": .5, "center_y": .5},
                )
                
                cam = self.rotations(cam)
                self.add_widget(cam)
                #cam.id = "cam"
                #layout = self.rotations(layout)
                #self.add_widget(layout)

                arrow = MDFloatingActionButton(
                    icon = "arrow-left",
                    icon_color = "#ffffff",
                    halign = "center",
                    pos_hint = {"center_x": .92, "center_y": .90},
                )
                arrow = self.rotations(arrow)
                self.add_widget(arrow)

                icon = MDFloatingActionButton(
                    icon = "camera-outline",
                    icon_color = "#ffffff",
                    halign = "center",
                    pos_hint = {"center_x": .5, "center_y": .1},
                    on_release = self.click(),
                )
                icon = self.rotations(icon)
                #icon.bind(on_release = self.click())
                self.add_widget(icon)
                '''button = MDFloatingActionButton(
                    on_release = app.go_to("face", "down"),'''
            else:
                
                '''restart = MDLabel(
                    text = "Please restart app and grant Camera Permissions.",
                    text_color = "#ffffff",
                    text_size = "100dp",
                    halign = "center",
                    pos_hint = {"center_x": .5, "center_y": .5},)'''
                restart = MDFloatingActionButton(
                    icon = "camera-outline",
                    icon_color = "#ffffff",
                    halign = "center",
                    pos_hint = {"center_x": .1, "center_y": .7},
                    #md_bg_color = "Blue",
                    #icon_size = "100dp",
                    #on_release = MyApp.go_to("face", "down"),
                )
                self.add_widget(restart)
                #layout = self.rotations(layout)
            return self
        
        else:
            cam = Camera(
                resolution = (1920, 1080),
                play = self.cam_state,
                size_hint_y = 2.3,
                size_hint_x = 1.75,
                pos_hint = {"center_x": .5, "center_y": .5},
            )
            return self.add_widget(cam)

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
    

        def click(self):
            self.cam_state = not self.cam_state
            return 
            


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("screens.kv")


    def on_resume(self):
        pass


    def on_pause(self):
        return True


    # function for switching screens
    def go_to(self, screen, transition): 
        self.root.ids.screen_manager.transition.direction = transition   
        self.root.ids.screen_manager.current = screen
   

    #def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        #camera = self.root.ids['camera']
        #time = datetime.datetime.now()
        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        #camera.take_picture(filename=filepath, on_complete=self.camera_callback)
 
        #camera.export_to_png("IMG_{}.png".format(timestr))
        #self.go_to("up", "save_pic")      
         


def main():
    MyApp().run()
    # if server in sql then 
    #mqttc = connect_server()


'''def save_server(server_ip, port, username=None, password=None):
    # get code from cs50 regit project
    if re.search(r"^(([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))\.){3}([0-9]|[1-9][0-9]|(1)[0-9][0-9]|(2)([0-5][0-5]|[0-4][0-9]))$", server_ip):
        if port >= 0 and port <= 65536:
            db = sqlite3.connect("data.db")
            db.execute("INSERT INTO server VALUES (?, ?, ?, ?)", server_ip, port, username, password)
        else:
            return "Not a valid Port Number"
    
    # true if all was good
    # and false if not a valid ip     
    # port number between 0 and 65536
    else:
        return "Not a valid IP Address"


def load_server():
    # get code from cs50 regit project
    db = sqlite3.connect("data.db")
    servers = db.execute("SELECT server_ip, server_port FROM servers ORDER BY server_id DESC LIMIT 10")   
    pass
    # return server    


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
'''


if __name__ == "__main__":
    main()

    