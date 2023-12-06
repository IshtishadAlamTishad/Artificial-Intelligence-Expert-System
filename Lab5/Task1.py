def func(P, Q):
    m = len(P)
    n = len(Q)

    max_length = 0
    end = 0

    for i in range(m):
        for j in range(n):
            length = 0
            p,q = i,j
            while p < m and q < n and P[p] == Q[q]:
                length += 1
                p += 1
                q += 1

            if length > max_length:
                max_length = length
                end = i

    cs = P[end:end + max_length]
    return cs


P = "AGTCTTCCAGCGAT"
Q = "GACATCGATAATGC"

x = func(P,Q)
print("Common Sequence:",x)
