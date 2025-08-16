from tick_controller import TickController
import keyboard

from world.world_manager import WorldManager

tick_controller = TickController()
tick_controller.register(WorldManager())

print("Press SPACE to process tick, ESC to exit.")

while True:
    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
    if keyboard.is_pressed('space'):
        tick_controller.process_tick()
        while keyboard.is_pressed('space'):
            pass  # Wait for space to be released to avoid multiple triggers
