'''
    Course: CST 205
    Title: CST 205 Final
    Abstract: Site showcasing information on three college related stressors
    Group 7333: Isai Molina, Joshua Gonong, Arise Tran
    Date: 17 May 2022
'''

from flask import Flask, render_template

app = Flask(__name__)

# All worked on landing page
@app.route("/")
def view_home():
    return render_template("landing_page.html", title="Home page")

#Isai worked on time management 
@app.route("/time-managment")
def view_time_management():
    return render_template("time_management.html", title="Time Management")

#Arise worked on mental strain
@app.route("/mental-strain")
def view_mental_strain():
    return render_template("mental_health.html", title="Mental Strain")
    
#Joshua worked on finacial 
@app.route("/finacials")
def view_finacials():
    return render_template("financial.html", title="Finacials")

app.run(debug=True)
    
