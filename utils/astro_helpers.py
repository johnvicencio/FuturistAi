import swisseph as swe
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

swe.set_ephe_path("static/lib/ephemeris")

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

def get_sign(deg):
    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
             'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    return signs[int(deg // 30)]

def calculate_sun_moon_asc(birth_date, birth_time, place):
    geolocator = Nominatim(user_agent="astro_app")
    location = geolocator.geocode(place)
    if not location:
        raise ValueError("Invalid location")
    lat, lon = location.latitude, location.longitude

    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    if not timezone_str:
        raise ValueError("Could not determine timezone")

    local_tz = pytz.timezone(timezone_str)
    naive_dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    local_dt = local_tz.localize(naive_dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                       utc_dt.hour + utc_dt.minute / 60.0)

    sun = swe.calc_ut(jd_ut, swe.SUN)[0][0]
    moon = swe.calc_ut(jd_ut, swe.MOON)[0][0]
    asc = swe.houses(jd_ut, lat, lon)[0][0]

    return {
        "sun_sign": get_sign(sun),
        "moon_sign": get_sign(moon),
        "asc_sign": get_sign(asc)
    }

def fetch_astrological_signs(birth_date, birth_time, place):
    return calculate_sun_moon_asc(birth_date, birth_time, place)
