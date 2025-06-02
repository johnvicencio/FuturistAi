from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()  # Load environment variables early

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    current_year = datetime.now().year
    max_tokens = 200

    if request.method == "POST":
        birth_date = request.form.get("birth_date")
        birth_time = request.form.get("birth_time") or None
        birthplace = request.form.get("birthplace")
        full_name = request.form.get("full_name")
        custom_question = request.form.get("custom_question")

        prompt = f"""
        Generate a clear, simple, and direct future prediction within {max_tokens} tokens using:
        - Western Zodiac (Sun sign, Moon sign, Rising sign if determinable)
        - Chinese Zodiac (animal and element)
        - Numerology (Life Path number, Destiny number, etc.)

        Use the following details:
        - Full name at birth: {full_name}
        - Date of birth: {birth_date}
        {"- Time of birth: " + birth_time if birth_time else ""}
        - Place of birth: {birthplace}

        Speak directly to the person using "you" instead of third person.
        Keep the tone personal and encouraging.

        {"Also answer this question: " + custom_question if custom_question else ""}

        Do not be verbose or detailed beyond {max_tokens} tokens.
        """

        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            prediction = completion.choices[0].message.content

        except Exception as e:
            prediction = f"Error: {str(e)}"

        return render_template("index.html", prediction=prediction, current_year=current_year,
                               birth_date=birth_date, birth_time=birth_time,
                               birthplace=birthplace, full_name=full_name,
                               custom_question=custom_question)

    return render_template("index.html", current_year=current_year, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)