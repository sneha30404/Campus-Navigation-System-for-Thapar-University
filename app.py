from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Outdoor navigation form
@app.route("/outdoor_navigation", methods=["GET", "POST"])
def outdoor_navigation():
    if request.method == "POST":
        start = request.form.get("start_location")
        end = request.form.get("end_location")
        return render_template("outdoor_navigation.html", start=start, end=end)
    return render_template("outdoor_navigation_form.html")

if __name__ == "__main__":
    app.run(debug=True)
