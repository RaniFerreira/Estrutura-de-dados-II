def intercalar_in_loco(a, x, y, z):
    m = x
    n = y + 1
    while m <= y and n <= z:
        if a[m] <= a[n]:
            m += 1
        else:
            t = a[n]
            p = n
            while p > m:
                a[p] = a[p - 1]
                p -= 1
            a[m] = t
            m += 1
            y += 1
            n += 1

b = [2, 5, 8, 1, 3, 6]
intercalar_in_loco(b, 0, 2, 5)
print("Vetor intercalado:", b)
