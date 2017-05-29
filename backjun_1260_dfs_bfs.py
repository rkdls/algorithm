"""문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.

입력
첫째 줄에 정점의 개수 N(1≤N≤1,000), 간선의 개수 M(1≤M≤10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력  복사
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력  복사
1 2 4 3
1 2 3 4"""


def make_adj_list(matrix):
    m = dict()
    for i, val in enumerate(matrix):
        row, col = val.split()
        row, col = int(row), int(col)
        if row not in m:
            m[row] = []
        m[row].append(col)
    return m


def make_adj_matrix(number):
    m = []
    number = int(number)
    for i in range(number):
        m.append(i)
        m[i] = []
        for j in range(number):
            m[i].append(0)
    return m


def fill_adj_matrix(adj_matrix, param):
    for i, val in enumerate(param):
        row, col = val.split(' ')
        row, col = int(row), int(col)
        adj_matrix[row - 1][col - 1] = 1
        # adj_matrix[col - 1][row - 1] = 1
    return adj_matrix


def depth_first_search(matrix_list, visit, v, N, dfs_result):
    visit[v - 1] = 1
    dfs_result.append(str(v))
    for i in range(N):
        if matrix_list[v - 1][i] == 1 and visit[i] != 1:
            # print(v, "에서 ", i + 1, "로 이동")
            depth_first_search(matrix_list, visit, i + 1, N, dfs_result)


def breadth_first_search(matrix_list, visit, v, N, bfs_result):
    q = [0 for _ in range(N)]
    visit[v - 1] = True
    q.append(v)
    bfs_result.append(str(v))
    while len(q) != 0:
        v = q.pop(0)
        for i in range(N):
            if matrix_list[v - 1][i] == 1 and visit[i] == False:
                visit[i] = True
                # print("{} 에서 {}로 이동".format(v, i + 1))
                bfs_result.append(str(i + 1))
                q.append(i + 1)
                # print(q)
                # print(bfs_result)


if __name__ == '__main__':
    #     data = """4 5 1
    # 1 2
    # 1 3
    # 1 4
    # 2 4
    # 3 4"""
    #     data = input()

    # data = data.splitlines()
    # case = data[0]
    case = input()
    N, M, v = case.split(' ')
    # matrix_list = make_adj_list(data[1:])
    data = []
    N, M, v = int(N), int(M), int(v)
    for i in range(M):
        point = input()
        data.append(point)

    adj_matrix = make_adj_matrix(N)
    filled = fill_adj_matrix(adj_matrix, data)
    visit = [0 for x in range(N)]
    dfs_result = []
    depth_first_search(filled, visit, v, N, dfs_result)
    # print(dfs_result)
    bfs_result = []
    visit = [0 for x in range(N)]
    breadth_first_search(filled, visit, v, N, bfs_result)

    print(" ".join(dfs_result))
    print(" ".join(bfs_result))
