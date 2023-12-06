def quickSort(x):
    item = len(x)
    if item < 2:
        return x

    curr_pos = 0

    for i in range(1, item):
        if x[i] <= x[0]:
            curr_pos += 1
            tmp = x[i]
            x[i] = x[curr_pos]
            x[curr_pos] = tmp
    tmp = x[0]
    x[0] = x[curr_pos]
    x[curr_pos] = tmp
    left = quickSort(x[0:curr_pos])
    right = quickSort(x[curr_pos + 1:item])
    x = left + [x[curr_pos]] + right
    return x


a = [123,21,1,2,3,44,5,3,0]

print("Original array: ", a)
print("Sorted array: ", quickSort(a))