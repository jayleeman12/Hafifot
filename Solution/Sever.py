"""Main program to start the server and init corona department"""

from flask import Flask, request
from Hafifot.Solution.Routes import Person, Logger
from Hafifot.Solution.Controllers.MinistryOfHealth import CoronaDept

app = Flask(__name__)
app.register_blueprint(Person.factory_route, url_prefix='/factory')
app.register_blueprint(Logger.events_route, url_prefix='/logger')


if __name__ == "__main__":
    corona_dept = CoronaDept()
    app.run(debug=True, port=5000)
    print(app.url_map)
