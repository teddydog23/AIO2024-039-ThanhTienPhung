def character_frequency(s):
    # Tạo một từ điển để đếm tần suất xuất hiện của các ký tự
    frequency_dict = {}
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        # Nếu ký tự đã có trong từ điển, tăng giá trị đếm lên 1
        if char in frequency_dict:
            frequency_dict[char] += 1
        # Nếu ký tự chưa có trong từ điển, thêm vào với giá trị đếm là 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

# Ví dụ sử dụng
s = "Happiness"
print(character_frequency(s))