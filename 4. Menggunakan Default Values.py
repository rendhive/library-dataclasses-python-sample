from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float = 10.0  # Default value

rect = Rectangle(5.0)
print(rect)
# Fungsi: Kelas Rectangle dengan width dan nilai tinggi default.
# Kondisi: Ketika Anda ingin memberikan nilai default untuk anggota kelas.