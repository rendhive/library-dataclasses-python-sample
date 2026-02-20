from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

    def circumference(self) -> float:
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.circumference())
# Fungsi: Menghitung keliling lingkaran berdasarkan radius.
# Kondisi: Ketika Anda ingin membangun logika metode terkait dengan data class.