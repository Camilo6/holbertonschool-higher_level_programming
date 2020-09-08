#!/usr/bin/python3
def no_c(my_string):
    no_more_c = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            no_more_c += char
    return(no_more_c)
