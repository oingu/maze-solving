from pyamaze import maze, agent

def DFS(maze):
    start = (maze.rows, maze.cols)  # Điểm bắt đầu là góc dưới cùng bên phải
    goal = (1, 1)  # Điểm đích là góc trên cùng bên trái

    stack = [start]  # Sử dụng stack để duyệt DFS
    visited = set()  # Lưu trữ các ô đã thăm
    path = {}  # Lưu trữ đường đi

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)

        # Nếu đã đến đích
        if current == goal:
            break

        # Lấy danh sách các ô kề có thể đi
        for direction in 'NEWS':
            if maze.maze_map[current][direction]:  # Kiểm tra xem ô có đường đi theo hướng đó không
                if direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'S':
                    neighbor = (current[0] + 1, current[1])

                if neighbor not in visited:
                    stack.append(neighbor)
                    path[neighbor] = current  # Lưu lại cha của ô đó

    # Dựng lại đường đi từ start đến goal
    fwd_path = {}
    cell = goal
    while cell != start:
        fwd_path[path[cell]] = cell
        cell = path[cell]
    return fwd_path

# Tạo mê cung và chạy DFS
m = maze(5, 5)  # Tạo mê cung kích thước 5x5
m.CreateMaze()

# Tìm đường đi bằng DFS
dfs_path = DFS(m)

# Hiển thị kết quả
a = agent(m, footprints=True)  # Tạo agent hiển thị dấu chân
m.tracePath({a: dfs_path})  # Vẽ đường đi DFS
m.run()
