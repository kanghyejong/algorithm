import copy
from collections import deque

def bfs(map_array, coordinate, type_num):
    result_map = copy.deepcopy(map_array)
    num1 = coordinate[0]
    num2 = coordinate[1]
    if map_array[num1][num2] == 1:
        if map_array[num1 + 1][num2] == 1:
            bfs(result_map, )
        if map_array[num1 - 1][num2] == 1:

        if map_array[num1][num2 + 1] == 1:

        if map_array[num1][num2 - 1] == 1:
    else:
        type_num = type_num + 1


if __name__ == "__main__":
    num = int(input())
    map_array = list(list(map(int, list(input()))) for _ in range(num))

    print(map_array)
    bfs(map_array, [0, 0], 2)
