from evdev import InputDevice, categorize, ecodes

stadia = InputDevice('/dev/input/event0')

axis_ljoy_x = ecodes.ABS_X
axis_ljoy_y = ecodes.ABS_Y
axis_rjoy_x = ecodes.ABS_Z
axis_rjoy_y = ecodes.ABS_RZ

axis_l2 = ecodes.ABS_BRAKE
axis_r2 = ecodes.ABS_GAS

axis_dpad_x = ecodes.ABS_HAT0X
axis_dpad_y = ecodes.ABS_HAT0Y

axes = [axis_ljoy_x,
        axis_ljoy_y,
        axis_rjoy_x,
        axis_rjoy_y,
        axis_l2,
        axis_r2,
        axis_dpad_x,
        axis_dpad_y]

prev_values = [128,
               128,
               128,
               128,
               0,
               0,
               0,
               0]

print(stadia)
#print(stadia.capabilities(verbose=True))

#loop and filter by event code and print the mapped label
for event in stadia.read_loop():
    for i in range(8):
        current_value = stadia.absinfo(axes[i]).value
        if(current_value != prev_values[i]):
            if i == 0:
                print("LJoy X Axis: ", current_value)
            elif i == 1:
                print("LJoy Y Axis: ", current_value)
            elif i == 2:
                print("RJoy X Axis: ", current_value)
            elif i == 3:
                print("RJoy Y Axis: ", current_value)
            elif i == 4:
                print("L2: ", current_value)
            elif i == 5:
                print("R2: ", current_value)
            elif i == 6:
                print("DPad X Axis: ", current_value)
            elif i == 7:
                print("DPad Y Axis: ", current_value)
        prev_values[i] = current_value
            
