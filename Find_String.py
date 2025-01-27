def count_substring(string, sub_string):
    count = 0
    n = len(string) - len(sub_string) + 1
    for i in range(n):
        if (sub_string == string[i:len(sub_string)+i]):
            count = count + 1
    return count
