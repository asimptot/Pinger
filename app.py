from flask import Flask
import requests
import time
import threading

app = Flask(__name__)

# Sabit ping aralığı (30 saniye)
PING_INTERVAL = 31

# Ping fonksiyonu
def ping_site(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Ping at {time.ctime()}: Status Code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ping at {time.ctime()}: Failed to reach {url}")
            print(e)
        time.sleep(PING_INTERVAL)

# Flask uygulaması başlatıldığında ping işlemini başlatmak
@app.before_first_request
def start_ping_on_app_start():
    url = "https://asimai.onrender.com/"
    threading.Thread(target=ping_site, args=(url,), daemon=True).start()

# Anasayfa route'u
@app.route('/')
def index():
    return "Ping işlemi 30 saniye aralıklarla başlatıldı!"

if __name__ == '__main__':
    app.run(debug=True)
