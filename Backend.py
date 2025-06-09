from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import torch
import os
from ml_model import load_model_and_predict
from combine import extract_and_combine

app = Flask(__name__)

@app.route('/analyze/', methods=['POST'])
def analyze_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join('uploads', filename)
    file.save(file_path)

    features = extract_and_combine(file_path)
    mbti_type = load_model_and_predict(features)
    profession = recommend_profession(mbti_type)

    return jsonify({'mbti_type': mbti_type, 'profession': profession})

if __name__ == '__main__':
    app.run(debug=True)
