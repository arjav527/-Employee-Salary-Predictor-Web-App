from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load pre-trained model
model = joblib.load("salary_model.pkl")

# Sample encoding maps (must match training)
education_map = {
    "10th": 0, "12th": 1, "Bachelor's": 2, "Master's": 3, "PhD": 4
}
gender_map = {"Male": 0, "Female": 1}
occupation_map = {
    "Data Scientist": 0, "AI/ML Engineer": 1, "Data Analyst": 2,
    "Web Developer": 3, "Software Engineer": 4, "System Analyst": 5,
    "IT Consultant": 6, "Cybersecurity Analyst": 7,
    "Network Admin": 8, "Tech Support": 9
}
workclass_map = {
    "Private Sector": 0, "Freelancer / Self-employed": 1,
    "Government Job": 2, "Startup / Contract": 3,
    "Currently Unemployed": 4
}
country_map = {
    "India": 0, "United States": 1, "Canada": 2,
    "Germany": 3, "Australia": 4
}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        name = request.form["name"]
        age = int(request.form["age"])
        gender = gender_map[request.form["gender"]]
        education = education_map[request.form["education"]]
        occupation = occupation_map[request.form["occupation"]]
        workclass = workclass_map[request.form["workclass"]]
        experience = int(request.form["experience"])
        hours = int(request.form["hours"])
        country = country_map[request.form["country"]]

        # Construct feature vector
        features = np.array([[age, gender, education, occupation,
                              workclass, experience, hours, country]])

        prediction = model.predict(features)[0]
        predicted_salary = round(prediction, 2)

        # Text output
        prediction_text = f"""
        <strong>Hello {name}!</strong><br>
        Based on the information you provided, your predicted monthly salary is: 
        <strong>₹{predicted_salary}</strong>
        """

        return render_template("index.html",
                               prediction_text=prediction_text,
                               predicted_salary=predicted_salary)

    except Exception as e:
        return f"❌ Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
