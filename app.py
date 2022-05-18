from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("landing_page.html", title="Home page")

@app.route("/time-managment")
def view_time_management():
    return render_template("time_management.html", title="Time Management")

@app.route("/mental-strain")
def view_mental_strain():
    return render_template("mental_health.html", title="Mental Strain")
    
@app.route("/finacials")
def view_finacials():
    return render_template("financial.html", title="Finacials")
    
app.run(debug=True)
    
