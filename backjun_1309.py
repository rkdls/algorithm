"""
이 동물원에는 사자들이 살고 있는데 사자들을 우리에 가둘 때, 가로로도 세로로도 붙어 있게 배치할 수는 없다. 이 동물원 조련사는 사자들의 
배치 문제 때문에 골머리를 앓고 있다.

동물원 조련사의 머리가 아프지 않도록 우리가 2*N 배열에 사자를 배치하는 경우의 수가 몇 가지인지를 알아내는 프로그램을 작성해 주도록 하자. 
사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다고 가정한다.

입력
첫째 줄에 우리의 크기 N(1≤N≤100,000)이 주어진다.

출력
첫째 줄에 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력하여라.

예제 입력  
4

예제 출력  
41
"""

if __name__ == '__main__':
    case = int(input())
    each_floor = dict()
    each_floor[0] = dict()
    each_floor[0][0], each_floor[0][1], each_floor[0][2] = 1, 1, 1

    each_floor_sum = dict()
    each_floor_sum[1] = sum(each_floor[0].values())
    for i in range(1, case + 1):
        each_floor[i] = dict()
        each_floor[i][0] = (each_floor[i - 1][0] + each_floor[i - 1][1] + each_floor[i - 1][2]) % 9901
        each_floor[i][1] = (each_floor[i - 1][0] + each_floor[i - 1][2]) % 9901
        each_floor[i][2] = (each_floor[i - 1][0] + each_floor[i - 1][1]) % 9901
        # data1 = each_floor_sum[i - 1]
        # data2 = sum(each_floor[i].values())
        # each_floor_sum[i] = data1 + data2
        # print(each_floor_sum, each_floor[i])
    print(each_floor[case][0])
