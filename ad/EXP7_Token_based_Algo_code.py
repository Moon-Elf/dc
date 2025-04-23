from collections import deque

def token_based_algorithm():
    process_queue = deque()
    num_processes = int(input("Enter the number of processes: "))

    for i in range(1, num_processes + 1):
        process_queue.append(i)

    print("Starting Token Passing...")

    while process_queue:
        process = process_queue.popleft()
        print(f"Process {process} has the token.")
        response = input(f"Does process {process} want to pass the token? (yes/no): ")

        if response.lower() == "yes":
            process_queue.append(process)
        # If response is "no", do nothing (process is removed)

    print("All processes have completed token passing.")

# Run the function
token_based_algorithm()
