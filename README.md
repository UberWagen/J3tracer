# J3tracer
I wanted to un-hitch the waveshare jetracer from the JetRacer image to be able to have some more functionality outside of the jupyter notebook.

Follow JetsonHacks' tutorial to get OSS installed https://www.jetsonhacks.com/2019/10/01/jetson-nano-visual-studio-code-python/

To get started, first things first, $ sudo apt-get update. You'll also want to install the following packages.  

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
$ python3 -m pip install Pillow

The input being used is the ps3 style controller that is included with the waveshare jetracer. Outside of these, the JetPack distro from Nvidia should come with everything you need. If you have issues, don't be afraid to open an issue.
