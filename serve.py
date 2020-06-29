from flask import (
    Flask,
    jsonify,
    request
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/image', methods=['POST'])
def image():
    data = request.json

    name['name']
    return jsonify(data)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)