from dataclasses import dataclass

@dataclass
class Account:
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount if amount > 0 else 0

account = Account()
account.deposit(100)
print(account)
# Fungsi: Mengelola wadah akun dengan deposit aman menggunakan ternary operator.
# Kondisi: Ketika Anda ingin menerapkan logika pada manipulasi nilai.