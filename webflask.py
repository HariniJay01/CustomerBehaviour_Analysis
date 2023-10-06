import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve user input from the request
    input_data = request.form['input_data']

    # Preprocess the input data as required

    # Make predictions using the loaded model
    prediction = model.predict([input_data])

    # Process the prediction result as needed

    # Render the result template with the prediction
    return render_template('result.html', prediction=prediction)
