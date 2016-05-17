#!/usr/bin/python

from assistant.python_list import create_square_list_1
from assistant.python_list import create_square_list_2
from assistant.python_list import list_comprehensions
from assistant.python_list import nested_list_comprehensions
from assistant.python_list import list_delete

from assistant.python_iterators_and_generators import iteration_over_list
from assistant.python_iterators_and_generators import iteration_over_string
from assistant.python_iterators_and_generators import iteration_over_dictionary
from assistant.python_iterators_and_generators import iteration_over_file_line
from assistant.python_iterators_and_generators import iteration_practical_usage


def main():
    """

    :rtype: object
    """

    # assistant > python_list.py outputs
    create_square_list_1()
    create_square_list_2()
    list_comprehensions()
    nested_list_comprehensions()
    list_delete()

    # assistant > python_iterators_and_generators outputs
    iteration_over_list()
    iteration_over_string()
    iteration_over_dictionary()
    iteration_over_file_line()
    iteration_practical_usage()


if __name__ == '__main__':
    main()
