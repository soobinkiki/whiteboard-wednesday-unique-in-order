# Whenever your value is not what the last one is,
# update what the last one is,
# and append the new value to our result.
def unique_in_order(iterable):
    result = []
    prev = None
    for element in iterable:
        if element != prev:
            result.append(element)
            prev = element
    return result

# Or just check against the most recently thing added.
def unique_in_order(iterable):
    result = []
    for element in iterable:
        if len(result) == 0 or element != result[-1]:
            result.append(element)
    return result
