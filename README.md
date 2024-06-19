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

#### Video Demo:  [![Project walk thru video][YouTube.com]][YouTube-url]


[![Listen (Subscribe) Screen][product-screenshot1]](https://youtu.be/I2C0B-_EbtU)



The Goal in mind for this project is an application that can:
* Subscribes to Mqtt Topics.
* Publish to Mqtt topics.
* Read out loud Mqtt topic payload using TTS.
* Animate photo to match TTS output.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- BUILT WITH -->
### Built With

These are the frameworks,libraries and softwares used to bring this project to life.


* [![Android][Android.com]][Android-url]
* [![Kivy][Kivy.com]][Kivy-url]
* [![KivyMD][KivyMD.com]][KivyMD-url]
* [![SQLite][SQLite.com]][SQLite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
* To connect to a local Mqtt server
  ```sh
  Download the apk file and install.
  ```

* To connect to a local Mqtt server
  ```sh
  Make sure you are on the same Network as the Mqtt server or use a vpn tunnel to the network of the server.
  ```




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ALL DEPENDENCIES -->
### Dependencies

This is a list of Dependencies needed to run the Server.

* Kivy
  ```sh
  pip install kivy
  ```
* KivyMD
  ```sh
  pip install kivymd
  ```
* Plyer
  ```sh
  pip install plyer
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

If first use navigate to the Configure Server Screen and enter Mqtt server ip, port, username and password into appropriate fields.
Next, navigate to listen or publish screen and Subscribe or Publish respectfully.
Thats it, all set to troubleshoot Mqtt.


[![Publish Screen][product-screenshot2]](https://youtu.be/I2C0B-_EbtU)
.

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
    - [ ] 
    - [ ] 
    - [ ] 
    - [ ] 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Stephen Littman - [My Facebook](https://www.facebook.com/stephen.littman.9)

Project Link - [CS50P-Final-project](https://github.com/anarchking/project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This is a list of some useful tool and resources used in the study of this project.


* [GitHub](https://github.com)
* [Stackoverflow](https://stackoverflow.co/)
* [Choose an Open Source License](https://choosealicense.com)
* [Kivy Tutorial Playlist from Codemy.com](https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg)
* [Img Shields](https://shields.io)
* [Kivy Course - Create Python Games and Mobile Apps from freecodecamp.org](https://www.youtube.com/watch?v=l8Imtec4ReQ&t=2166s)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



[product-screenshot1]: Screenshots/Screenshot(1).png
[product-screenshot2]: Screenshots/Screenshot(2).png
[Android.com]: https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white
[Android-url]: https://www.android.com/
[Kivy.com]: https://kivy.org/doc/stable/_static/logo-kivy.png
[Kivy-url]: https://kivy.org/
[KivyMD.com]: https://avatars.githubusercontent.com/u/12729247?s=200&v=4
[KivyMD-url]: https://kivymd.readthedocs.io/en/1.1.1/index.html
[SQLite.com]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://sqlite.org/

[YouTube.com]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[YouTube-url]: https://youtu.be/I2C0B-_EbtU


