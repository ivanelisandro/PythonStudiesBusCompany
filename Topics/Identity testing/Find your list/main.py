def find_my_list(lists, my_list):
    for position, lst in enumerate(lists):
        if lst is my_list:
            return position
    return None
