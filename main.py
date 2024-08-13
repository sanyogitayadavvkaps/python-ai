from flask import Flask, request, jsonify, send_file
from rembg import remove
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app) 
@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Process the file
    input_image = file.read()
    output_image = remove(input_image)
    
    # Return the processed image
    return send_file(io.BytesIO(output_image), mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(port=8000)
