from flask import Flask, render_template, request
import requests
import time
import threading

app = Flask(__name__)


def ping_site(url, interval):
    while True:
        try:
            response = requests.get(url)
            print(f"Ping at {time.ctime()}: Status Code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ping at {time.ctime()}: Failed to reach {url}")
            print(e)
        time.sleep(interval)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_ping', methods=['POST'])
def start_ping():
    url = "https://asimai.onrender.com/"
    interval = int(request.form['interval'])
    threading.Thread(target=ping_site, args=(url, interval)).start()

    return f"Ping işlemi {interval} saniye aralıklarla başlatıldı!"


if __name__ == '__main__':
    app.run(debug=True)
