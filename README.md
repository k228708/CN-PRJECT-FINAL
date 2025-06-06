# CN-PRJECT-FINAL
Authentication Server with Flask and SSL
Table of Contents

    - Installation
    - Usage
    - Folder Structure
    - Dependencies
    - License
    
Installation

    To run this project, follow these steps:

    1. Install Python 3
    Make sure you have Python 3 installed. You can download it from the official website: https://www.python.org/downloads/

    2. Install Project Dependencies
    Install all dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

    Navigate to the project directory and create a virtual environment to manage your dependencies.

    python -m venv venv

    Activate the virtual environment:
      venv\Scripts\activate
  
    3. Set Up the Database
    Make sure you have MySQL installed on your machine. You can follow the installation guide from https://dev.mysql.com/doc/refman/8.0/en/installing.html.

    Create a database called `AUTHENTICATION_DB` and add a `users` table with the following structure:

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );

    4. SSL Certificates
    You need to generate SSL certificates to run the server securely. You can use OpenSSL to generate a self-signed certificate (for local development):

    openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365

    This will create `server.key` and `server.crt` files that should be placed in the project directory.

    5. Run the Server
    Start the server by running the following command:

    python server.py

    This will start the server on `127.0.0.1:5000` with SSL encryption.

    6. Run the Client
    Start the Flask client application by running:

    python app.py

    This will start the Flask application on `127.0.0.1:5001` and allow you to interact with the server via a web interface.
    
Dependencies

    This project requires the following Python libraries:

    - Flask: Web framework for handling the frontend.
    - mysql-connector-python: Python connector for MySQL.
    - bcrypt: For securely hashing passwords.
    - SSL: For secure client-server communication.
    - socket: For handling communication between client and server.

