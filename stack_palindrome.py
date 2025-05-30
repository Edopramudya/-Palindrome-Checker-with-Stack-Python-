class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def is_palindrome(input_string):
    input_string = input_string.lower()  # Mengubah semua huruf menjadi huruf kecil
    stack = Stack() #Membuat objek stack dari kelas Stack.

    # Loop untuk memasukkan setengah pertama dari string ke dalam stack. (// agar hasil tidak float)
    for char in input_string[:len(input_string)//2]: 
        stack.push(char)

    # Menentukan indeks awal untuk membandingkan setengah kedua string. 
    # Jika panjang string genap, maka dimulai dari setengah string. Jika panjang string ganjil, maka dimulai dari setengah + 1.
    start = len(input_string)//2 if len(input_string) % 2 == 0 else len(input_string)//2 + 1
     # Loop untuk membandingkan setengah kedua string dengan elemen yang di-pop dari stack.
    for char in input_string[start:]: #start: memasukan nilai dari start sampai akhir
        if char != stack.pop(): #Jika karakter saat ini tidak sama dengan elemen teratas yang di-pop dari stack
            # print(f"{input_string} bukan palindrom.")
            return False
    # print(f"{input_string} adalah palindrom.")
    return True

while True:
    input_string = input("Masukkan Kata: ")

    if is_palindrome(input_string):
        print(f"{input_string} adalah palindrom.")
    else:
        print(f"{input_string} bukan palindrom.")

