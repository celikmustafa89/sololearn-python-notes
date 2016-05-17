
def iteration_over_list():
    """Iteration over list elements.

    :return: None
    """

    print("##### ##### iteration_over_list ##### #####")
    for i in [1, 2, 3, 4]:
        print(i)
    # prints:
    # 1
    # 2
    # 3
    # 4


def iteration_over_string():
    """Iteration over string characters.

    :return: None
    """

    print("##### ##### iteration_over_string ##### #####")
    for i in "python":
        print(i)
    # prints:
    # p
    # y
    # t
    # h
    # o
    # n


def iteration_over_dictionary():
    """Iteration over dictionary elements.

    :return: None
    """

    print("##### ##### iteration_over_dictionary ##### #####")
    for i in {"x": 1, "y": 2, "z": 3}:
        print(i)
    # prints:
    # z
    # y
    # x


def iteration_over_file_line():
    """Iteration over file lines.

    :return: None
    """

    print("##### ##### iteration_over_file_line ##### #####")
    for line in open("a.txt"):
        print(line)
    # prints:
    # first line
    # second line


def iteration_practical_usage():
    """Efficient usage examples of iterations.
    1. list join
    2. dictionary join
    3. string list
    4. dictionary list

    :return: None
    """

    print("##### ##### iteration_practical_usage ##### #####")
    print(",".join(["a", "b", "c"]))
    # prints as string: 'a,b,c'

    print(",".join({"x": 1, "y": 2}))
    # prints as string: 'y,x'

    print(list("python"))
    # prints as list: ['p', 'y', 't', 'h', 'o', 'n']

    list({"x": 1, "y": 2})
    # prints as list: ['y', 'x']
