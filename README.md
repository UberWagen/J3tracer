# J3tracer
I wanted to un-hitch the waveshare jetracer from the JetRacer image to be able to have some more functionality outside of the jupyter notebook.

<p align="center">
  <img width="600" height="400" src="https://i.imgur.com/qtZstYu.jpg">
</p>


To get started, first things first: 

$ sudo apt-get update. 

You'll also want to install the following packages, if you haven't already.
$ sudo apt install python-pip
$ sudo apt install python3-pip
$ sudo apt install git 
 
Clone this git with 
$ git clone https://github.com/UberWagen/J3tracer


If you end up having issues with camera feeds or image processing, it's possible that your Linux config didn't come with a few packages. Run the following if you run into issues with image processing:
$ sudo apt-get install libcanberra-gtk-module
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev
tcl8.6-dev tk8.6-dev python-tk


The input being used is the ps3 style controller that is included with the waveshare jetracer. Outside of these, the JetPack distro from Nvidia should come with everything you need. If you have issues, don't be afraid to open an issue. I did have some luck using a bluetooth Xbox One S controller as well. Your mileage may vary.
