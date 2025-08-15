from tick_controller import TickController
import keyboard

tick_controller = TickController()
tick_controller.register("Module1")
tick_controller.register("Module2")
tick_controller.register("Module3")

print("Press SPACE to process tick, ESC to exit.")

while True:
    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
    if keyboard.is_pressed('space'):
        tick_controller.process_tick()
        while keyboard.is_pressed('space'):
            pass  # Wait for space to be released to avoid multiple triggers
