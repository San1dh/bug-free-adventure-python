from flask import Flask, request, render_template

import pytz
from datetime import datetime


def get_date_and_time(timezone):
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezones = pytz.all_timezones
        return {
            "ok": "error",
            "error": "Unknown timezone",
            "available_timezones": timezone
        }
    data = datetime.now(tz)
    date = data.strftime("%d-%m-%Y")
    time = data.strftime("%H:%M:%S")
    return {"ok": "true", "date": date, "time": time}


# get_date_and_time("asia/kolkata")

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/data")
def data():
    timezone = request.args.get("timezone")
    return (
        get_date_and_time(timezone=timezone)
        if timezone
        else {"ok": "error", "error": "No timezone provided"}
    )

# if __name__ == "__main__":
#     app.run(debug = True)
