from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

### PART TWO

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


# # Put your app in here.
# from flask import Flask, request

# app = Flask(__name__)

# # @app.route('/add')
# # def add():
# #     a = request.args["term"]
# #     return f"<h1>Search Results For: {term} </h1>" 

# @app.route('/add')
# def search():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = a + b
#     print(request.args)
#     return f"<h1> Search: {result}</h1>"

# @app.route('/sub')
# def sub(): 
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = b - a 
#     return f"<h1> Search: {result}</h1>"

# @app.route('/mult')
# def mult():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = b * a 
#     return f"<h1> Search: {result}</h1>"

# @app.route('/div')
# def div():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = b / a 
#     return f"<h1> Search: {result}</h1>"

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)