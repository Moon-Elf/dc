def main():
    num_clocks = int(input("Enter the number of clocks: "))
    clocks = []

    print("Enter the time (in seconds) for each clock:")
    for i in range(num_clocks):
        time = int(input(f"Clock {i + 1}: "))
        clocks.append(time)

    avg_time = sum(clocks) // num_clocks
    print(f"Synchronized Clock Time: {avg_time} seconds")

if __name__ == "__main__":
    main()
