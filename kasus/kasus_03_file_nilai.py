
try:
    with open("nilai.txt", "r") as file:
        nilai = file.read()
        print("Isi file:", nilai)

except FileNotFoundError:
    print("Error: File nilai.txt tidak ditemukan.")
