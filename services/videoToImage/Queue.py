class Queue:
    list = []
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.insert(0,item)
    def pop(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0
    def length(self):
        return len(self.list)