from flask import Flask, render_template, request, redirect, url_for, session
import random
import os
from dotenv import load_dotenv

load_dotenv()
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64
import requests

app = Flask(__name__)
app.secret_key = "orbitlink_secret_key"

# Function to simulate space delay
def calculate_signal_delay():
    # Distance between Earth and Mars changes
    # Approx 56 million km to 400 million km
    distance_million_km = random.randint(56, 400)

    # Speed of light = 300,000 km/sec
    speed_of_light = 300000

    # Convert million km to km
    distance_km = distance_million_km * 1_000_000

    delay_seconds = distance_km / speed_of_light
    delay_minutes = round(delay_seconds / 60, 2)

    return distance_million_km, delay_minutes

def generate_graph(one_way, round_trip):
    plt.figure()
    labels = ['One Way Delay', 'Round Trip Delay']
    values = [one_way, round_trip]

    plt.bar(labels, values)
    plt.ylabel('Delay (minutes)')
    plt.title('Space Communication Delay')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    graph_url = base64.b64encode(img.getvalue()).decode()

    plt.close()

    return graph_url
#NASA API
def get_nasa_apod():
    api_key = os.environ.get("NASA_API_KEY")

    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        image_url = data.get("url")
        title = data.get("title")
        explanation = data.get("explanation")

        return image_url, title, explanation

    except:
        return None, None, None

#Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
      return redirect(url_for("login"))
    message = None
    distance = None
    delay = None
    mars_reply = None
    destination = None
    round_trip = None
    graph = None
    image_url = None
    image_title = None
    image_explanation = None

    if request.method == "POST":
        user_message = request.form["message"]

        distance, delay = calculate_signal_delay()

        # Round trip delay (Earth -> Mars -> Earth)
        round_trip = round(delay * 2, 2)

        message = f"Mars received: {user_message}"
        graph = generate_graph(delay, round_trip)
        image_url, image_title, image_explanation = get_nasa_apod()

        # Simple AI-style Mars reply
        mars_replies = [
            "Greetings from Mars! 👽",
            "Signal received clearly on Mars.",
            "Mars colony acknowledges your message.",
            "We are analyzing Earth's transmission.",
            "Communication stable across orbit."
        ]

        mars_reply = random.choice(mars_replies)

    return render_template("index.html",
                       message=message,
                       distance=distance,
                       delay=delay,
                       round_trip=round_trip,
                       mars_reply=mars_reply,
                       graph=graph,
                       destination=destination,
                       image_url=image_url,
                       image_title=image_title,
                       image_explanation=image_explanation,
                       user=session.get("user"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
