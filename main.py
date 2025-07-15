import socket

from app.service import Service

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        print(f"Servidor ouvindo em {HOST}:{PORT}")
        conn, addr = s.accept()

        with conn:
            print(f"Conectado por {addr}")
            while True:
                data = conn.recv(1024).decode("utf-8")

                if not data:
                    break

                decoded_data = data
                try:
                    response = Service(decoded_data).execute()
                    conn.sendall(response.encode("utf-8"))
                except Exception as e:
                    error_msg = f"Erro no processamento: {e}"
                    conn.sendall(error_msg.encode("utf-8"))
