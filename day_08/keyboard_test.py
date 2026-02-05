import keyboard
import time

def on_arrow_press(event):
    if event.name == 'up':
        print('Up arrow key pressed!')
    elif event.name == 'down':
        print('Down arrow key pressed!')
    elif event.name == 'left':
        print('Left arrow key pressed!')
    elif event.name == 'right':
        print('Right arrow key pressed!')

# Hook the key press event
keyboard.on_press(on_arrow_press)

print("Press arrow keys (Press Ctrl+C to exit)")

try:
    # Keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")