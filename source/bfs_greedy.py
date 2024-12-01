import heapq
import math


# Tính khoảng cách Euler giữa hai điểm (x1, y1) và (x2, y2)
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Hàm thực hiện Greedy Best-First Search
def greedy_bfs(start, goal, matrix):
    rows, cols = len(matrix), len(matrix[0])
    open_list = []
    heapq.heappush(open_list, (euclidean_distance(start, goal), start))  # Heuristic + current position
    closed_list = set()
    came_from = {}  # Lưu lại con đường đi

    # Hướng di chuyển: lên, xuống, trái, phải
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        _, current = heapq.heappop(open_list)

        # Nếu đã đến đích
        if current == goal:
            # Dựng lại đường đi từ điểm đích về điểm bắt đầu
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()  # Đảo ngược lại để có đường đi từ start đến goal
            return path

        closed_list.add(current)

        # Kiểm tra các ô xung quanh
        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])

            # Kiểm tra nếu vị trí là hợp lệ
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if matrix[neighbor[0]][neighbor[1]] == 0 and neighbor not in closed_list:  # 0 là ô trống
                    heapq.heappush(open_list, (euclidean_distance(neighbor, goal), neighbor))
                    came_from[neighbor] = current  # Lưu lại bước đi từ neighbor về current

    return None


# Tạo ma trận ngẫu nhiên với tường và đường đi
def generate_maze(rows, cols):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]  # 0: ô trống, 1: ô tường

    # Thêm tường vào ma trận ngẫu nhiên (ví dụ)
    maze[2][2] = 1
    maze[3][2] = 1
    maze[4][2] = 1
    maze[5][2] = 1
    maze[6][2] = 1
    maze[7][2] = 1
    maze[2][3] = 1
    maze[4][3] = 1
    maze[6][3] = 1
    maze[2][4] = 1
    maze[4][4] = 1
    maze[5][4] = 1

    return maze


# Hiển thị ma trận
def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


def main():
    # Tạo ma trận 10x10
    rows, cols = 10, 10
    maze_matrix = generate_maze(rows, cols)

    # Hiển thị ma trận
    print("Maze:")
    print_maze(maze_matrix)

    start = (0, 0)  # Vị trí bắt đầu
    goal = (9, 9)  # Vị trí đích

    path = greedy_bfs(start, goal, maze_matrix)

    if path:
        print("Đường đi tới đích:")
        print(path)
    else:
        print("Không thể tìm đường tới đích!")


if __name__ == "__main__":
    main()
