def count_substring(string, sub_string):
    string_length = len(string)
    sub_string_length = len(sub_string)
    last_index_to_compare = string_length - sub_string_length
    count = 0
    for i in range(last_index_to_compare + 1):
        if string[i:i+sub_string_length] == sub_string:
            count += 1
    return count
