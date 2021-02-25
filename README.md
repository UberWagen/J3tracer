# J3tracer
I wanted to un-hitch the waveshare jetracer from the JetRacer image to be able to have some more functionality outside of the jupyter notebook.

<p align="center">
  <img width="600" height="400" src="https://i.imgur.com/qtZstYu.jpg">
</p>

Follow JetsonHacks' tutorial to get OSS installed https://www.jetsonhacks.com/2019/10/01/jetson-nano-visual-studio-code-python/


To get started, first things first, $ sudo apt-get update. You'll also want to install the following packages.  


$ sudo apt install python-pip

$ sudo apt install python3-pip

$ sudo pip3 install adafruit-blinka  
$ sudo pip3 install adafruit-circuitpython-servokit  
$ sudo pip3 install adafruit-circuitpython-busdevice  
$ sudo pip3 install adafruit-circuitpython-register  
$ sudo pip3 install adafruit-circuitpython-pca9685  
$ sudo pip3 install adafruit-circuitpython-motor  
$ sudo pip3 install adafruit-circuitpython-motorkit  
$ sudo pip3 install inputs  
$ sudo pip3 install numpy  
$ sudo apt-get install libcanberra-gtk-module

$ pip3 install nanocamera

$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev
libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev
tcl8.6-dev tk8.6-dev python-tk

$ pip3 install Pillow

$ sudo apt-get install python3-matplotlib

follow Jetson Hacks tutorial to get the PiOLED package installed https://www.jetsonhacks.com/2019/12/03/adafruit-pioled-on-jetson-nano/

The input being used is the ps3 style controller that is included with the waveshare jetracer. Outside of these, the JetPack distro from Nvidia should come with everything you need. If you have issues, don't be afraid to open an issue.
