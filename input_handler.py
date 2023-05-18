import os
import uinput

fifo_path = "/tmp/my_pipe"

# Create the named pipe if it doesn't exist
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

# Set up the uinput device
device = uinput.Device([
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
])

with open(fifo_path, "r") as fifo:
    while True:
        data = fifo.readline().strip()
        if data:
            print(f"Received: {data}")
            event, *args = data.split(" ")

            if event == "MOVE":
                x, y = map(int, args)
                device.emit(uinput.REL_X, x, syn=False)
                device.emit(uinput.REL_Y, y)
            elif event == "CLICK":
                button = int(args[0])
                if button == 1:
                    device.emit_click(uinput.BTN_LEFT)

# Clean up the named pipe when the daemon exits
os.remove(fifo_path)
