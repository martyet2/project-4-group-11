from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper
import os

print(__file__)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/tableau2")
def tableau2():
    # Return template and data
    return render_template("tableau2.html")

@app.route("/tableau3")
def tableau3():
    # Return template and data
    return render_template("tableau3.html")

@app.route("/work_cited")
def work_cited():
    # Return template and data
    return render_template("work_cited.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    country = content["country"]
    amount_usd = float(content["amount_usd"])
    transaction_type = content["transaction_type"]
    month = int(content["month"])
    industry = content["industry"]
    destination_country = content["destination_country"]
    reported_by_authority = bool(int(content["reported_by_authority"]))
    shell_companies_involved = int(content["shell_companies_involved"])
    money_laundering_risk_score = int(content["money_laundering_risk_score"])
    tax_haven_country = content["tax_haven_country"]

    preds = modelHelper.makePredictions(country, amount_usd, transaction_type, month, industry, destination_country, reported_by_authority, 
                                        shell_companies_involved, money_laundering_risk_score, tax_haven_country)
    return(jsonify({"ok": True, "prediction": str(preds)}))


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
