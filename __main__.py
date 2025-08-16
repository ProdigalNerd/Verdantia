import time
import threading
import sys

from rich.live import Live

from tick_controller import TickController
from world.world_manager import WorldManager
from console.layout_manager import LayoutManager

world_manager = WorldManager()
layout_manager = LayoutManager()

tick_controller = TickController()
tick_controller.register(world_manager)

quit_flag = False
def listen_for_quit():
    global quit_flag
    try:
        if sys.platform == "win32":
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode("utf-8").lower()
                    if key == 'q':
                        quit_flag = True
                        break
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                while True:
                    key = sys.stdin.read(1).lower()
                    print("oh hi there")
                    print(key)
                    if key == 'q':
                        quit_flag = True
                        break
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except Exception as e:
        quit_flag = True
        print(e)
threading.Thread(target=listen_for_quit, daemon=True).start()

def main():
    global quit_flag
    with Live(layout_manager.render_layout(world_manager.get_map(), {}), refresh_per_second=4) as live:
        while not quit_flag:
            print(quit_flag)
            tick_controller.process_tick()
            live.update(layout_manager.render_layout(world_manager.get_map(), {}))
            time.sleep(1)

if __name__ == "__main__":
    main()
