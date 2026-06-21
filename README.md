🎯 KBC Clone – Kaun Banega Crorepati

A complete recreation of India’s most popular quiz show Kaun Banega Crorepati (KBC) developed in two versions:

* 🖥️ Python Terminal Application
* 🌐 Django Web Application

The project simulates the complete KBC experience, including contestant registration, Fastest Finger First, Hot Seat gameplay, lifelines, prize ladder progression, timers, sound effects, and winner tracking.

⸻

📌 Project Overview

The goal of this project is to recreate the real KBC game flow while applying concepts of:

* Python Programming
* File Handling
* Object-Oriented Programming
* Django Framework
* HTML, CSS & JavaScript
* Database Management
* Session Handling
* Full Stack Web Development

The project was initially built as a terminal-based application and later transformed into a fully interactive web application using Django.

⸻

🚀 Features

🖥️ Python Terminal Version

Contestant Registration

* Register multiple contestants
* Store contestant information
* Input validation
* Individual player records

Fastest Finger First (FFF)

* Random question generation
* Multiple contestant participation
* Timer-based response tracking
* Automatic winner selection

Hot Seat Round

* 16-question gameplay
* Difficulty-based progression
* Prize ladder system
* Winner determination

Difficulty Levels

* Simple
* Medium
* Hard
* Hardest
* Extreme
* Ultimate

Prize Ladder

Question	Prize
1	₹1,000
2	₹2,000
3	₹3,000
4	₹5,000
5	₹10,000
6	₹20,000
7	₹40,000
8	₹80,000
9	₹1,60,000
10	₹3,20,000
11	₹6,40,000
12	₹12,50,000
13	₹25,00,000
14	₹50,00,000
15	₹1 Crore
16	₹7 Crore

Safe Levels

* ₹10,000
* ₹3,20,000

File Handling

* Contestant storage
* Question storage
* Winner tracking
* Game history records

⸻

🌐 Django Web Application

The terminal version was upgraded into a fully interactive web-based KBC game using Django.

🏠 Home Page

* KBC-inspired user interface
* Game introduction screen
* Start Game functionality

📝 Contestant Registration

* Dynamic registration form
* Database storage
* Bootstrap-powered interface
* Player management

⚡ Fastest Finger First

* Randomized questions
* Multiple participant support
* Timer tracking
* Automatic winner selection

🎮 Hot Seat Round

Real KBC Interface

* Question display panel
* Four answer options
* Prize ladder
* Lifelines
* Timers
* Sound effects

⸻

🎯 Lifelines

50:50

Removes two incorrect options.

Audience Poll

Displays audience voting percentages for all options.

⸻

⏱️ Timer System

Questions 1–5

* 30 Seconds

Questions 6–14

* 60 Seconds

Questions 15–16

* Unlimited Time

⸻

🔊 Sound Effects

* Intro Music
* Question Sound
* Correct Answer Sound
* Wrong Answer Sound
* Timer Tick Sound
* ₹7 Crore Winner Sound

⸻

🏆 Winner Page

Displays:

* Contestant Name
* Amount Won
* Result Status
* Correct Answer (if applicable)

⸻

📊 Leaderboard

Stores complete game history:

* Contestant Name
* Amount Won
* Result
* Date & Time

⸻

🛠️ Technologies Used

Backend

* Python
* Django

Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

Database

* SQLite3

Version Control

* Git
* GitHub

⸻

📂 Project Structure

KBC-CLONE/
├── kbc/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│   └── kbc/
│       ├── base.html
│       ├── home.html
│       ├── register.html
│       ├── fff.html
│       ├── fff_result.html
│       ├── hotseat.html
│       ├── correct_answer.html
│       ├── winner.html
│       └── leaderboard.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── sounds/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

⸻

⚙️ Installation

Clone Repository

git clone https://github.com/Meet15-tech/KBC-CLONE.git
cd KBC-CLONE

Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Mac/Linux

python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Run Database Migrations

python manage.py migrate

Create Admin User

python manage.py createsuperuser

Run Development Server

python manage.py runserver

Open Browser

http://127.0.0.1:8000

⸻

🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* File Handling
* Object-Oriented Programming
* Data Validation
* Randomization Techniques
* Django Framework
* MVT Architecture
* Session Management
* Database Operations
* Frontend Development
* Full Stack Web Development
* Git & GitHub Workflow

⸻

🌟 Future Enhancements

* 📞 Phone A Friend Lifeline
* 👨‍🏫 Ask The Expert Lifeline
* 🤖 AI Generated Questions
* 🔐 User Authentication System
* 👥 Multiplayer Gameplay
* ☁️ Cloud Deployment
* 📱 Mobile Responsive Design
* ✨ Advanced Animations
* 📈 Real-Time Leaderboard

⸻

🏆 Final Result

A complete recreation of Kaun Banega Crorepati (KBC) available in both Terminal and Web Application formats, showcasing practical software development skills ranging from core Python programming to full-stack Django development.

⸻

👨‍💻 Author

Meet Thakkar

Aspiring Full Stack & AI Developer

* Python Development
* Django Development
* Machine Learning
* Artificial Intelligence
* Web Application Development

⭐ If you found this project useful, consider giving it a star on GitHub.
