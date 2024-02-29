from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_hello():
    return "Hello, worl!"


if __name__ == '__main__':
    app.run(
        debug=True, # Optional but useful for now
        host="0.0.0.0" # Listen for connections directed _to_ any address
    )
