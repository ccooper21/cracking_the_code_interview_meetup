def find_longest_substring(input_string, max_unique_letters_quantity):

    best_left_index = 0
    best_length = 0

    current_left_index = 0
    current_length = 0
    unique_letters_quantity = 0
    letters_quantity_by_letter = [0 for _ in range(26)]

    for i in range(len(input_string)):
        letter_index = ord(input_string[i]) - ord('a')
        while(unique_letters_quantity == max_unique_letters_quantity and not letters_quantity_by_letter[letter_index] > 0):
            expired_letter_index = ord(input_string[current_left_index]) - ord('a')
            letters_quantity_by_letter[expired_letter_index] -= 1
            unique_letters_quantity -= (0, 1)[letters_quantity_by_letter[expired_letter_index] == 0]
            current_left_index += 1
            current_length -= 1

        current_length += 1
        unique_letters_quantity += (0, 1)[letters_quantity_by_letter[letter_index] == 0]
        letters_quantity_by_letter[letter_index] += 1
        if current_length >  best_length:
            best_left_index = current_left_index
            best_length = current_length

    return input_string[best_left_index:best_left_index + best_length]

if __name__ == '__main__':
    print(find_longest_substring('eceba', 2))
    print(find_longest_substring('baece', 2))
