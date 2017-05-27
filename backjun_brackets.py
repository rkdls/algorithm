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

    def clear(self):
        if self.empty() ==1:
            return
        else:
            self.data.clear()

def checkEmpty(s_val, st):
    if st.empty() == True:
        return False
    else:
        if st.pop() != s_val:
            return False
    return True


if __name__ == '__main__':
    st = Stack()
    ex = '(())()) (((()())() (()())((())) ((()()(()))(((())))() ()()()()(()()())() (()((())()('
    s = ex.split(' ')

    count = int(input())

    for val in range(0,count):
        flag = True
        value = input()
        for i, s_val in enumerate(value):
            # print(s_val)
            if s_val == '(' or s_val == '{' or s_val == '[':
                st.push(s_val)

            # elif s_val == ')':
            #     # if st.empty() == True:
            #     #     flag = False
            #     #     break
            #     # else:
            #     #     if st.pop() != '(':
            #     #         break
            #     if checkEmpty(s_val,st) == False:
            #         break

            elif s_val == ']' or s_val == '}' or s_val == ')':
                if checkEmpty(s_val,st) == False:
                    flag = False
                    break
            # elif s_val == '}':
            #     if checkEmpty(s_val,st) == False:
            #         break
        if st.empty() == False or flag == False:
            print('NO')
        else :
            print("YES")
        st.clear()
