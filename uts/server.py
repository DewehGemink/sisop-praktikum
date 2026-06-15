import socket
import threading
import os

# ================= CONFIG =================
HOST = "0.0.0.0"
PORT = 5000 
BUFFER_SIZE = 4096

# Menyimpan koneksi client {conn: username}
connected_clients = {}

# ================= UTIL =================
def receive_header(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()

def remove_client(conn):
    if conn in connected_clients:
        username = connected_clients[conn]
        print(f"{username} disconnected")
        del connected_clients[conn]
    conn.close()

# ================= SEND MODE =================
def send_unicast(target_username, message, sender_conn=None):
    for conn, username in connected_clients.items():
        if username == target_username:
            try:
                conn.sendall(message)
            except:
                remove_client(conn)

def send_broadcast(message, sender_conn=None):
    for conn in list(connected_clients.keys()):
        if conn != sender_conn:
            try:
                conn.sendall(message)
            except:
                remove_client(conn)

# ================= CLIENT HANDLER =================
def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    try:
        username = conn.recv(1024).decode().strip()
        connected_clients[conn] = username

        print(f"{username} joined")
        send_broadcast(f"[SYSTEM] {username} joined\n".encode())

        while True:
            header = receive_header(conn)
            if not header:
                break

            # ===== MESSAGE =====
            if header.startswith("MESSAGE"):
                # Format:
                # MESSAGE|mode|target(optional)|content
                parts = header.split("|")

                mode = parts[1]

                if mode == "BROADCAST":
                    content = parts[2]
                    print(f"{username} (broadcast): {content}")
                    send_broadcast(f"{username}: {content}\n".encode(), conn)

                elif mode == "UNICAST":
                    target = parts[2]
                    content = parts[3]
                    print(f"{username} -> {target}: {content}")
                    send_unicast(target, f"{username}: {content}\n".encode(), conn)

            # ===== FILE =====
            elif header.startswith("FILE"):
                # Format:
                # FILE|mode|target(optional)|filename|size
                parts = header.split("|")

                mode = parts[1]

                if mode == "BROADCAST":
                    filename = parts[2]
                    file_size = int(parts[3])
                    target = None
                else:
                    target = parts[2]
                    filename = parts[3]
                    file_size = int(parts[4])

                print(f"{username} sending file {filename} ({file_size} bytes)")

                # Receive file
                data = b""
                remaining = file_size
                while remaining > 0:
                    chunk = conn.recv(min(BUFFER_SIZE, remaining))
                    if not chunk:
                        break
                    data += chunk
                    remaining -= len(chunk)

                # Save file
                os.makedirs("server_files", exist_ok=True)
                filepath = os.path.join("server_files", filename)
                with open(filepath, "wb") as f:
                    f.write(data)

                print(f"Saved: {filepath}")

                # Send file
                header_send = f"FILE|{filename}|{file_size}\n".encode()

                if mode == "BROADCAST":
                    send_broadcast(header_send, conn)
                    for c in connected_clients:
                        if c != conn:
                            try:
                                c.sendall(data)
                            except:
                                remove_client(c)

                elif mode == "UNICAST":
                    for c, user in connected_clients.items():
                        if user == target:
                            try:
                                c.sendall(header_send)
                                c.sendall(data)
                            except:
                                remove_client(c)

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        remove_client(conn)

# ================= SERVER =================
def start_server(multithread=True):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    mode = "MULTI THREAD" if multithread else "SINGLE THREAD"
    print(f"Server running on {HOST}:{PORT} | Mode: {mode}")

    while True:
        conn, addr = server.accept()

        if multithread:
            threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True
            ).start()
        else:
            handle_client(conn, addr)

# ================= MAIN =================
if __name__ == "__main__":
    print("Pilih Mode Server:")
    print("1. Single Thread")
    print("2. Multi Thread")

    choice = input("Masukkan pilihan: ")
    start_server(multithread=(choice == "2"))