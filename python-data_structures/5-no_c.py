#!/usr/bin/python3
def no_c(my_string):
    # Remove both 'C' and 'c' characters
    my_new_string = my_string.translate({ord('C'): None, ord('c'): None})
    return my_new_string
