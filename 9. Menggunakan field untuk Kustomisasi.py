from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)  # List default

product = Product("Laptop", 1200.0)
print(product)
# Fungsi: Menggunakan `field` untuk mengatur nilai default dengan factory.
# Kondisi: Ketika Anda ingin mengatur nilai default untuk koleksi yang dapat diubah.