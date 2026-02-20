from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

circle = Circle(5.0)
print(circle)
# Fungsi: Mendefinisikan kelas Circle dengan atribut radius dan otomatisasinya.
# Kondisi: Ketika Anda butuh kelas sederhana tanpa perlu menulis constructor.