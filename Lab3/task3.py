def insertion_Sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

a = [200,12,11,1000,2,1,3,2,0]
insertion_Sort(a)
print("Sorted Array is : ")
print(a)
