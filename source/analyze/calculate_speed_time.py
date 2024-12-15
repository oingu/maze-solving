import time
import pandas as pd
import matplotlib.pyplot as plt

# Giả sử bạn có một danh sách các ma trận và các điểm start, goal
matrices = [matrix1, matrix2, matrix3]
start_goals = [(start1, goal1), (start2, goal2), (start3, goal3)]
algorithms = ['BFS', 'A*', 'Greedy']

# Lưu kết quả vào DataFrame
results = []

# Hàm để chạy và đo thời gian của mỗi thuật toán
def run_algorithm(algorithm, matrix, start, goal):
    start_time = time.time()
    # Chạy thuật toán ở đây, ví dụ BFS, A*, Greedy
    # path = algorithm(matrix, start, goal)  # Đặt thuật toán ở đây
    end_time = time.time()
    return end_time - start_time  # Thời gian thực thi

# Chạy trên tất cả các trường hợp
for matrix, (start, goal) in zip(matrices, start_goals):
    for algorithm in algorithms:
        execution_time = run_algorithm(algorithm, matrix, start, goal)
        results.append({
            'Thuật toán': algorithm,
            'Thời gian (giây)': execution_time,
            'Ma trận': matrix,
            'Start': start,
            'Goal': goal
        })

# Tạo DataFrame từ kết quả
df = pd.DataFrame(results)

# Hiển thị bảng kết quả
print(df)

# Vẽ biểu đồ so sánh
plt.figure(figsize=(10, 6))
plt.bar(df['Thuật toán'], df['Thời gian (giây)'])
plt.xlabel('Thuật toán')
plt.ylabel('Thời gian (giây)')
plt.title('So sánh thời gian thực thi của các thuật toán')
plt.show()
