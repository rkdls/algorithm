'''괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어
있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운
문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. '''

'''출력은 표준 출력을 사용한다.
만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면
“YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

예제
6
(())())     NO
(((()())()  NO
(()())((()))    YES
((()()(()))(((())))()   NO
()()()()(()()())()      YES
(()((())()(             NO
'''
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
            if s_val == '(':
                st.push(s_val)
            elif s_val == ')':
                if st.empty() == True:
                    # print('No')
                    flag = False
                    break
                else:
                    st.pop()

        if st.empty() == False or flag == False:
            print('NO')
        else :
            print("YES")
        st.clear()
