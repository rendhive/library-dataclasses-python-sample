from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

point = ImmutablePoint(1, 2)
print(point)

# point.x = 10  # Ini akan menyebabkan TypeError
# Fungsi: Menetapkan kelas data immutable menggunakan `frozen`.
# Kondisi: Ketika Anda ingin melindungi kelas dari perubahan setelah instansiasi.