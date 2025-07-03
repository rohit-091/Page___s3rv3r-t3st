import time
import requests

def read(filename):
    return open(filename).read().strip()

def main():
    token = read("token.txt")
    convo = read("convo.txt")
    msg = read("message.txt")
    delay = int(read("time.txt") or 0)
    name = read("name.txt")

    # delay wait before sending
    time.sleep(delay)

    # send message via Facebook Graph API
    url = f"https://graph.facebook.com/{convo}/messages"
    data = {
        "message": msg,
        "access_token": token
    }
    res = requests.post(url, data=data)
    print("Message sent!", res.text)

if __name__ == "__main__":
    main()
