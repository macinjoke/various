
# input debug
# for query, x, y in lines:
#     print(query, x, y)

if __name__ == '__main__':
    n, q = map(int, input().split())
    lines = [map(int, input().split()) for _ in range(q)]

    groups = []
    for i in range(n):
        groups.append(i)

    for query, x, y in lines:
        if query == 0:


