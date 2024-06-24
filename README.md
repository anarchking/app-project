# MQTT Android Application

<a name="readme-top"></a>

<br />

  <h3 align="center">CS50P Final Project</h3>

  <p align="center">
    This is Stephen Littman's CS50P Final Project.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

#### Video Demo:  [![Youtube][YouTube.com]][YouTube-url]



The Goal in mind for this project is an application that can:
* Subscribes to Mqtt Topics.
* Publish to Mqtt topics.

<!-- The future of this project -->
<!--* Read out loud Mqtt topic payload using TTS.-->
<!--* Animate photo to match TTS output.-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Files -->
## File Structure
Files in this project are as follows:
* main.py is the App code that runs everything.
* myapp.kv is the Kivy/KivyMD Style language file. Style attributes can be in .kv file or in main.py, Some styling is in main.py for dynamic values.
* project.py is a copy of main.py and its only use is to meet CS50P's Final Project Requirements (Buildozer requires the main app code to be named "main.py" and CS50P requires "project.py").
* test_project.py tests 3 functions in project.py "copy of main" with pytest.
* data.db is the database file.
* buildozer.spec is the Application compiler config file. This is where you can change the icon, name, permissions and all kinds of settings. 
* android.txt is needed by Buildozer for android.
* requirements.txt is all the required modules/libraries needed for this project.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
### Built With

These are the frameworks,libraries and softwares used to bring this project to life.


* [![Android][Android.com]][Android-url]
* [![Kivy][Kivy.com]][Kivy-url]
* [![KivyMD][KivyMD.com]][KivyMD-url]
* [![Paho_Mqtt][Paho_Mqtt.com]][Paho_Mqtt-url]
* [![SQLite][SQLite.com]][SQLite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
* To try it out 
  ```sh
  Download the apk file and install.
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ALL DEPENDENCIES -->
### Dependencies

This is a list of Dependencies needed to compile with buildozer.

* Kivy
  ```sh
  pip install Kivy==2.3.0
  ```
* KivyMD
  ```sh
  pip install kivymd==1.2.0
  ```
* Paho
  ```sh
  pip install paho_mqtt==2.1.0
  ```
* Plyer
  ```sh
  pip install plyer==2.1.0
  ```
* Kivy Examples
  ```sh
  pip install Kivy_examples==2.3.0
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* To connect to a local Mqtt server
  ```sh
  Make sure you are on the same Network as the Mqtt server or use a vpn tunnel to the network of the server.
  ```
* Once network connection is configured
  ```sh
  Click on the Configure Server Screen and enter appropriate information the the input fields and Click the Connect button.
  Next time you open the app, that server will be saved and you can reconnect to it by pressing the button at the top.
  ```
  * Subscribe or Publish
  ```sh
  Click on the Menu button at the top left and choose Listen or Publish 
  ```

<div align="center">
    <img src="assets/Listen.gif" width="300" height="600">
    <img src="assets/Publish.gif" width="300" height="600">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Get connection to server working
- [x] Get Subscribe Screen loading messages
- [x] Get Publish Screen publishing and displaying previously published commands. 
- [ ] Add MDLabel to Server Screen that prints success or failed message.
- [ ] Add run in background permisson request.
- [ ] Anchor MDLabel in MDScrollview to the top and left on both Listen and Publish Screen
- [ ] Create face outline overlay for Camera Screen
- [ ] Bugs
    - [on_pause()/on_resume() bug, long break from app loses connection to server, run in background?] 
    - [ ] 
    - [ ] 
    - [ ] 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [![Facebook][Facebook.com]](https://www.facebook.com/stephen.littman.9)

* [![Linkedin][Linkedin.com]](https://www.linkedin.com/in/stephen-littman-023a30258/)

* [![Github][Github.com]](https://github.com/anarchking)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This is a list of some useful tool and resources used in the study of this project.


* [GitHub](https://github.com)
* [Stackoverflow](https://stackoverflow.co/)
* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)
* [Kivy Tutorial Playlist from Codemy.com](https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg)
* [Kivy Course - Create Python Games and Mobile Apps from freecodecamp.org](https://www.youtube.com/watch?v=l8Imtec4ReQ&t=2166s)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


[Android.com]: https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white
[Android-url]: https://www.android.com/
[Kivy.com]: https://img.shields.io/badge/Kivy-gray?style=for-the-badge
[Kivy-url]: https://kivy.org/

[KivyMD.com]: https://img.shields.io/badge/KivyMD-9ca0a5?style=for-the-badge
[KivyMD-url]: https://kivymd.readthedocs.io/en/1.1.1/index.html

[Paho_Mqtt.com]: https://img.shields.io/badge/Paho_Mqtt-orange?style=for-the-badge
[Paho_Mqtt-url]: https://eclipse.dev/paho/index.php?page=clients/python/index.php

[SQLite.com]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://sqlite.org/

[YouTube.com]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[YouTube-url]: https://youtu.be/I2C0B-_EbtU

[Facebook.com]: https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white
[Linkedin.com]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Github.com]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white