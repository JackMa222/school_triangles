from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", triangle_message="Enter triangle information above")

@app.route('/send', methods=["GET", "POST"])
def calc():
    triangleMessage = ""
    triangleError = False
    
    sides = [float(request.form.get('sidea')), float(request.form.get('sideb')), float(request.form.get('sidec'))]
    
    for side in sides:
        if side <= 0:
            triangleError = True
            triangleMessage = "Side length cannot be zero or a negative number"
    
    sidec = max(sides)
    sides.remove(sidec)
    sidea = sides[0]
    sideb = sides[1]
    
    if (sidea == sideb) and (sideb == sidec) and (sidea == sidec):
        triangle = "Equilateral"
    elif (sidea == sideb) or (sideb == sidec) or (sidea == sidec):
        triangle = "Isoceles"
    elif ((sidea ** 2) + (sideb ** 2)) == (sidec ** 2):
        triangle = "Right angle"
    else:
        triangle = "Scalene"
        
    if triangleError is False:
        triangleMessage = f"Triangle is {triangle}"
    return render_template("index.html", triangle_message=triangleMessage)