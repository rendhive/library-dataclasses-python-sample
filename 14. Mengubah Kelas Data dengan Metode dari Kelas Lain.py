from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())
# Fungsi: Menghitung luas dari objek yang terdefinisi dalam data class.
# Kondisi: Ketika Anda ingin menghitung data berdasarkan atribut dari data class.