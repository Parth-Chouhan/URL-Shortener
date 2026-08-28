# 🔗 URL Shortener

<p align="center">
  <strong>A simple, fast, and user-friendly URL shortening web application.</strong>
</p>

<p align="center">
  Built with Python, Flask, MySQL, HTML, CSS, and JavaScript.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white">
</p>

---

## 📌 Overview

Long URLs can be difficult to share, remember, and manage.

**URL Shortener** provides a simple solution by converting long URLs into short, easy-to-share links.

### Example

```text
Original URL:
https://www.example.com/this-is-a-very-long-url

Short URL:
http://127.0.0.1:5000/aB72xQ
```

When a user opens the generated short URL, the application retrieves the corresponding original URL from the MySQL database and automatically redirects the user to it.

This project was developed as part of the GeeksforGeeks Recruitment Task.

## ✨ Features
-🔗 Convert long URLs into short URLs
-🔐 Generate unique 6-character short codes
-💾 Store URL mappings using MySQL
-🔄 Redirect short URLs to their original destinations
-✅ Validate URL format
-⚠️ Handle empty URL inputs
-⚠️ Handle invalid URL inputs
-❌ Handle unknown short codes
-♻️ Prevent duplicate entries for the same URL
-🛡️ Keep database credentials outside the source code
-📱 Clean and responsive user interface
-🗄️ Persistent URL storage
🛠️ Tech Stack
-Technology	Purpose
-Python	Backend programming
-Flask	Web framework and routing
-MySQL	Persistent database storage
-HTML5	Frontend structure
-CSS3	UI styling and responsiveness
-JavaScript	Frontend interaction and API communication
-MySQL Connector/Python	Python-MySQL connectivity
-python-dotenv	Environment variable management
-Git & GitHub	Version control and source management
## 🏗️ Project Structure
URL-Shortener/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── .python-version
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

### 📂 File Description
File / Folder	Description
app.py	Main Flask application containing routes, URL validation, short-code generation, shortening logic, and redirects
database.py	Handles the connection between Flask and MySQL
templates/index.html	Contains the webpage structure and frontend JavaScript
static/style.css	Contains the application's styling and responsive design
requirements.txt	Lists the Python packages required by the project
.env.example	Template showing the required environment variables
.gitignore	Prevents sensitive and unnecessary files from being committed

### 🔄 Application Workflow

The application follows a simple request-and-redirect workflow:

                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  Enter Long URL │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   JavaScript    │
                  │ POST /shorten   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      Flask      │
                  │     Backend     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Validate URL  │
                  └────────┬────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │  URL already exists?  │
               └───────────┬────────────┘
                           │
                    ┌──────┴──────┐
                    │             │
                   YES            NO
                    │             │
                    ▼             ▼
             Return existing   Generate
             short code        unique code
                    │             │
                    │             ▼
                    │       Store in MySQL
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                  Return Short URL
                           │
                           ▼
                          USER
                           │
                           │ Opens short URL
                           ▼
                  ┌─────────────────┐
                  │ Flask           │
                  │ /<short_code>   │
                  └────────┬────────┘
                           │
                           ▼
                    Search MySQL
                           │
                           ▼
                     Original URL
                           │
                           ▼
                      redirect()
                           │
                           ▼
                   Original Website
 ### 🗄️ Database Design

The application uses a MySQL database named:

url_shortener

The main table is:

urls
Table Structure
Column	Data Type	Description
id	INT	Unique identifier for each record
original_url	TEXT	Original long URL
short_code	VARCHAR(10)	Generated short URL code
created_at	TIMESTAMP	Time when the URL was created
SQL Schema
CREATE DATABASE url_shortener;

USE url_shortener;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

The UNIQUE constraint on short_code ensures that two database records cannot use the same short code.

### 🔐 Environment Configuration

Database credentials are stored using environment variables instead of being hardcoded into the application.

Create a file named:

.env

in the project root.

Add:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener

Replace your_mysql_password with your local MySQL password.

⚠️ Security Note

The .env file contains sensitive database credentials and must not be uploaded to GitHub.

The project includes .env.example as a safe configuration template.

### ⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Parth-Chouhan/URL-Shortener.git

Navigate into the project directory:

cd URL-Shortener
2️⃣ Create a Virtual Environment

On Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure MySQL

Make sure your local MySQL server is running.

Create the url_shortener database and urls table using the SQL schema provided above.

5️⃣ Configure Environment Variables

