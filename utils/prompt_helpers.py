from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def native_astro_prediction(full_name, birth_date, birth_time, sun_sign, moon_sign, asc_sign, chinese_zodiac, life_path, custom_question):
    profile_summary = f"""
    Full Name: {full_name}
    Birth Date: {birth_date}
    Birth Time: {birth_time}
    Sun Sign: {sun_sign}
    Moon Sign: {moon_sign}
    Ascendant: {asc_sign}
    Chinese Zodiac: {chinese_zodiac}
    Life Path Number: {life_path}
    Custom Question: {custom_question}
    """

    prompt = f"""
    You are a friendly and insightful astrologer and numerologist.
    Based on this person's birth chart and numbers, write a warm and easy-to-understand prediction.
    Avoid technical jargon. Answer their custom question with intuitive and gentle advice.

    Here is the user's profile:
    {profile_summary}

    Give the prediction below:

    Sign the message at the end as: FuturistAi, your cosmic servant.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert astrologer and numerologist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"""
        Hello {full_name},

        We're having a bit of trouble generating your full prediction right now. 
        Here's a quick summary based on your data:

        - Sun Sign: {sun_sign}
        - Moon Sign: {moon_sign}
        - Ascendant: {asc_sign}
        - Chinese Zodiac: {chinese_zodiac}
        - Life Path Number: {life_path}

        Stay positive and trust your journey. Try again later for your full reading!
        Error: {str(e)}
        """