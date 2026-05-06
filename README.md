Hotel Booking Cancellation Predictor

This project is a Machine Learning-based web application that predicts whether a hotel booking will be confirmed or canceled based on user inputs.

📌 Project Overview

The system takes booking details such as:

Lead Time
Average Price
Special Requests
Number of Guests
Number of Nights
Repeated Guest Status

It then uses a trained ML model to predict:

✅ Confirmed Booking
❌ Canceled Booking

🚀 Technologies Used
🔹 Frontend
HTML
CSS
JavaScript (Fetch API)
🔹 Backend
Python
Flask
🔹 Machine Learning
Scikit-learn
Gradient Boosting / Random Forest
RandomizedSearchCV (Hyperparameter tuning)
📂 Project Structure
project/
├──Backend
     └──app.py # Flask backend
     └── gb_booking_model.pkbl 
      
├── gb_booking_model.pkbl      # Trained ML model         # (Optional) Scaler
├── Frondend
│   └── index.html      # Frontend UI
 # Styling (optional)
└── README.md
⚙️ How It Works
User enters booking details in the web form
Frontend sends data to Flask API (/predict)
Backend processes input using trained ML model
Prediction is returned:
0 → Confirmed
1 → Canceled
Result is displayed on UI
▶️ How to Run the Project
Step 1: Install dependencies
pip install flask scikit-learn numpy pandas
Step 2: Run Flask server
python app.py

You will see:

Running on http://127.0.0.1:5000/
Step 3: Open the application
Open browser
Go to:
http://127.0.0.1:5000/
🧪 Sample Inputs
✅ Confirmed Booking
Lead Time: 0
Price: 100
Requests: 0
Guests: 2
Nights: 1
Repeat: 0
❌ Canceled Booking
Lead Time: 150
Price: 300
Requests: 0
Guests: 1
Nights: 1
Repeat: 0
🧠 Model Details
Algorithm: Gradient Boosting / Random Forest
Hyperparameter tuning using RandomizedSearchCV
Features scaled (if applicable)
Model trained on hotel booking dataset
⚠️ Known Issues
Requires Flask server to be running locally
CORS issues may occur if frontend is separate
Model accuracy depends on dataset quality
🔥 Future Improvements
Show prediction probability (%)
Add data visualization (charts)
Deploy using Render / Heroku / AWS
Improve model with XGBoost
Add user authentication
