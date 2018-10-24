from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            textarea {{

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }}
        </style>

    </head>

    <body>

      <!-- create your form here -->
    <form action="/" method="post">

    <label>
    Rotate by:
    <input type="text" name= "rot" placeholder="0"/>
    </label>

    <textarea name="text">{0}</textarea>

    <input type="submit" value="Submit Query"/>
    </form>

    </body>

</html>"""
@app.route("/",methods=['POST'])
def encrypt():
    text_input = str(request.form["text"])

    numb_input = int(request.form["rot"])
    return form.format(rotate_string(text_input,numb_input))
@app.route("/")
def index():
    return form.format("")
app.run()