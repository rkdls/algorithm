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
        adj_matrix[col - 1][row - 1] = 1
    return adj_matrix


def depth_first_search_stack(matrix_list, v, N, visitied, dfs_result):
    dfs_result.append(v)
    visitied[v - 1] = True
    for i in range(N):
        if matrix_list[v - 1][i] == 1 and visitied[i] == False:
            print("{} 에서 {} 로 이동".format(v, i + 1))
            depth_first_search_stack(matrix_list, i + 1, N, visitied, dfs_result)
    print(dfs_result)


def breadth_first_search(matrix_list, visited, v, N, bfs_result):
    for i, val in enumerate(matrix_list):
        print(val)
    visited[v-1] = True
    bfs_result.append(v)

    while True:
        for i in range(N):
            if visited[i] is not True and matrix_list[v - 1][i] == 1:
                visited[i] = True
                print("{} 에서 {}로 이동".format(v,i+1))
                bfs_result.append(i+1)
        if v >= N:
            break
        v = v + 1
    print(visited)
    print(bfs_result)


if __name__ == '__main__':
    data = """7 5 1
1 2
1 3
1 4
2 4
3 4
3 5"""
    data = data.splitlines()
    case = data[0]
    matrix_list = make_adj_list(data[1:])
    N, M, v = case.split(' ')
    N, M, v = int(N), int(M), int(v)

    adj_matrix = make_adj_matrix(N)
    filled = fill_adj_matrix(adj_matrix, data[1:])
    dfs_result = []

    # visited = [False for _ in range(N)]
    # depth_first_search_stack(filled, v, N, visited, dfs_result)
    # print(dfs_result)
    bfs_result = []
    visited = [False for x in range(N + 1)]
    breadth_first_search(filled, visited, v, N, dfs_result)
