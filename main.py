
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import tensorflow as tf

# Load pre-trained model for image analysis
model = tf.keras.models.load_model('home_improvement_model.h5')

# Initialize Flask app
app = Flask(__name__)

# Define home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define route for image analysis
@app.route('/analyse_image', methods=['POST'])
def analyse_image():
    # Get uploaded image from request
    image = request.files['image']

    # Preprocess image for analysis
    image = np.array(image) / 255.0

    # Predict project details using loaded model
    predictions = model.predict(np.expand_dims(image, axis=0))[0]

    # Extract project type, scope, materials, and tools from predictions
    project_type = predictions[0]
    project_scope = predictions[1]
    materials = predictions[2:7]
    tools = predictions[7:]

    # Render results page with project details
    return render_template('results.html', project_type=project_type, project_scope=project_scope, materials=materials, tools=tools)

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
