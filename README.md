🎯 KBC Clone – Kaun Banega Crorepati

A complete implementation of the famous Indian quiz game Kaun Banega Crorepati (KBC) built in two versions:

1. Python Terminal Version
2. Django Web Application Version

This project simulates the real KBC game experience with contestant registration, Fastest Finger First, Hot Seat gameplay, lifelines, prize ladder, timers, sound effects, and winner tracking.

⸻

📌 Project Overview

The objective of this project is to recreate the KBC game flow while demonstrating concepts of:

* Python Programming
* File Handling
* Object-Oriented Programming
* Django Framework
* HTML/CSS/JavaScript
* Database Management
* Session Management
* Web Development

The project was first developed as a terminal-based application and later upgraded into a fully interactive Django web application.

⸻

🚀 Features

Terminal Version

Contestant Registration

* Register multiple contestants
* Store contestant details
* Create individual player files
* Validate user inputs

Fastest Finger First

* Random question selection
* Multiple contestants participate
* Timer-based response tracking
* Fastest correct contestant selected

Hot Seat Round

* 16 Question Format
* Difficulty-based question selection
* Progressive prize ladder
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
* Winner tracking
* Question storage
* Game history

⸻

🌐 Django Web Application Version

The terminal application was later transformed into a modern web-based KBC game using Django.

⸻

Home Page

* Professional KBC-inspired UI
* Amitabh Bachchan themed landing page
* KBC branding
* Start Game button

⸻

Contestant Registration

* Dynamic registration form
* Database storage
* Bootstrap styling
* Player listing

⸻

Fastest Finger First Round

* Random question generation
* Multiple contestant participation
* Individual timer tracking
* Automatic winner selection

⸻

Hot Seat Round

Real KBC Style Interface

* Question panel
* Answer options
* Prize ladder
* Lifelines
* Timer
* Sound effects

Lifelines

50:50

Removes two incorrect options.

Audience Poll

Displays audience voting percentages.

⸻

Timer System

Question 1–5

* 30 seconds

Question 6–14

* 60 seconds

Question 15–16

* Unlimited Time

⸻

Sound Effects

Intro Music

* KBC opening theme

Question Sound

* Plays when a question appears

Correct Answer Sound

* Plays after correct answer

Wrong Answer Sound

* Plays after incorrect answer

Clock Tick Sound

* Countdown timer sound

₹7 Crore Winner Sound

* Grand finale sound effect

⸻

Winner Page

Displays:

* Contestant Name
* Amount Won
* Result
* Correct Answer (if applicable)

⸻

Leaderboard

Stores game history:

* Contestant Name
* Amount Won
* Result
* Date

⸻

🛠 Technologies Used

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

KBC-DJANGO/

├── kbc/

│   ├── models.py

│   ├── views.py

│   ├── forms.py

│   ├── urls.py

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

└── requirements.txt

⸻

⚙ Installation

Clone Repository

git clone https://github.com/Meet15-tech/KBC-CLONE.git
cd KBC-CLONE

⸻

Create Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

⸻

Install Dependencies

pip install -r requirements.txt

⸻

Run Migrations

python manage.py migrate

⸻

Create Admin User

python manage.py createsuperuser

⸻

Run Server

python manage.py runserver

⸻

Open Browser

http://127.0.0.1:8000

⸻

🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* File Handling
* Data Validation
* Randomization
* Django Framework
* MVC/MVT Architecture
* Session Management
* Database Operations
* Frontend Design
* Web Application Development
* Version Control with Git

⸻

🌟 Future Enhancements

* Phone A Friend Lifeline
* Ask The Expert Lifeline
* AI Generated Questions
* User Authentication
* Multiplayer Support
* Cloud Deployment
* Mobile Responsive Design
* Advanced Animations
* Real-Time Leaderboard

⸻
🏆 Final Result

A complete recreation of the Kaun Banega Crorepati game available in both Terminal and Web Application formats, demonstrating practical software development skills from core Python programming to full-stack web development.
