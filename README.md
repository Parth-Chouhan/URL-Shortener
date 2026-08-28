# 🔗 URL Shortener

A simple and user-friendly URL Shortener built using **Python, Flask, MySQL, HTML, CSS, and JavaScript**.

The application converts long URLs into short, easy-to-share links. Each generated short code is stored in a MySQL database and can be used to redirect users back to the original URL.

---

## 📌 Project Overview

Long URLs can be difficult to share, remember, and manage. This project provides a simple solution by converting a long URL into a compact short URL.

For example:

```text
Original URL:
https://www.example.com/this-is-a-very-long-url

Short URL:
http://127.0.0.1:5000/aB72xQ

When the generated short URL is accessed, the application looks up the corresponding original URL in the database and redirects the user automatically.

The project was developed as part of the GeeksforGeeks (GFG) project task.

✨ Features
🔗 Convert long URLs into short URLs
🔐 Generate unique 6-character short codes
💾 Store URL mappings in MySQL
🔄 Redirect short URLs to their original destinations
✅ Validate URL format
⚠️ Handle empty URL inputs
⚠️ Handle invalid URL inputs
❌ Handle unknown short codes
♻️ Return the existing short URL when the same URL is submitted again
🛡️ Keep database credentials outside the source code
📱 Responsive and clean user interface
🗄️ Persistent URL storage using MySQL
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming language
Flask	Web framework and API routing
MySQL	Database for storing URL mappings
HTML5	Frontend structure
CSS3	User interface styling
JavaScript	Frontend interaction and API requests
MySQL Connector/Python	Python-MySQL communication
python-dotenv	Loading environment variables
Git & GitHub	Version control and source-code management
🏗️ Project Structure
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
Important Files

app.py

Contains the main Flask application, URL validation, short-code generation, URL shortening logic, and redirect functionality.

database.py

Handles the connection between the Flask application and the MySQL database.

templates/index.html

Contains the structure of the web interface and JavaScript used to communicate with the Flask backend.

static/style.css

Contains the styling and responsive design of the application.

requirements.txt

Contains the Python dependencies required to run the project.

.env.example

Provides an example of the environment variables required for database configuration.

.gitignore

Prevents sensitive files, virtual environments, and unnecessary generated files from being uploaded to GitHub.

🔄 Application Workflow

The application follows the workflow below:

                    USER
                      │
                      ▼
             ┌────────────────┐
             │ Enter Long URL │
             └───────┬────────┘
                     │
                     ▼
             ┌────────────────┐
             │   JavaScript   │
             │ Send POST      │
             │ /shorten       │
             └───────┬────────┘
                     │
                     ▼
             ┌────────────────┐
             │     Flask      │
             │ Backend        │
             └───────┬────────┘
                     │
                     ▼
             ┌────────────────┐
             │ Validate URL   │
             └───────┬────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ URL already exists?  │
          └──────────┬───────────┘
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
             ┌────────────────┐
             │ Flask          │
             │ /<short_code>  │
             └───────┬────────┘
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
🗄️ Database Design

The project uses a MySQL database named:

url_shortener

The database contains a table called:

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
🔐 Environment Configuration

Database credentials are stored using environment variables instead of being hardcoded into the application.

Create a file named:

.env

in the root directory.

Add:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener

Replace your_mysql_password with your local MySQL password.

Important

The .env file should never be uploaded to GitHub because it contains database credentials.

The repository includes .env.example as a safe template:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener
⚙️ Installation
1. Clone the Repository
git clone https://github.com/Parth-Chouhan/URL-Shortener.git

Navigate into the project:

cd URL-Shortener
2. Create a Virtual Environment

On Windows:

python -m venv venv

Activate the virtual environment:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure MySQL

Make sure your local MySQL server is running.

Create the database and table using the SQL commands provided in the Database Design section.

5. Configure Environment Variables

Create a .env file:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener
▶️ Running the Application

Start the Flask application:

python app.py

The application will run locally at:

http://127.0.0.1:5000

Open the URL in a web browser.

🖥️ How to Use
Step 1 — Enter a URL

Enter a valid long URL into the input field.

Example:

https://www.google.com
Step 2 — Click "Shorten URL"

The frontend sends the URL to the Flask backend.

Step 3 — URL Validation

The backend checks whether the URL is valid.

Step 4 — Generate Short Code

A random 6-character code is generated using letters and numbers.

Example:

aB72xQ
Step 5 — Store the Mapping

The application stores the relationship in MySQL:

aB72xQ → https://www.google.com
Step 6 — Display the Short URL

The application displays:

http://127.0.0.1:5000/aB72xQ
Step 7 — Redirect

When the short URL is opened, Flask searches the database for aB72xQ and redirects the user to:

https://www.google.com
🧪 Validation and Error Handling

The application handles several possible invalid scenarios.

Empty URL

If no URL is entered:

URL cannot be empty
Invalid URL

For example:

hello

The application responds with:

Please enter a valid URL
Unknown Short Code

If a short code does not exist:

Short URL not found

with a 404 response.

Database Error

If a database operation fails, the application returns an appropriate error message instead of exposing database details to the user.

♻️ Duplicate URL Handling

If the same original URL is submitted multiple times, the application first checks whether that URL already exists in the database.

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

This prevents unnecessary duplicate URL mappings.

🔑 Short Code Generation

The application generates a 6-character code using:

Uppercase letters
Lowercase letters
Numbers

Example:

aB72xQ
K9mP2z
X7rT21

The Python secrets module is used to randomly select characters.

Before storing a generated code, the application checks the database to make sure the code is not already being used.

Additionally, the MySQL database applies a UNIQUE constraint to the short_code column.

🔒 Security Considerations

The project follows several basic security practices:

Environment Variables

Database credentials are stored in .env rather than directly inside the source code.

Parameterized SQL Queries

Database values are passed using parameterized queries:

cursor.execute(
    "SELECT short_code FROM urls WHERE original_url = %s",
    (original_url,)
)

This helps prevent SQL injection.

Secure Code Generation

The Python secrets module is used instead of a predictable random-number approach for generating short codes.

Git Protection

The .gitignore file prevents sensitive and unnecessary files such as:

.env
venv/
__pycache__/

from being committed to the repository.

📚 Key Concepts Demonstrated

This project demonstrates practical implementation of:

Flask routing
HTTP GET and POST requests
REST-style API communication
JSON request and response handling
HTML forms
JavaScript Fetch API
URL validation
Random short-code generation
MySQL database connectivity
SQL queries
CRUD-related database operations
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

The current project intentionally focuses on the core URL-shortening requirements.

Possible future improvements include:

URL expiration
Click analytics
Custom short URLs
QR code generation
User accounts
URL management dashboard
Copy-to-clipboard functionality
Rate limiting
Deployment with a production database

These features are outside the scope of the current implementation.

📌 Project Requirements

The project satisfies the following requirements:

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

## Author

**Parth Chouhan**

*GeeksforGeeks Recruitment Task — URL Shortener*

<p align="center">
  <img src="https://img.shields.io/badge/-2F8D46?style=for-the-badge&logoColor=white" width="100%" height="8">
</p>
