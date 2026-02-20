from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str

    def __repr__(self):
        return f"User({self.username})"

user = User("alice", "alice@example.com")
print(user)
# Fungsi: Kustomisasi tampilan representasi objek.
# Kondisi: Ketika Anda ingin menampilkan representasi khusus dari objek.