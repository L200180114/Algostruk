def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

a = [10, 51,2, 18, 4, 31, 13, 5, 23, 64, 29]
print(cariLurus(a, 31))
print(cariLurus(a, 8))
