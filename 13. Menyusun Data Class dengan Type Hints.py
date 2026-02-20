from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

people = [Person("Ali", 30), Person("Budi", 25)]
# Fungsi: Menceritakan kumpulan orang menggunakan data class.
# Kondisi: Ketika Anda ingin menyimpan dan memanipulasi banyak entitas dengan tipe data terdefinisi.