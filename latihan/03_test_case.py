
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    return max(nilai)


# Test Case 1
print("T1:", hitung_rata_rata([80, 60, 90, 70]))

# Test Case 2
print("T2:", hitung_rata_rata([100, 80]))

# Test Case 3
print("T3:", status(60))

# Test Case 4
print("T4:", status(59))

# Test Case 5
print("T5:", nilai_tertinggi([80, 60, 90, 70]))
