'''수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 
있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.'''


class Queue(object):
    def __init__(self):
        self.items = []

    def put(self, N):
        self.items.insert(0, N)

    def get(self):
        return self.items.pop()


q = Queue()


def location(N, K):
    q.put(N)
    visited = [False for i in range(100000)]
    visited[N] = True
    if N > 100000 or K > 100000:
        return
    count = 0
    route = {i: 0 for i in range(10000)}

    while True:
        N = q.get()
        count += 1
        if N == K:
            return route[N], N, K
        if N + 1 < 100000 and visited[N + 1] == False:
            q.put(N + 1)
            visited[N + 1] = True
            route[N + 1] = route[N] + 1
        if N - 1 > 0 and visited[N - 1] == False:
            q.put(N - 1)
            visited[N - 1] = True
            route[N - 1] = route[N] + 1
        if 2 * N < 100000 and visited[2 * N] == False:
            q.put(2 * N)
            visited[2 * N] = True
            route[2 * N] = route[N] + 1


numbers = input()
K, N = numbers.split(' ')
N, _, _ = location(int(K), int(N))
print(N)
