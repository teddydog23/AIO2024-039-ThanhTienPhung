def word_count(file_path)
    word_freq = {}
    with open(file_path, 'r') as file
        for line in file
            words = line.lower().split()
            for word in words
                if word in word_freq
                    word_freq[word] += 1
                else
                    word_freq[word] = 1
    return word_freq

file_path = 'contentP1_data.txt'
print(word_count(file_path))