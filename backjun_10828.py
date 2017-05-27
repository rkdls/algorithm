class Stack():
    data = []
    def push(self, num):
        self.data.append(num)

    def show(self):
        return self.data

    def size(self):
        return len(self.data)

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data.pop()

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() ==1:
            return -1
        return self.data[(len(self.data) - 1)]

if __name__ == '__main__':
    stack = Stack()
    val = int(input())
    res = []
    for a in range(0,val):
        command = str(input())
        command = command.split(' ')
        if len(command) == 2:
            com = command[0]
            val = command[1]
            if com == 'push':
                stack.push(val)
        elif len(command) ==1:
            com = command[0]
            if com =='pop':
                res.append(stack.pop())
            elif com =='size':
                res.append(stack.size())
            elif com == 'empty':
                res.append(stack.empty())
            elif com == 'top':
                res.append(stack.top())
    for i in res:
        print(i)