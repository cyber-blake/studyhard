from itertools import cycle
import time

led_states = cycle(["🔴", "🟡", "🟢", "🔵"])

while True:
    print(f"\rСветодиод: {next(led_states)}", end="")
    time.sleep(0.5)
