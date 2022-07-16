"""
Source: https://www.thepythoncode.com/article/control-mouse-python
"""

import sys
import mouse
from time import sleep

n_clicked = 0
mouse_positions = []

n_clicks = 0
if len(sys.argv) < 2: sys.exit(0)
else: n_clicks = int(sys.argv[1])

clicking_delay = 1
if len(sys.argv) > 2: clicking_delay = float(sys.argv[2])

mouse_move_duration = 0.1
if len(sys.argv) > 3: mouse_move_duration = float(sys.argv[3])

def middle_button_clicked_listener(*args):
    global n_clicked, mouse_positions
    pos_x, pos_y = mouse.get_position()
    print(f"Mouse position: x ({pos_x}), y ({pos_y})")
    mouse_positions.append((pos_x, pos_y))
    n_clicked += 1

def automatic_clicking(mouse_position, click="left", delay=1):
    pos_x, pos_y = mouse_position
    mouse.move(x=pos_x, y=pos_y, absolute=True, duration=mouse_move_duration)
    mouse.click(click)
    if delay != 0:
        sleep(delay)

mouse.on_middle_click(middle_button_clicked_listener)

if __name__ == "__main__":
    print(f"You will click {n_clicks} times!")
    print(f"Please press middle button {n_clicks} times to save the position of mouse!")
    
    while n_clicked < n_clicks:
        continue
    print(f"{n_clicked} mouse positions were captured!")
    
    repeat = "y"
    while repeat == "y":
        _ = input("Press a key to start ...")
        for i in range(n_clicks):
            automatic_clicking(mouse_positions[i], delay=clicking_delay)        
        repeat = input("Do you want to repeat? (y/n): ").lower().strip()        
    
    # remove the listeners when you want
    mouse.unhook_all()