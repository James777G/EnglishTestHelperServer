import os
import uuid

from flask import Flask, request, jsonify

from algo.image_processor import process_images

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/process_images', methods=['POST'])
def process_uploaded_images():
    # Check if files were uploaded
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part'})

    files = request.files.getlist('files[]')
    image_paths = []

    # Iterate through each uploaded file
    for file in files:
        # Check if the file is empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Check if the file is an allowed format (you may adjust these)
        allowed_formats = {'png', 'jpg', 'jpeg', 'gif'}
        if '.' not in file.filename or file.filename.split('.')[-1].lower() not in allowed_formats:
            return jsonify({'error': 'Invalid file format'})

        # Generate a unique filename using uuid
        unique_filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1].lower()

        # Save the uploaded file to a static folder with the unique filename
        file.save(os.path.join('static', unique_filename))
        image_paths.append(os.path.join('static', unique_filename))

    # Process the uploaded images and generate the English test answer
    result = process_images(image_paths)

    # Delete the uploaded image files
    for image_path in image_paths:
        os.remove(image_path)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

