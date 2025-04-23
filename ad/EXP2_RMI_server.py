import socket
import pickle

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def handle_request(request):
    func_name = request['function']
    params = request['params']
    
    if func_name == 'add':
        return add(*params)
    elif func_name == 'subtract':
        return subtract(*params)
    else:
        return f"Function {func_name} not found"

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    totalclients = 1
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclients)
    print("Waiting for clients to connect...")
    
    conn, addr = sock.accept()
    print(f"Connected with client at {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        
        request = pickle.loads(data)  # Deserialize the data
        print(f"Received RPC request: {request}")
        
        response = handle_request(request)
        conn.send(pickle.dumps(response))  # Serialize the response

    conn.close()
    sock.close()
