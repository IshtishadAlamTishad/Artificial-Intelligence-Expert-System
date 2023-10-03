def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

a = [200,12,11,1000,2,1,3,2,0]
selection_sort(a)
print("Sorted Array is : ")
print(a)