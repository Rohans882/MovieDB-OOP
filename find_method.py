def find_by_attribute(items, expected, finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found