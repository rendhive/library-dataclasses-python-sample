from dataclasses import dataclass

@dataclass
class Order:
    item: str
    quantity: int
    total_price: float = 0.0

    def __post_init__(self):
        self.total_price = self.quantity * 10.0  # Anggap harga setiap item adalah 10.0

order = Order("T-shirt", 3)
print(order)
# Fungsi: Menangani logika setelah inisialisasi data class.
# Kondisi: Ketika Anda ingin menghitung nilai berdasarkan atribut saat inisialisasi.