Create the .env file in the project root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener
▶️ Running the Application

Start the Flask application:

python app.py

The application will run locally at:

http://127.0.0.1:5000

Open the address in your browser.

🖥️ How to Use
1️⃣ Enter a URL

Enter a valid long URL into the input field.

Example:

https://www.google.com
2️⃣ Shorten the URL

Click the Shorten URL button.

The frontend sends the URL to the Flask backend.

3️⃣ URL Validation

The backend verifies that the URL contains a valid http or https scheme and a valid network location.

4️⃣ Generate Short Code

A random 6-character code is generated using letters and numbers.

Example:

aB72xQ
5️⃣ Store the Mapping

The URL and short code are stored in MySQL:

aB72xQ → https://www.google.com
6️⃣ Receive the Short URL

The application returns:

http://127.0.0.1:5000/aB72xQ
7️⃣ Redirect

When the short URL is opened, Flask searches the database for aB72xQ, retrieves the original URL, and redirects the user to it.

### ♻️ Duplicate URL Handling

Before generating a new short code, the application checks whether the submitted URL already exists in the database.

For example:

First request:

https://www.google.com
        ↓
aB72xQ

Submitting the same URL again:

https://www.google.com
        ↓
Existing record found
        ↓
aB72xQ

This prevents unnecessary duplicate mappings.

🔑 Short Code Generation

Each short URL uses a 6-character code consisting of:

Uppercase letters
Lowercase letters
Numbers

Examples:

aB72xQ
K9mP2z
X7rT21

The Python secrets module is used to randomly select characters.

Before storing a generated code, the application checks whether the code is already present in the database.

The database also enforces uniqueness through the UNIQUE constraint on short_code.

### 🧪 Validation & Error Handling

The application handles several invalid scenarios.

Empty URL
URL cannot be empty
Invalid URL

Input:

hello

Response:

Please enter a valid URL
Unknown Short Code

If a short code does not exist:

Short URL not found

The application returns a 404 response.

Database Errors

If a database operation fails, the application returns a user-friendly error message instead of exposing internal database details.

### 🔒 Security Considerations

The project implements several basic security practices.

Environment Variables

Database credentials are stored in .env instead of being hardcoded into the source code.

Parameterized SQL Queries

Database values are passed using parameterized queries:

cursor.execute(
    "SELECT short_code FROM urls WHERE original_url = %s",
    (original_url,)
)

This helps protect against SQL injection.

Secure Short-Code Generation

The Python secrets module is used to generate short codes rather than relying on predictable random values.

Git Protection

.gitignore prevents sensitive and unnecessary files from being committed:

.env
venv/
.venv/
__pycache__/
*.pyc
.vscode/
## 📚 Key Concepts Demonstrated

This project demonstrates practical implementation of:

Flask routing
HTTP GET and POST requests
JSON request and response handling
HTML forms
JavaScript Fetch API
URL validation
Short-code generation
MySQL database connectivity
SQL database operations
Dynamic Flask routes
HTTP redirects
Error handling
Environment variables
Git and GitHub
Basic web application security
🎯 Learning Outcomes

Through this project, the following concepts were practiced:

Building a web application using Flask.
Connecting a Python application to MySQL.
Designing a simple relational database.
Sending data between frontend JavaScript and a Flask backend.
Creating dynamic URL routes.
Generating and validating unique identifiers.
Implementing URL redirection.
Handling invalid user input.
Managing environment variables securely.
Using Git and GitHub for version control.
🚀 Future Improvements

The current implementation focuses on the core URL-shortening requirements.

Possible future improvements include:

📊 Click analytics
⏳ URL expiration
✏️ Custom short URLs
📱 QR code generation
👤 User accounts
📋 URL management dashboard
📋 Copy-to-clipboard functionality
🛡️ Rate limiting
🌐 Production deployment

These features are outside the scope of the current implementation.

📌 Project Requirements
Requirement	Status
Enter a valid long URL	✅
Generate a unique short URL/code	✅
Redirect to original URL	✅
Handle invalid URL input	✅
Handle empty URL input	✅
Display generated short URL	✅
Store URL mappings	✅
Provide source code	✅
Provide project explanation	✅
GitHub repository	✅

### 👨‍💻 Author

Parth Chouhan

GeeksforGeeks Recruitment Task — URL Shortener

<p align="center"> <img src="https://img.shields.io/badge/-2F8D46?style=for-the-badge&logoColor=white" width="100%" height="8"> </p> ```
