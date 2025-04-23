from collections import deque

class LoadBalancer:
    def __init__(self, server_list):
        self.servers = deque(server_list)

    def get_server(self):
        server = self.servers.popleft()
        self.servers.append(server)
        return server

def main():
    # Load Balancer Simulation
    server_list = ["Server1", "Server2", "Server3","Server4", "Server5"]
    load_balancer = LoadBalancer(server_list)

    # User Input
    requests = int(input("Enter number of requests: "))
    for i in range(requests):
        print(f"Request {i + 1} directed to {load_balancer.get_server()}")

if __name__ == "__main__":
    main()
