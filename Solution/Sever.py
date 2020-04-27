"""Main program to start the server"""

from flask import Flask
from Hafifot.Solution.Routes import Person, Logger

app = Flask(__name__)
app.register_blueprint(Person.factory_route, url_prefix='/factory')
app.register_blueprint(Logger.events_route, url_prefix='/logger')


def main():
    app.run(debug=True, port=5000)
    print(app.url_map)


if __name__ == "__main__":
    main()
