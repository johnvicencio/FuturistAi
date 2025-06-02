def generate_prompt(full_name, birth_date, birth_time, sun_sign, moon_sign, asc_sign,
                    chinese_zodiac, life_path, custom_question, max_tokens):
    custom_q = f"Also answer this question: {custom_question}" if custom_question else ""
    return f"""
    You are an expert astrologer and numerologist. Provide a clear and inspiring prediction
    for the next 12 months using the following birth data:

    Full name: {full_name}
    Sun Sign: {sun_sign}, Moon Sign: {moon_sign}, Rising Sign: {asc_sign}
    Chinese Zodiac: {chinese_zodiac}
    Life Path Number: {life_path}

    Birth date and time: {birth_date} {birth_time}

    {custom_q}

    Be encouraging, brief, and specific. Limit the response to {max_tokens} tokens.
    """
