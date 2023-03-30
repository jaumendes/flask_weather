from flask import Flask, render_template, request
import requests
from openweather import KEY


app = Flask(__name__)

@app.route('/city', methods=('GET', 'POST'))
def get_weather():
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={KEY}'
        res = requests.get(url)
        data = res.json()
        return render_template('index.html', city=city, data=data)
    return render_template('index.html')



