def mergesort(x):
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] <= right[j] :
                x[k] = left[i]
                i+=1

            else :
                x[k] = right[j]
                j+=1
            k+=1
        while i < len(left) :
            x[k] = left[i]
            i+=1
            k+=1
        while j<len(right) :
            x[k] = right[j]
            j+=1
            k+=1

def quickSort(x):
    item = len(x)
    if item < 2:
        return x

    curr_pos = 0

    for i in range(1, item):
        if x[i] <= x[0]:
            curr_pos += 1
            pivot = x[i]
            x[i] = x[curr_pos]
            x[curr_pos] = pivot
    pivot = x[0]
    x[0] = x[curr_pos]
    x[curr_pos] = pivot

    left = quickSort(x[0:curr_pos])
    right = quickSort(x[curr_pos + 1:item])

    x = left + [x[curr_pos]] + right
    return x

def binarySearch(a,k) :
    l=0
    r=len(a)
    ans = -1
    while l < r :
        mid = (l+r) // 2
        if (int(a[mid]) == int(k)) :
            ans = mid
            break
        elif (int(a[mid]) < int(k)) :
            l = mid+1
        else :
            r = mid-1
    return ans

def linearSearch(a,k) :
    l = len(a)
    ans=-1
    for i in range(l) :
        if (a[i] == k) :
            ans = i
    return ans

def combineSortSearch(a,k) :

    print("What sort you like to do ?")
    print("a) Linear Search")
    print("b) Binary Search")

    s = input("Please enter option : ")

    if s == "a" :
        mergesort(a)
        o = linearSearch(a,k)
        if o != -1:
            print(k, " Element found at index : ",o)
        else :
            print("Not Found")
    else :
        print("which sort you want?")
        print("a) Merge Sort")
        print("b) Quick Sort")

        t = input("Enter your option : ")

        if t == "a" :
            mergesort(a)
            print(a)
        else :
            x = quickSort(a)
            print(x)

        ans = binarySearch(a,k)

        if ans != -1:
            print(k, " Element found at index : ",ans)
        else :
            print("Not Found")


x = [123,21,1,2,3,44,5,3,0]
k = input("Enter number you want to search : ")
combineSortSearch(x,k)