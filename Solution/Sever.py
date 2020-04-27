"""Main program to start the server"""

from flask import Flask
from Hafifot.Solution.Routes import Person, Logger, MinistryOfHealth

app = Flask(__name__)
app.register_blueprint(Person.factory_route, url_prefix='/factory')
app.register_blueprint(Logger.events_route, url_prefix='/logger')
app.register_blueprint(MinistryOfHealth.moh_route, url_prefix='/moh')


def main():
    app.run(debug=True, port=5000)
    print(app.url_map)


if __name__ == "__main__":
    main()
