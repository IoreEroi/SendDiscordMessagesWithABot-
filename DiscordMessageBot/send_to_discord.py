import requests
import time
import json

CONFIG_FILE = 'config.json'
MESSAGES_FILE = 'messages.txt'

def load_config():
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)

def send_message_to_discord(token, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'content': message
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Message successfully sent to channel {channel_id}")
        save_message(message)
    else:
        print(f"Error sending message to channel {channel_id}: {response.status_code}")
        print(response.json())

def save_message(message):
    with open(MESSAGES_FILE, 'a') as file:
        file.write(message + '\n')

def load_messages():
    try:
        with open(MESSAGES_FILE, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

if __name__ == '__main__':

    config = load_config()
    servers = config['servers']
    
    interval = 30  # Fixed time interval of 30 seconds
    
    message = input("Enter the message to send to Discord: ")
    
    while True:
        for server in servers.values():
            send_message_to_discord(server['token'], server['channel_id'], message)
        time.sleep(interval)
