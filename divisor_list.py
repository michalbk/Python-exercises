"""
Prints a range of numbers that are divided by integers from 2 to 9.
Usage: main(start, end)
start .. initial number of the range
end .. final number of the range
"""


def main(start, end):
    numbers = range(start, end + 1)
    print_result(start, end, divisibility(numbers))


def divisibility(numbers):
    divisors = range(2, 10)  # divisors from 2 to 9
    result = makedict(divisors)  # dict of results, each value as a list of numbers
    for number in numbers:
        for divisor in divisors:
            if number % divisor == 0:
                result[divisor].append(number)
    return result


def makedict(item):
    dict1 = dict.fromkeys(item)
    for i in dict1:
        dict1[i] = []
    return dict1


def print_result(start, end, dict1):
    maxw = max_length(dict1)  # the longest row in the table
    print('\nSTART POINT: {}'.format(start))
    print('END POINT: {}\n'.format(end))
    print('|{0:^9}|{1:<{width}}|'.format('Divisor', ' Numbers Divided ', width=maxw+2))
    if maxw < 17:
        print('=' * 29)
        for i in dict1:
            print('|{0:^9}| {1:<{width}}|'.format(i, str(dict1.get(i)).strip('[]'), width=16))
    else:
        print('=' * (maxw+14))
        for i in dict1:
            print('|{0:^9}| {1:<{width}}|'.format(i, str(dict1.get(i)).strip('[]'), width=maxw+1))


# returns length of the longest dictionary item (string w/o [])
def max_length(dict1):
    len_list = []
    for i in dict1:
        len_list.append(len(str(dict1.get(i)).strip('[]')))
    return max(len_list)


main(100, 2000)
