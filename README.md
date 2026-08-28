# URL Shortener

A simple URL Shortener built using Python, Flask, MySQL, HTML, CSS, and JavaScript.

The application converts long URLs into short, easy-to-share URLs and redirects users to the original URL when the shortened link is accessed.

## Features

- Enter a long URL.
- Validate URL input.
- Generate a unique 6-character short code.
- Store URLs and short codes in MySQL.
- Display the generated short URL.
- Redirect users to the original URL.
- Prevent duplicate entries for the same URL.
- Handle invalid and empty URL inputs.
- Handle database errors gracefully.

## Technologies Used

- Python
- Flask
- MySQL
- HTML5
- CSS3
- JavaScript
- MySQL Connector/Python

## Project Structure

```text
URL-Shortener/
│
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
How It Works
1. Enter a URL

The user enters a valid long URL through the web interface.

2. Send the URL to Flask

JavaScript sends the URL to the Flask /shorten endpoint using a POST request.

3. Validate the URL

Flask checks whether the URL contains a valid http or https scheme and a network location.

4. Generate a Short Code

A random 6-character code containing letters and numbers is generated.

5. Store the URL

The original URL and generated short code are stored in the MySQL database.

6. Return the Short URL

The application returns a URL such as:

http://127.0.0.1:5000/aB72xQ
7. Redirect

When the short URL is accessed, Flask searches the database for the corresponding short code and redirects the user to the original URL.

Database

The application uses a MySQL database named:

url_shortener

The main table is:

urls

with the following columns:

Column	Description
id	Unique ID
original_url	Original long URL
short_code	Generated short code
created_at	URL creation timestamp
Database Setup

Create the database:

CREATE DATABASE url_shortener;

USE url_shortener;

Create the table:

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Environment Variables

Create a .env file in the project root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener

Do not commit the .env file to GitHub.

Installation

Clone the repository and open the project directory.

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Configure the .env file with your MySQL credentials.

Run the application:

python app.py

Open the application in your browser:

http://127.0.0.1:5000
Example

Long URL:

https://www.example.com/very/long/url

Short URL:

http://127.0.0.1:5000/aB72xQ

Opening the short URL redirects the user to the original URL.

Error Handling

The application handles:

Empty URL input
Invalid URLs
Unknown short codes
Database connection/query errors
Author

Parth Chouhan