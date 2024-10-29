import keyboard
import mouse
import time
import os
import socket
from pymongo import MongoClient
ascii_art = '\n $$$$$$\\                                 $$\\                     $$\\       $$\\                       $$\\      $$\\ $$$$$$$$\\ $$$$$$$\\  \n$$  __$$\\                                $$ |                    $$ |      $$ |                      $$$\\    $$$ |\\__$$  __|$$  __$$\\ \n$$ /  \\__| $$$$$$\\   $$$$$$\\   $$$$$$\\ $$$$$$\\    $$$$$$\\   $$$$$$$ |      $$$$$$$\\  $$\\   $$\\       $$$$\\  $$$$ |   $$ |   $$ |  $$ |\n$$ |      $$  __$$\\ $$  __$$\\  \\____$$\\\\_$$  _|  $$  __$$\\ $$  __$$ |      $$  __$$\\ $$ |  $$ |      $$\\$$\\$$ $$ |   $$ |   $$$$$$$  |\n$$ |      $$ |  \\__|$$$$$$$$ | $$$$$$$ | $$ |    $$$$$$$$ |$$ /  $$ |      $$ |  $$ |$$ |  $$ |      $$ \\$$$  $$ |   $$ |   $$  __$$< \n$$ |  $$\\ $$ |      $$   ____|$$  __$$ | $$ |$$\\ $$   ____|$$ |  $$ |      $$ |  $$ |$$ |  $$ |      $$ |\\$  /$$ |   $$ |   $$ |  $$ |\n\\$$$$$$  |$$ |      \\$$$$$$$\\ \\$$$$$$$ | \\$$$$  |\\$$$$$$$\\ \\$$$$$$$ |      $$$$$$$  |\\$$$$$$$ |      $$ | \\_/ $$ |   $$ |   $$ |  $$ |\n \\______/ \\__|       \\_______| \\_______|  \\____/  \\_______| \\_______|      \\_______/  \\____$$ |      \\__|     \\__|   \\__|   \\__|  \\__|\n                                                                                     $$\\   $$ |                                       \n                                                                                     \\$$$$$$  |                                       \n                                                                                      \\______/                                        \n'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_local_ip():
    """Get the local IP address of the machine."""
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

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
client = MongoClient('mongodb://<redacted>:<redacted>@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/bs9e4hbojsmyo8t?replicaSet=rs0')
db = client['bs9e4hbojsmyo8t']
collection = db['licenses']

def check_license(license_id):
    document = collection.find_one({'_id': license_id})
    return document and document.get('update', False)

def perform_actions(key1, key2):
    keyboard.press_and_release(key1)
    mouse.press(button='right')
    time.sleep(0.2)
    mouse.release(button='right')
    keyboard.press_and_release(key2)

def save_ip(license_id, ip_address):
    collection.update_one({'_id': license_id}, {'$set': {'ip': ip_address}}, upsert=True)
local_ip = get_local_ip()
license_id = input("Please enter your license ID (e.g., 'XXXX-XXXX-XXXX-XXXX'): ")
if not check_license(license_id):
    print('Invalid or inactive license. Exiting...')
    exit()
document = collection.find_one({'_id': license_id})
if document:
    stored_ip = document.get('ip')
    if stored_ip == '127.0.0.1':
        save_ip(license_id, local_ip)
    elif stored_ip and stored_ip != local_ip:
        print('This program is already registered to another IP address.')
        exit()
else:
    save_ip(license_id, local_ip)
clear_console()
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
