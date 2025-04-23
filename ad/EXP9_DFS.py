class DistributedFileSystem:
    def __init__(self):
        self.file_storage = {}

    def add_file(self, file_name, content):
        self.file_storage[file_name] = content

    def get_file(self, file_name):
        return self.file_storage.get(file_name, "File not found")


if __name__ == "__main__":
    # Distributed File System Simulation
    dfs = DistributedFileSystem()
    dfs.add_file("file1.txt", "This is file 1 content")
    dfs.add_file("file2.txt", "This is file 2 content")

    file_name = input("Enter filename to retrieve: ")
    print(f"Content: {dfs.get_file(file_name)}")
