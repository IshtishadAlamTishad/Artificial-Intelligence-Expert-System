a = [[1,2,3],[4,5,6],[7,8,9]]

r=3
c=3
def diag_sum(a) :
    dsum =0
    for i in range(c) :
        dsum = dsum + a[i][i]
    for i in range(c) :
        dsum = dsum + a[i][c-1-i]
    return dsum

print("Diagnal sum is : ",diag_sum(a))