from evdev import InputDevice, categorize, ecodes

stadia = InputDevice('/dev/input/event0')

btn_a = 304
btn_b = 305
btn_x = 307
btn_y = 308

btn_options = 314
btn_menu    = 315
btn_assist  = 704
btn_capture = 705
btn_stadia  = 316

btn_l1 = 310
btn_r1 = 311
btn_ljoy = 317
btn_rjoy = 318

print(stadia)
#print(stadia.capabilities(verbose=True))

#loop and filter by event code and print the mapped label
for event in stadia.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == btn_a:
                print("A")
            elif event.code == btn_b:
                print("B")
            elif event.code == btn_x:
                print("X")
            elif event.code == btn_y:
                print("Y")
                
            elif event.code == btn_options:
                print("Options")
            elif event.code == btn_menu:
                print("Menu")
            elif event.code == btn_assist:
                print("Assistant")
            elif event.code == btn_capture:
                print("Capture")
            elif event.code == btn_stadia:
                print("Stadia")

            elif event.code == btn_l1:
                print("L1")
            elif event.code == btn_r1:
                print("R1")
                
            elif event.code == btn_ljoy:
                print("LJoy Button L3")
            elif event.code == btn_rjoy:
                print("RJoy Button R3")
                
            
