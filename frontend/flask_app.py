from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.main import Main

app = Flask(__name__)
CORS(app) 
@app.route('/upload', methods=['POST'])
def upload_image():
    api_key = request.form.get('api-key')
    prompt = request.form.get('prompt', '')
    framework = request.form.get('framework')
    image = request.files.get('image-upload')
    
    if not api_key or not image or not framework:
        return jsonify({'error': 'API key, image, and framework are required!'}), 400
    
    #saving the image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        image.save(temp_image.name)
        image_path = temp_image.name

    print(f"\n\n\n IMAGE saved at: {image_path}\n\n\n")

    #passing the image path to the backend connection
    output = backend_connection(api_key, framework, image_path, prompt)
    os.remove(image_path)

    return jsonify({'output': output})

def backend_connection(api_key, programming_languages, image_path, prompt):
    main = Main()
    return main.main_fun(api_key, programming_languages, image_path, prompt)

if __name__ == '__main__':
    app.run(debug=True)
