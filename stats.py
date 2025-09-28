def num_words(text):
    count_word = 0
    for line in text:
        for word in line.split():
            #print(word)
            count_word += 1
    return count_word

def num_chars(text):
    end_dict = {}
    for line in text:
        for char in line:
            if char.lower() in end_dict:
                end_dict[char.lower()] += 1
            else:
                end_dict[char.lower()] = 1

    return end_dict


def sort_dict(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
