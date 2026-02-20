from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    is_active: bool = True

new_user = User("john_doe", "john@example.com")
print(new_user)
# Fungsi: Mengelola atribut pengguna dengan data class.
# Kondisi: Ketika Anda memerlukan struktur untuk menyimpan data pengguna secara terorganisir.