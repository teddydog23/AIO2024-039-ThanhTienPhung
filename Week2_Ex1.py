def sliding_window_max(num_list, k):
    if not num_list or k == 0:
        return []
    
    n = len(num_list)
    if k > n:
        return []
    
    max_values = []
    for i in range(n - k + 1):
        window = num_list[i:i + k]
        max_values.append(max(window))
    
    return max_values

# Ví dụ sử dụng
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window_max(num_list, k))