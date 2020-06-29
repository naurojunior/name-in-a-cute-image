from flask import (
    Flask,
    jsonify,
    request,
    send_file
)

from images import (
    image_with_text,
    save_image
)

import uuid

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def image():
    uuid_return = str(uuid.uuid4())
    output_filename = uuid_return + ".jpg"

    data = request.json
    save_image(image_with_text(data['name']), ("temp/" + output_filename) )
    return jsonify({'filename' : uuid_return})

@app.route('/image', methods=['GET'])
def get_image():
    id = request.args.get('id').replace(".", "")
    return send_file('temp/' + id + '.jpg', mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)
