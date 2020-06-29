from flask import (
    Flask,
    jsonify,
    request
)

from images import (
    image_with_text,
    save_image
)

import uuid

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def image():
    output_filename = str(uuid.uuid4()) + ".jpg"

    data = request.json
    save_image(image_with_text(data['name']), ("temp/" + output_filename) )
    return jsonify({'filename' : output_filename})

if __name__ == '__main__':
    app.run(debug=True)
