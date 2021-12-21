# 1697
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# input
# 5 17

# output
# 4

from collections import deque

max_pos = 100000
n, k = map(int, input().split())


def bfs(start, finish):
    visited = [False for i in range(max_pos + 1)]
    depth = 0
    queue = deque([[start, depth]])

    while queue:
        # print("q : ", q)
        [pos, depth] = queue.popleft()

        if not visited[pos]:
            visited[pos] = True

            if pos == finish:
                return depth
            depth += 1

            if pos - 1 >= 0 and visited[pos - 1] == False:
                queue.append([pos - 1, depth])
            if pos + 1 <= max_pos and visited[pos + 1] == False:
                queue.append([pos + 1, depth])
            if pos * 2 <= max_pos and visited[pos * 2] == False:
                queue.append([pos * 2, depth])


print(bfs(n, k))

# v
# 1 -1 *2

#   5
# 4 6 10
# ---
#   4       6         10
# 3 5 8   5 7 12    9 11 20
# ---
#   3       5 (die)    8         5 (die)...
# 2 4 6   4 6 10    7 9 16    4 6 10 ...
