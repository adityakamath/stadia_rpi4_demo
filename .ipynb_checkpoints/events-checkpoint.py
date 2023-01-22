#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
stadia = InputDevice('/dev/input/event0')

#prints out device info at start
print(stadia)
#print(stadia.capabilities(verbose=True))

#evdev takes care of polling the controller in a loop
for event in stadia.read_loop():
    print(categorize(event))
