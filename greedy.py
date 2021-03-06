"""
문제 : H전자에서 최신 스마트폰 출시를 앞두고 있다. 스마트폰 내의 운영체제 포팅은 끝났고 남은것은 각종 기본 어플리케이션을 포팅하는
 작업이다. 이때, OS가 설치된 공간을 제외하고 메모리 공간을 최대한 사용하여 앱을 탑재하려고 하는데 앱이 구동되는데 걸리는 시간은 
 최소로 하려고 한다. 여러 앱이 설치되어 있을 때, 하나의 앱은 여러번 구동 될 수도 있다.
예를들어 메모리 총량이 11이고, OS크기가 1이면 사용가능한 메모리의 크기는 10이 된다. 여기에 기본 앱을 3개를 포팅한다고 했을 때, 
a앱의 구동시간은 4, 메모리차지는 3이고, b앱의 구동시간은 5, 메모리차지는 4, c앱의 구동시간은 7, 메모리차지는 5라고 하면, 
메모리 10을 최대로 사용해서 구동시간을 최소로 하는 경우는 a앱 2번, b앱을 1번 실행했을 때 메모리사용10, 구동시간 13으로 최소가 된다.
이런 방식으로 사용할 수 있는 메모리 공간에 앱을 최대한으로 설치한 뒤 최소가 되는 구동시간을 구하여라

입력 : 첫째줄에 테스트케이스 횟수 t를 입력한다. 각 테스트케이스의 첫 줄에 OS가 차지하는 메모리크기 e와 전체 메모리 크기 f를 
입력한다.(단, 둘다 10000이하의 자연수) 각 테스트의 둘째 행에는 스마트폰에 탑재할 앱의 개수 n을 입력한다.(n은 10 이하의 자연수) 
각 n행에는 각 앱을 실행시키는데 소요되는 구동시간 p(p는 50000이하의 자연수), 앱이 차지하는 메모리 크기w(w는 10000이하의 자연수)가 
주어진다.

출력 : 각 테스트케이스에 주어진 메모리 크기를 갖는 앱들이 실행될 때 소요되는 최소 시간을 출력한다. 만일 사용하는 앱의 메모리 
크기가 정확히 맞지 않으면 -1을 출력한다.

입출력 예 :
<입력>
3

10 110

2
1 1
30 50
10 110

2
1 1
50 30
1 6

2
10 3
20 4

<출력>
60
100
-1
[출처] [알고리즘 문제풀이 전략] 탐욕 알고리즘 (Greedy) - 문제편|작성자 occidere
"""

if __name__ == '__main__':
    data = '''3
10 110
2
1 1
30 50
10 110
2
1 1
50 30
1 6
2
10 3
20 4'''

    datas = data.splitlines()
    case = [x for x in datas]
    print(case.pop(0))  # 케이스는 그냥 버림.

    while case is not None:
        os_total = case.pop(0)
        os, total = os_total.split()
        n = case.pop(0)
        print(os, total, n)