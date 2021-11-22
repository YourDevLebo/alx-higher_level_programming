#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    old_list = my_list.copy()
    if 0 <= idx < len(my_list):
        old_list[idx] = element
    return old_list
