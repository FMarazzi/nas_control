from flask import Flask

app = Flask(__name__)
stopped = 0


@app.route("/")
def hello():
    global stopped
    return "Front page, downloads are " + ("stopped." if stopped else "not stopped.")


@app.route("/start")
def start():
    global stopped
    if stopped:
        stopped = 0
        # Code to restart the app
        return "Download resumed."
    else:
        return "Download still going."


@app.route("/stop")
def stop():
    global stopped
    if stopped:
        # Give info about the duration of this stop?
        return "Download already stopped."
    else:
        # Code to actually stop the app
        stopped = 1
        return "Download stopped."

if __name__ == "__main__":
    app.run()
