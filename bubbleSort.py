def bubble_Sort(a):
    n = len(a)

    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp


a = [1200,12,11,1000,2,1,3,2,0]
bubble_Sort(a)
print("Sorted Array is : ")
print(a)
