from flask import Flask, render_template, request, jsonify, redirect
from database import get_connection
from urllib.parse import urlparse
import secrets
import string
from mysql.connector import Error

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def is_valid_url(url):
    try:
        parsed_url = urlparse(url)

        return parsed_url.scheme in ("http", "https") and bool(parsed_url.netloc)

    except Exception:
        return False


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    return "".join(secrets.choice(characters) for _ in range(length))


@app.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data["url"].strip()

    if not original_url:
        return jsonify({"error": "URL cannot be empty"}), 400

    if not is_valid_url(original_url):
        return jsonify({"error": "Please enter a valid URL"}), 400

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor(buffered=True)

        # Check if URL already exists
        cursor.execute(
            "SELECT short_code FROM urls WHERE original_url = %s",
            (original_url,)
        )

        existing_url = cursor.fetchone()

        if existing_url:
            short_url = request.host_url + existing_url[0]

            return jsonify({
                "short_url": short_url
            })

        # Generate a unique short code
        while True:

            short_code = generate_short_code()

            cursor.execute(
                "SELECT id FROM urls WHERE short_code = %s",
                (short_code,)
            )

            if cursor.fetchone() is None:
                break

        # Save URL
        cursor.execute(
            """
            INSERT INTO urls (original_url, short_code)
            VALUES (%s, %s)
            """,
            (original_url, short_code)
        )

        connection.commit()

        short_url = request.host_url + short_code

        return jsonify({
            "short_url": short_url
        })

    except Error:
        return jsonify({
            "error": "Database error. Please try again later."
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

@app.route("/<short_code>")
def redirect_to_url(short_code):

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor(dictionary=True, buffered=True)

        cursor.execute(
            "SELECT original_url FROM urls WHERE short_code = %s",
            (short_code,)
        )

        result = cursor.fetchone()

        if result is None:
            return "Short URL not found", 404

        return redirect(result["original_url"])

    except Error:
        return "Database error. Please try again later.", 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)