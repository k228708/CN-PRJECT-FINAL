

import socket
import ssl
import mysql.connector
import bcrypt
import os

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="AUTHENTICATION_DB"
)
cursor = db.cursor()


# Server configuration
HOST = '127.0.0.1'
PORT = 5000


# SSL configuration
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")  # Your SSL certs

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    conn = context.wrap_socket(conn, server_side=True)
    print(f"Connection from {addr}")

    try:
        data = conn.recv(4096).decode()
        if not data:
            conn.close()
            continue

        request_type, credentials = data.split("|", 1)

############################################ LOGIN ###############################################
        if request_type == "LOGIN":
            username, password = credentials.split(",")

            query = "SELECT password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result and bcrypt.checkpw(password.encode(), result[0].encode()):
                conn.sendall(b"Login Success")
            else:
                conn.sendall(b"Login Failed")



############################################ REGISTER ###############################################

        elif request_type == "REGISTER":
            username, password = credentials.split(",")

            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                conn.sendall(b"Username already exists")
            else:
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, hashed_password))
                db.commit()
                conn.sendall(b"Registration Successful")




############################################ REQUEST.server ###############################################



        elif request_type == "REQUEST_FILE":
            filename = credentials.strip()
            folder_path = r"C:\Users\HP\Desktop"  # <-- Your server's file location
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        conn.sendall(data)
            else:
                conn.sendall(b"ERROR: File not found")

        elif request_type == "REQUEST_IMAGE":
            filename = credentials.strip()
            folder_path = r"C:\Users\HP\Pictures"  # <-- Your server's images location
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    conn.sendfile(f)
            else:
                conn.sendall(b"ERROR: Image not found")

        else:
            conn.sendall(b"Invalid Request")

    except Exception as e:
        print(f"Error: {e}")
        try:
            conn.sendall(b"Server Error")
        except:
            pass
    finally:
        conn.close()
