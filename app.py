from flask import Flask, render_template, request, redirect
from packages.triangles import Triangle

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", triangleMessage="Enter triangle information above", triangleValidity="Trianlge Validity will appear here")

@app.route('/send', methods=["GET", "POST"])
def calc():
    if request.method == "GET":
        return redirect("/")
    else:
        userTriangle = Triangle(request.form.get("side_a"), request.form.get("side_b"), request.form.get("side_c"))
        return render_template("index.html", triangleMessage=userTriangle.triangleTypeStatement, triangleValidity=userTriangle.validtyStatement)