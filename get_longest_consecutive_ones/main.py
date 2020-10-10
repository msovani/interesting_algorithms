# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
# For example, given 156, you should return 3.

def get_longest_consecutive(n):
    total_ones = 0
    max_ones = 0
    this_one = 0
    num_in_binary = list()
    for i in range(64)[::-1]:
        char_value = 1 & int(n) >> i
        num_in_binary.append(char_value)
        last_one_is_one = False
        if char_value == 1:
            last_one_is_one = True
            total_ones = total_ones + 1
        if last_one_is_one:
            this_one = this_one + 1
        else:
            this_one = 0
        if this_one >= max_ones:
            max_ones = this_one
    return max_ones


if __name__ == '__main__':
    print(str(get_longest_consecutive(156)))