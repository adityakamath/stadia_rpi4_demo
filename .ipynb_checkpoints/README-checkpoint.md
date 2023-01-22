# Stadia RPi4 Demo

Simple scripts to print events and input values from a Google Stadia controller, connected via Bluetooth to a Raspberry Pi 4 (8GB) running Ubuntu 22.04.

* ```events.py``` : Prints event data, shows the event codes which will be used in the other two scripts.
* ```stadia_buttons.py```: Prints information from button type inputs - A, B, X, Y, Options, Menu, Assistant, Capture, Stadia button, L1/R1, and left/right joystick buttons.
* ```stadia_axes.py```: Prints information from axes type inputs - left/right joysticks, L2/R2 triggers, and D-pad


## Pre-requisites / References

* Stadia controller must be switched to Bluetooth mode. Follow the instructions [here](https://stadia.google.com/controller/).
* Connect the controller to the Raspberry Pi using Bluetooth. There are many tutorials available, I followed the instructions from [here](https://salamwaddah.com/blog/connecting-ps4-controller-to-raspberry-pi-via-bluetooth). The link says PS4, but it also works with the Stadia Controller. The light around the Stadia logo should be solid white indicating a successful connection.
* Follow the instructions from this [amazing tutorial](https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python/), or watch their [YouTube video](https://www.youtube.com/watch?v=F5-dV6ULeg8). It is an old article/video and uses Python 2.7, but using Python 3 works just fine.

