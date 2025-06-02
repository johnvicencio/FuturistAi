from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import swisseph as swe
import os

from utils.astro_helpers import calculate_life_path_number, get_chinese_zodiac, fetch_astrological_signs
from utils.prompt_helpers import generate_prompt

load_dotenv()  # Load environment variables early

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set the ephemeris path to your local ephemeris files
swe_path = "static/lib/ephemeris"

app = Flask(__name__)

def calculate_life_path_number(birth_date_str):
    digits = ''.join(d for d in birth_date_str if d.isdigit())
    total = sum(int(d) for d in digits)
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

def get_chinese_zodiac(year):
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    animal = animals[(year - 4) % 12]
    element = elements[((year - 4) % 10) // 2]
    return f"{element} {animal}"

def calculate_sun_moon_asc_global(birth_date, birth_time, place):
    from datetime import datetime
    import pytz
    import swisseph as swe
    from geopy.geocoders import Nominatim
    from timezonefinder import TimezoneFinder

    # Set ephemeris path
    swe.set_ephe_path("static/lib/ephemeris")

    # Step 1: Get coordinates
    geolocator = Nominatim(user_agent="astro_app")
    location = geolocator.geocode(place)
    if not location:
        raise ValueError("Invalid location")
    lat, lon = location.latitude, location.longitude

    # Step 2: Get timezone
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    if not timezone_str:
        raise ValueError("Could not determine timezone")

    # Step 3: Parse datetime and convert to UTC
    local_tz = pytz.timezone(timezone_str)
    naive_dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    local_dt = local_tz.localize(naive_dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    # Step 4: Convert to Julian Day
    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                       utc_dt.hour + utc_dt.minute / 60.0)

    # Step 5: Get Sun, Moon, and Ascendant
    sun = swe.calc_ut(jd_ut, swe.SUN)[0][0]
    moon = swe.calc_ut(jd_ut, swe.MOON)[0][0]
    asc = swe.houses(jd_ut, lat, lon)[0][0]  # First house cusp = Ascendant

    def get_sign(deg):
        signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        return signs[int(deg // 30)]

    return {
        "sun_sign": get_sign(sun),
        "moon_sign": get_sign(moon),
        "asc_sign": get_sign(asc)
    }

def fetch_astrological_signs(birth_date, birth_time, place):
    return calculate_sun_moon_asc_global(birth_date, birth_time, place)

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    current_year = datetime.now().year
    max_tokens = 300

    if request.method == "POST":
        birth_date = request.form.get("birth_date")
        birth_time = request.form.get("birth_time") or "12:00"
        full_name = request.form.get("full_name")
        custom_question = request.form.get("custom_question")
        place = request.form.get("place")

        try:
            dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
            life_path = calculate_life_path_number(birth_date)
            chinese_zodiac = get_chinese_zodiac(dt.year)
            signs = fetch_astrological_signs(birth_date, birth_time, place)

            prompt = generate_prompt(
                full_name=full_name,
                birth_date=birth_date,
                birth_time=birth_time,
                sun_sign=signs.get("sun_sign"),
                moon_sign=signs.get("moon_sign"),
                asc_sign=signs.get("asc_sign"),
                chinese_zodiac=chinese_zodiac,
                life_path=life_path,
                custom_question=custom_question,
                max_tokens=max_tokens
            )

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert astrologer and numerologist."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            prediction = completion.choices[0].message.content

        except Exception as e:
            prediction = f"Error: {str(e)}"

        return render_template("index.html", prediction=prediction, current_year=current_year,
                               birth_date=birth_date, birth_time=birth_time,
                               full_name=full_name, custom_question=custom_question)

    return render_template("index.html", current_year=current_year, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)