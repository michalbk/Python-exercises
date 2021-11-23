"""
Prints a vertical histogram from a list of numbers to the console.
Usage: vert_histogram(list_of_numbers)
"""
list1 = [3, 7, 12, 8, 2, 20]


def vert_histogram(lst):
    matrix = create_matrix(lst)
    print_matrix(matrix)


def generate_row(lst, y):
    row = []
    for x in lst:
        if x-y >= 0:
            row.append('**')
        else:
            row.append('  ')
    return row


def create_matrix(lst):
    columns = []
    for y in range(0, max(lst)+1):
        columns.append(generate_row(lst, y))
    return columns


def print_matrix(twodimarray):
    for y in range(len(twodimarray)-1, 0, -1):
        row = '  '.join(twodimarray[y])
        print('{0:>4} | {1}'.format(y, row))


vert_histogram(list1)
