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
    Navigate to the project directory and create a virtual environment to manage your dependencies.

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
  
      



    3. Set Up the Database
    Make sure you have MySQL installed on your machine. You can follow the installation guide from https://dev.mysql.com/doc/refman/8.0/en/installing.html.

    Create a database called `AUTHENTICATION_DB` and add a `users` table with the following structure:

    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );
    ```

    4. SSL Certificates
    You need to generate SSL certificates to run the server securely. You can use OpenSSL to generate a self-signed certificate (for local development):

    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365
    ```

    This will create `server.key` and `server.crt` files that should be placed in the project directory.

    5. Run the Server
    Start the server by running the following command:

    ```bash
    python server.py
    ```

    This will start the server on `127.0.0.1:5000` with SSL encryption.

    6. Run the Client
    Start the Flask client application by running:

    ```bash
    python client.py
    ```

    This will start the Flask application on `127.0.0.1:5001` and allow you to interact with the server via a web interface.
    
Usage

    - **Login**: Use the login page to authenticate users with their credentials.
    - **Register**: Register a new user account by providing a username and password.
    - **File Requests**: After logging in, the user can access the file or image download menu, where they can request files from the server (stored on the server’s local path).
    
Folder Structure

    The project directory structure looks like this:

    /project_root
    ├── server.py           # Server-side code for handling requests
    ├── client.py           # Client-side Flask application
    ├── requirements.txt    # List of required Python packages
    ├── server.crt          # SSL certificate
    ├── server.key          # SSL private key
    ├── /templates
    │   ├── login.html      # Login page template
    │   ├── register.html   # Registration page template
    │   ├── menu.html       # File download menu template
    │   └── login_success.html  # Success page after login
    ├── /static
    │   └── (static files like images, CSS, JavaScript, etc.)
    └── README.md           # This file
    
Dependencies

    This project requires the following Python libraries:

    - Flask: Web framework for handling the frontend.
    - mysql-connector-python: Python connector for MySQL.
    - bcrypt: For securely hashing passwords.
    - SSL: For secure client-server communication.
    - socket: For handling communication between client and server.

    Install all dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

    `requirements.txt` should contain:

    ```txt
    Flask==2.0.2
    mysql-connector-python==8.0.27
    bcrypt==3.2.0
    ```
    
License

    This project is licensed under the MIT License - see the LICENSE file for details.
    
