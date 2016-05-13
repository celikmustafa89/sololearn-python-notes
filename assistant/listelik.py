
def create_square_list_1():
    """Creates a list of squares using "for" and "range".

    prints: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    :return: None
    """

    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)


def create_square_list_2():
    """Creates a list of squares using one line code "for" and "range".

    prints: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    :return: None
    """

    squares = [x**2 for x in range(10)]
    print(squares)


def list_comprehensions():
    """Different kind of short list examples.

    :return:
    """

    vec = [-4, -2, 0, 2, 4]

    # create a new list with the values doubled
    doubled_list = [x*2 for x in vec]
    print(doubled_list)
    # prints: [-8, -4, 0, 4, 8]

    # filter the list to exclude negative numbers
    negative_list = [x for x in vec if x >= 0]
    print(negative_list)
    # prints: [0, 2, 4]

    # apply a function to all the elements
    function_usage = [abs(x) for x in vec]
    print(function_usage)
    # prints: [4, 2, 0, 2, 4]

    # call a method on each element
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    method_usage = [weapon.strip() for weapon in fresh_fruit]
    print(method_usage)
    # prints: ['banana', 'loganberry', 'passion fruit']

    # create a list of 2-tuples like (number, square)
    tuples_usage = [(x, x**2) for x in range(6)]
    print(tuples_usage)
    # prints: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # flatten a list using a listcomp with two 'for'
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    nested_list = [num for elem in vec for num in elem]
    print(nested_list)
    # prints: [1, 2, 3, 4, 5, 6, 7, 8, 9]


def nested_list_comprehensions():
    """Different kind of short list examples.

    :return:
    """

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Transpose-1
    # The following list comprehension will transpose rows and columns:
    transposed = [[row[i] for row in matrix] for i in range(4)]
    print(transposed)
    # prints: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # Transpose-2
    # As we saw in the previous example, the nested listcomp is evaluated in
    # the context of the for that follows it, so this example is equivalent to:
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)
    # prints: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # Transpose-3
    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)
    # prints: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # Transpose-4 (RECOMMENDED)
    # Built-in functions
    transposed = zip(*matrix)
    print(transposed)
    # prints: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


def list_delete():
    """Deletes the elements of list.

    :return: None
    """

    # deletes a specific index of element
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    # prints: [1, 66.25, 333, 333, 1234.5]

    # deletes a slice of the list
    del a[2:4]
    print(a)
    # prints: [1, 66.25, 1234.5]

    # deletes all elements of list
    del a[:]
    print(a)
    # prints: []

    # deletes the entire list variable
    del a


