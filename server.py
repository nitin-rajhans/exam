from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to itil exam modules: itil and devops, me: prn 230344223037 name: nitin , phone number : 9172536238"


# run the application
app.run(host="0.0.0.0", port=4000, debug=True)
