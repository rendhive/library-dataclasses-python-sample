from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point = Point(10, 20)
print(point)
# Fungsi: Membuat kelas Point dengan atribut x dan y.
# Kondisi: Ketika Anda ingin mendefinisikan struktur data untuk menyimpan data dengan jelas.