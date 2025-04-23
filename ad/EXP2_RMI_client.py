import socket
import pickle

def call_rpc(function, params):
    request = {'function': function, 'params': params}
    sock.sendall(pickle.dumps(request))  # Serialize and send the request
    
    response = sock.recv(1024)
    result = pickle.loads(response)  # Deserialize the response
    return result

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8080
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    while True:
        function = input("Enter function name (add/subtract): ")
        params = input("Enter parameters as comma separated values (e.g., 3,4): ")
        params = tuple(map(int, params.split(',')))
        
        result = call_rpc(function, params)
        print(f"Response: {result}")
    
    sock.close()    
