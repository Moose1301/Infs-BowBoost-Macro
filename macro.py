import keyboard
import mouse
import time

ascii_art = '\n $$$$$$\\                                 $$\\                     $$\\       $$\\                       $$\\      $$\\ $$$$$$$$\\ $$$$$$$\\  \n$$  __$$\\                                $$ |                    $$ |      $$ |                      $$$\\    $$$ |\\__$$  __|$$  __$$\\ \n$$ /  \\__| $$$$$$\\   $$$$$$\\   $$$$$$\\ $$$$$$\\    $$$$$$\\   $$$$$$$ |      $$$$$$$\\  $$\\   $$\\       $$$$\\  $$$$ |   $$ |   $$ |  $$ |\n$$ |      $$  __$$\\ $$  __$$\\  \\____$$\\\\_$$  _|  $$  __$$\\ $$  __$$ |      $$  __$$\\ $$ |  $$ |      $$\\$$\\$$ $$ |   $$ |   $$$$$$$  |\n$$ |      $$ |  \\__|$$$$$$$$ | $$$$$$$ | $$ |    $$$$$$$$ |$$ /  $$ |      $$ |  $$ |$$ |  $$ |      $$ \\$$$  $$ |   $$ |   $$  __$$< \n$$ |  $$\\ $$ |      $$   ____|$$  __$$ | $$ |$$\\ $$   ____|$$ |  $$ |      $$ |  $$ |$$ |  $$ |      $$ |\\$  /$$ |   $$ |   $$ |  $$ |\n\\$$$$$$  |$$ |      \\$$$$$$$\\ \\$$$$$$$ | \\$$$$  |\\$$$$$$$\\ \\$$$$$$$ |      $$$$$$$  |\\$$$$$$$ |      $$ | \\_/ $$ |   $$ |   $$ |  $$ |\n \\______/ \\__|       \\_______| \\_______|  \\____/  \\_______| \\_______|      \\_______/  \\____$$ |      \\__|     \\__|   \\__|   \\__|  \\__|\n                                                                                     $$\\   $$ |                                       \n                                                                                     \\$$$$$$  |                                       \n                                                                                      \\______/                                        \n'

def get_key_input(prompt):
    print(prompt)
    while True:
        if keyboard.is_pressed('esc'):
            print('Exiting key input.')
            return
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            return event.name
print(ascii_art)
print('Version: 1.2.2-SNAPSHOT')


def perform_actions(key1, key2):
    keyboard.press_and_release(key1)
    mouse.press(button='right')
    time.sleep(0.2)
    mouse.release(button='right')
    keyboard.press_and_release(key2)
    
print(ascii_art)
print("Please enter the key to your bow (e.g., '3'): ")
key1 = get_key_input("Press a key or 'esc' to quit.")
if key1 is None:
    exit()
print("Please enter the key to your sword (e.g., '1'): ")
key2 = get_key_input("Press a key or 'esc' to quit.")
if key2 is None:
    exit()
print("Please enter the key to toggle (e.g., 'V'): ")
trigger_key = get_key_input("Press a key to trigger the macro or 'esc' to quit.")
if trigger_key is None:
    exit()
print(f"Press '{trigger_key}' to execute the actions. Press '-' to quit.")
while True:
    if keyboard.is_pressed(trigger_key):
        perform_actions(key1, key2)
    elif keyboard.is_pressed('-'):
        print('Exiting...')
    time.sleep(0.05)
