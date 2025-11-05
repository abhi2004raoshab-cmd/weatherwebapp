from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv(" 8dcd38918b518318095958b6342b384e")
import requests

app = Flask(__name__)  # ✅ Use __name__, not _name_
API_KEY = ' 8dcd38918b518318095958b6342b384e ' # Replace with your actual API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={ '8dcd38918b518318095958b6342b384e'  }&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].capitalize(),
                }
            else:
                error = "City not found!"
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":  # ✅ Use __name__ and __main__
    app.run(debug=True)
