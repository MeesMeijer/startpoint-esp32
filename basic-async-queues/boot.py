# boot.py -- run on boot-up

from network import WLAN, STA_IF

wlan = WLAN(STA_IF)
mac = wlan.config("mac")

print(f"[boot.py] - espmac: {mac}")

