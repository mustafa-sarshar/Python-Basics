# Source: https://people.csail.mit.edu/albert/bluez-intro/index.html

# Checking For Devices
import bluetooth

nearby_devices = bluetooth.discover_devices()

for i, device in enumerate(nearby_devices):
    print(f"{i} - {device}")

target_name = "My Phone"
target_address = None

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")
