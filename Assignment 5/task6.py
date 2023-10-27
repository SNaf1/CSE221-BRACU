with open('input6.txt', 'r') as input_file:
    R, C = map(int, input_file.readline().split())
    grid = []
    for i in range(R):
        row = input_file.readline().strip()  
        cells = list(row)  
        grid.append(cells)  


def dfs(r, c, visited):
    diamonds = 0
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < R and 0 <= c < C and not visited[r][c] and grid[r][c] != '#':
            visited[r][c] = True
            if grid[r][c] == 'D':
                diamonds += 1
            stack.append((r+1, c))
            stack.append((r-1, c))
            stack.append((r, c+1))
            stack.append((r, c-1))
    return diamonds

max_diamonds = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '.':
            visited = [[False]*C for i in range(R)]
            diamonds = dfs(r, c, visited)
            max_diamonds = max(max_diamonds, diamonds)

with open('output6.txt', 'w') as output_file:
    output_file.write(str(max_diamonds))