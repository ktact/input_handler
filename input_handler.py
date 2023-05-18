import os
import json
import uinput

fifo_path = "/tmp/my_pipe"

# Create the named pipe if it doesn't exist
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

# Set up the uinput device
device = uinput.Device([
    uinput.ABS_X + (0, 1920, 0, 0),
    uinput.ABS_Y + (0, 1080, 0, 0),
    uinput.BTN_LEFT,
])

with open(fifo_path, "r") as fifo:
    while True:
        event = fifo.readline().strip()

        if event:
            coordinate = json.loads(event)

            device.emit(uinput.ABS_X, coordinate['x'], syn=False)
            device.emit(uinput.ABS_Y, coordinate['y'])

# Clean up the named pipe when the daemon exits
os.remove(fifo_path)
