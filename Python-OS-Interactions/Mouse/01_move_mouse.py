"""
Source: https://www.thepythoncode.com/article/control-mouse-python
"""

import mouse
from time import sleep

middle_button_clicked = False
double_click = False

def middle_button_clicked_listener(*args):
    global middle_button_clicked
    print("Middle button clicked.")
    pos = mouse.get_position()
    print(f"Mouse position: x ({pos[0]}), y ({pos[1]})")

def double_clicked_listener(*args):
    global double_click
    print("Double clicked.")    
    double_click = True
    print(double_click)

def demo():
    print("Demo will start!")
    # while mouse.
    # move 750 right & 500 down
    mouse.move(x=750, y=500, absolute=True, duration=0.2)

    # drag from (0, 0) to (500, 500) relatively with a duration of 0.1s
    mouse.drag(start_x=0, start_y=0, end_x= 500, end_y=500, absolute=True, duration=1)

    # left click
    mouse.click("left")
    sleep(1)

    # right click
    mouse.click("right")
    sleep(1)

    # middle click
    mouse.click("middle")
    sleep(1)

    # scroll down
    mouse.wheel(-1)

    mouse_position = mouse.get_position()
    print("Mouse position:", mouse_position)

    # whether the right button is clicked
    right_pressed = mouse.is_pressed("right")
    print("Right button pressed:", right_pressed)

def mouse_recording():
    print("Mouse recoding started! and will continue till mouse is double clicked")
    # record until you click right
    events = mouse.record(button="left", target_types="double")
    print("Recoding finished!")

    sleep(1)

    # replay these events
    # print("Events recorded:\n", events)
    print("Replay started!")
    mouse.play(events[:-1])

# make a listener when left button is clicked
mouse.on_click(lambda: print("Left Button clicked."))
# make a listener when right button is clicked
mouse.on_right_click(lambda: print("Right Button clicked."))
# make a listener when middle button is clicked
mouse.on_middle_click(middle_button_clicked_listener)
# make a listener when mouse is double clicked
mouse.on_double_click(double_clicked_listener)

if __name__ == "__main__":
    print("Get the mouse position by clicking middle button.")
    print("Or move to the next part of the program by double clicking!")

    while not double_click:
        continue

    demo()
    mouse_recording()
    # remove the listeners when you want
    mouse.unhook_all()