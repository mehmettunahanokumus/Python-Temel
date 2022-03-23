def flatten(f_list):
    flat_list = [] #empty list
    for element in f_list:
        if type(element) is list: #query that asks is element type of list
            for item in element: #iterate the item over the element
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
