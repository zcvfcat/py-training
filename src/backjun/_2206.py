from collections import deque

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def Bfs(visited, graph):
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        cur_x, cur_y, iscrash = queue.popleft()
        if cur_x == N - 1 and cur_y == M - 1:
            return visited[cur_x][cur_y][iscrash]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x <= -1 or next_x >= N or next_y <= -1 or next_y >= M:
                continue
            if graph[next_x][next_y] == 0 and visited[next_x][next_y][iscrash] == 0:
                queue.append((next_x, next_y, iscrash))
                visited[next_x][next_y][iscrash] = visited[cur_x][cur_y][iscrash] + 1
            if graph[next_x][next_y] == 1 and iscrash == 0:
                queue.append((next_x, next_y, iscrash + 1))
                visited[next_x][next_y][iscrash +
                                        1] = visited[cur_x][cur_y][iscrash] + 1

    return -1


print(Bfs(visited, map))
