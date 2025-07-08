💼 Employee Salary Predictor-Web-App
An intelligent, interactive, and visually modern web application that predicts the monthly salary of an employee based on multiple input factors such as age, gender, education, occupation, experience, work hours, and country.

Built using Python (Flask) on the backend and a beautiful responsive frontend with Chart.js, jsPDF, Lottie animations, and PDF generation capabilities. The project leverages a trained machine learning model for accurate salary forecasting.

📌 Live Demo
🌐 Click here to view the deployed app (Add after deployment)

## 📸 Screenshots

### 🌓 Dark & Light Mode UI
| Light Mode              | Dark Mode               |
|-------------------------|-------------------------|
| ![](screens/light.png)  | ![](screens/dark.png)   |

### 📊 Salary Comparison Chart
![Salary Chart](screens/chart.png)

🚀 Features
✅ ML-Based Salary Prediction
Predicts monthly salary based on realistic job features.

✅ Glassmorphism UI
Modern, clean, and responsive design with dark/light toggle.

✅ Chart-Based Visualization
Compares predicted salary with average using interactive bar chart.

✅ PDF Report Generator
Instantly download a polished salary report as a PDF.

✅ Lottie Animations
Professional animations for smoother user experience.

✅ Personalized Feedback
Greeting + prediction with user’s name for human-centric experience.

🧠 How It Works
User fills out the web form with their job details.

Input data is preprocessed and encoded.

A trained ML regression model (salary_model.pkl) processes the input.

Predicted salary is displayed with a salary comparison chart.

User can download the result chart as a PDF report.

🧰 Tech Stack
Layer	Tools Used
🖥️ Frontend	HTML5, CSS3, JavaScript, Chart.js, jsPDF, Lottie
🧠 Backend	Python, Flask
📊 ML Model	scikit-learn (Linear Regression)
📦 Model I/O	joblib
☁ Deployment	Render

📁 Project Structure
employee-salary-predictor/
├── app.py                  # Flask backend
├── salary_model.pkl        # Trained ML model
├── requirements.txt        # Python packages
├── Procfile                # For deployment on Render
├── templates/
│   └── index.html          # Web frontend (with Jinja2)
└── static/ (optional)      # Custom JS, CSS, images

🔧 Setup Instructions
✅ Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/employee-salary-predictor.git
cd employee-salary-predictor
✅ Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Step 3: Run Locally
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000/

🌍 Deploying on Render
Push your project to GitHub

Go to Render.com

Click "New Web Service"

Connect your GitHub repo

Set:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Click Deploy ✅

🧪 Sample Inputs
Field	Value
Name	Arjav Jain
Age	24
Gender	Male
Education	Bachelor's
Occupation	Data Analyst
Workclass	Private Sector
Experience	2
Hours/week	40
Country	India

🧾 Output
Predicted Salary: ₹27,000 – ₹32,000/month

Chart: Your Salary vs Average

PDF Report: Downloadable & sharable chart snapshot

📦 requirements.txt
txt
Copy
Edit
Flask
joblib
numpy
pandas
scikit-learn
gunicorn
📋 License
This project is open-source and free to use for learning, academic, or demo purposes.

👤 Author
Arjav Jain
BCA Final Year Student | Aspiring Data Analyst
📫 LinkedIn

⭐️ Want to Contribute?
Fork it, improve it, and send a pull request! This project welcomes community involvement and feedback.

