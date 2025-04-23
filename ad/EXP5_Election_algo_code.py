class Pro:
    def __init__(self, pid):
        self.id = pid
        self.act = True

class GFG:
    def __init__(self):
        self.process_ids = [1, 3, 5, 7, 56, 63, 92 ,87]  # <<< YOU CAN EDIT THIS LIST
        self.TotalProcess = len(self.process_ids)
        self.process = [Pro(pid) for pid in self.process_ids]

    def Election(self):
        failed_index = self.FetchMaximum()
        failed_id = self.process[failed_index].id
        print(f"Process no {failed_id} fails")
        self.process[failed_index].act = False

        initialized_pid = 5  # <<< CHANGE the initiator process ID here
        init_index = self.getIndexById(initialized_pid)

        print(f"Election Initiated by Process {initialized_pid}")
        old = init_index
        newer = (old + 1) % self.TotalProcess

        while True:
            if self.process[newer].act:
                print(f"Process {self.process[old].id} passes Election({self.process[old].id}) to {self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == init_index:
                break

        new_coord_index = self.FetchMaximum()
        new_coord_id = self.process[new_coord_index].id
        print(f"\nProcess {new_coord_id} becomes coordinator")

        old = new_coord_index
        newer = (old + 1) % self.TotalProcess
        while True:
            if self.process[newer].act:
                print(f"Process {self.process[old].id} passes Coordinator({new_coord_id}) to Process {self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == new_coord_index:
                print("End Of Election")
                break

    def FetchMaximum(self):
        max_id = -1
        max_index = 0
        for i in range(self.TotalProcess):
            if self.process[i].act and self.process[i].id > max_id:
                max_id = self.process[i].id
                max_index = i
        return max_index

    def getIndexById(self, pid):
        for i, p in enumerate(self.process):
            if p.id == pid:
                return i
        raise ValueError(f"Process ID {pid} not found!")

def main():
    gfg = GFG()
    gfg.Election()

if __name__ == "__main__":
    main()
