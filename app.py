
from flask import Flask, render_template, request, redirect, url_for
import socket
import ssl

app = Flask(__name__)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def communicate_with_server(request_type, param1, param2=""):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # SSL context for client
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        conn = context.wrap_socket(client_socket, server_hostname=SERVER_HOST)
        conn.connect((SERVER_HOST, SERVER_PORT))


        # Prepare message based on request type
        if request_type in ["LOGIN", "REGISTER"]:
            message = f"{request_type}|{param1},{param2}"
        else:
            message = f"{request_type}|{param1}"

        conn.send(message.encode())

        response = b''
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            response += chunk

        conn.close()
        return response

    except Exception as e:
        print("Error:", e)
        return b"Server Error"

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = communicate_with_server("LOGIN", username, password)

        if result.decode() == "Login Success":
           
            return redirect(url_for('login_success'))
        elif result.decode() == "Login Failed":
            message = "❌ Login Failed. Try again."
        else:
            message = "⚠️ Server Error."

    return render_template('login.html', message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = communicate_with_server("REGISTER", username, password)

        if result.decode() == "Registration Successful":
            message = "✅ Registration Successful! You can now login."
        elif result.decode() == "Username already exists":
            message = "❌ Username already taken. Try a different one."
        else:
            message = "⚠️ Server Error."

    return render_template('register.html', message=message)

@app.route('/login_success')
def login_success():
    return render_template('login_success.html', server_host=SERVER_HOST)


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    message = ""
    if request.method == 'POST':
        choice = request.form['choice']
        filename = request.form['filename']

        if choice == '1':
            result = communicate_with_server("REQUEST_FILE", filename)

        elif choice == '2':
            result = communicate_with_server("REQUEST_IMAGE", filename)

        else:
            return redirect(url_for('login'))

        
        # Handle result
        if isinstance(result, bytes):
            if result.startswith(b"ERROR"):
                message = "❌ File/Image not found."
            else:
                download_folder = r"C:\Users\HP\Downloads"  # <-- Save downloads here
                filepath = f"{download_folder}/{filename}"
                with open(filepath, 'wb') as f:
                    f.write(result)
                message = f"✅ '{filename}' downloaded successfully!"
        else:
            message = "⚠️ Server Error."

    return render_template('menu.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
