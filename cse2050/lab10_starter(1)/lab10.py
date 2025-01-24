class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


    def __eq__(self, other):
        if (self.priority == other.priority) and (self.item == other.item):
            return True
        
        else: return False

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        
        else: return False


class PQ_UL(Entry):

    def __init__(self, Entries = []):
        self.Entries = Entries


    def __len__(self):
        return len(self.Entries)
    
    def insert(self, item, priority):
        entry = Entry(item, priority)

        return self.Entries.append(entry)

    def find_min(self):
        index = 0
        for i in range(len(self.Entries)):
            if self.Entries[i] < self.Entries[index]:
                index = i
        return self.Entries[index]

    def remove_min(self):
        min = self.find_min()

        index = 0
        for i in range(len(self.Entries)):
            if self.Entries[i] < self.Entries[index]:
                index = i

        self.Entries.pop(index)
        
        return min
    
class PQ_OL(Entry):

    def __init__(self, Entries = []):
        self.Entries = Entries

    def __len__(self):
        return len(self.Entries)

    def insert(self, item, priority):
        entry = Entry(item, priority)

        return self.Entries.append(entry)
        
    def find_min(self):

        self.Entries.sort()

        return self.Entries[0]
        
    def remove_min(self):
        min = self.find_min()

        self.Entries.pop(0)
        
        return min