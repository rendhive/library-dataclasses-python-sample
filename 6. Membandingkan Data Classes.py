from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")

print(book1 == book2)  # True karena mereka memiliki nilai yang sama
# Fungsi: Menggunakan perbandingan otomatis untuk data class.
# Kondisi: Ketika Anda perlu membandingkan dua objek berdasarkan nilai.