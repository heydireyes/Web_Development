from flask_webapp import create_app
from flask import Flask


application = create_app()



if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
