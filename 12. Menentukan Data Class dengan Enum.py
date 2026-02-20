from dataclasses import dataclass
from enum import Enum

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"

@dataclass
class ColoredPoint:
    x: int
    y: int
    color: Color

point = ColoredPoint(1, 2, Color.RED)
print(point)
# Fungsi: Menggunakan enum bersama data class untuk memperjelas tipe data.
# Kondisi: Ketika Anda ingin menggunakan status tetap bersamaan dengan atribut dalam data class.