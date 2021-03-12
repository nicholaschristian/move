import pyautogui
import time
import sys

class Mover:
    def __init__(self, runtime_minutes=0, sleep_time=5):
        pyautogui.FAILSAFE = False
        self.runtime_minutes = runtime_minutes
        self.sleepTime = sleep_time

    def move_to_relative(self, num_px):
        right = True
        if self.runtime_minutes == 0:
            print("Running until stopped....")
            if num_px:
                while True:
                    if right:
                        pyautogui.moveRel(xOffset=num_px, yOffset=num_px)
                        print(pyautogui.position())
                        right = False
                    else:
                        pyautogui.moveRel(xOffset=-num_px, yOffset=-num_px)
                        print(pyautogui.position())
                        right = True

                    time.sleep(self.sleepTime)
            else:
                print("ERROR: Coordinates required")

        else:
            print("Running for {} minute(s)".format(self.runtime_minutes))
            t_end = time.time() + 60 * self.runtime_minutes

            while time.time() < t_end:
                if num_px:
                    if right:
                        pyautogui.moveRel(xOffset=num_px, yOffset=num_px)
                        print(pyautogui.position())
                        right = False
                    else:
                        pyautogui.moveRel(xOffset=-num_px, yOffset=-num_px)
                        print(pyautogui.position())
                        right = True

                    time.sleep(self.sleepTime)
                else:
                    print("ERROR: Coordinates required")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        runtime = sys.argv[1]
        m = Mover(runtime_minutes=float(runtime))
        m.move_to_relative(num_px=1)
    else:
        print("\nRuntime argument required. Use 0 to run until manually stopped. Runtime otherwise measured in minutes.\n")