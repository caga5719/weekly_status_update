from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/project_proposal')
def project_proposal():
    return render_template("project_proposal.html")

@app.route('/book_report')
def book_report():
    return render_template("book_report.html")

@app.route('/final_project_report')
def book_report():
    return render_template("final_project_report.html")

@app.route('/<week_chosen>')
def weekly_status_update(week_chosen):
    return render_template(f"{week_chosen}.html")

if __name__ == "__main__":
    app.run()
