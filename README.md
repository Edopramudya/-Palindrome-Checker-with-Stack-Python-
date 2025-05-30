# 🔁 Palindrome Checker with Stack (Python)
Proyek ini merupakan implementasi program **pengecekan palindrom** menggunakan struktur data **Stack** dalam bahasa Python. Program akan menerima input dari pengguna dan menentukan apakah string tersebut merupakan palindrom atau bukan.

## 🧠 Konsep
Palindrom adalah kata atau kalimat yang dapat dibaca sama baik dari depan maupun belakang. Contoh: `katak`, `radar`, `level`.
Dalam program ini, digunakan **struktur data Stack** untuk membandingkan setengah bagian pertama dan setengah bagian kedua dari string input.

## 📦 Struktur Folder
```
palindrome\_checker/
├── stack\_palindrome.py
└── README.md
```

## 🔍 Cara Kerja Program
1. Input string diubah menjadi huruf kecil (case-insensitive).
2. Setengah pertama string dimasukkan ke dalam stack.
3. Setengah kedua string dibandingkan dengan elemen yang di-pop dari stack.
4. Jika semua karakter cocok, maka string adalah palindrom.

## 🧪 Contoh Output
```
Masukkan Kata: katak
katak adalah palindrom.

Masukkan Kata: python
python bukan palindrom.
````

## 🚀 Cara Menjalankan
1. Clone repository ini.
2. Jalankan file `stack_palindrome.py` menggunakan Python.

## 🛠 Teknologi
* Python 3.x
* Struktur Data Stack (manual, tidak menggunakan library eksternal)

