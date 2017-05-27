'''예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.
input = 27
output =
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
'''

def root(val, i=0):

    if val == 1:
        return i

    else:
        val = val/3
        i+=1
        return root(val, i)

def squre(val,i = 0):

    for i in range(0, i-1):
        val = 3*val
    return val

if __name__ == '__main__':
    input_val = 81
    # print(root(input_val))
    line = []
    cols =[]
    area = [cols]
    for row in range(0,input_val):
        line = '*' * input_val
        cols.append(line)
        area.append(cols)

    for i, row in enumerate(area):
        for j, col in enumerate(row):
            if j == 2:
                area[i][j]=2

    for i, row in enumerate(area):
        for j, col in enumerate(row):
            print(col, end='')
        print()