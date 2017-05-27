class Stack():
    def __init__(self):
        self.list = []

    def pop(self):
        return self.list.pop()

    def push(self, data):
        self.list.append(data)

    def clear(self):
        self.list.clear()


def enqueue(A, data):
    A.push(data)


def dequeue(A):
    A.pop()

if __name__ == '__main__':
    A = Stack()
    B = Stack()

    N = 10

    print(A.pop())
    print(B.pop())
