from flask import Flask, render_template, request
from datetime import datetime

from utils.astro_helpers import calculate_life_path_number, get_chinese_zodiac, fetch_astrological_signs
from utils.prompt_helpers import native_astro_prediction
from utils.url_helpers import override_url_for

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.context_processor(override_url_for) 

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    current_year = datetime.now().year

    if request.method == "POST":
        birth_date = request.form.get("birth_date")
        birth_time = request.form.get("birth_time") or "12:00"
        full_name = request.form.get("full_name")
        custom_question = request.form.get("custom_question")
        place = request.form.get("place")

        try:
            # Validate time format
            try:
                dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
            except ValueError:
                raise ValueError("Invalid birth time format. Please use HH:MM in 24-hour format.")

            # Calculate astrology values
            life_path = calculate_life_path_number(birth_date, reduce_master=True)
            chinese_zodiac = get_chinese_zodiac(dt.year)
            signs = fetch_astrological_signs(birth_date, birth_time, place)

            prediction = native_astro_prediction(
                full_name=full_name,
                birth_date=birth_date,
                birth_time=birth_time,
                sun_sign=signs.get("sun_sign"),
                moon_sign=signs.get("moon_sign"),
                asc_sign=signs.get("asc_sign"),
                chinese_zodiac=chinese_zodiac,
                life_path=life_path,
                custom_question=custom_question
            )

        except Exception as e:
            prediction = f"Error: {str(e)}"

        return render_template("index.html", prediction=prediction, current_year=current_year,
                               birth_date=birth_date, birth_time=birth_time,
                               full_name=full_name, custom_question=custom_question, place=place)

    return render_template("index.html", current_year=current_year, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)