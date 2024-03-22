#!/usr/bin/python3
def search_replace(my_list, search, replace):
    changed = []
    for i in my_list:
        if i == search:
            changed.append(replace)
        else:
            changed.append(i)

    return changed
