from dataclasses import dataclass
from typing import List

@dataclass
class Library:
    name: str
    books: List[str]

library = Library("City Library", ["Book A", "Book B"])
print(library)
# Fungsi: Mengelompokkan informasi tentang pustaka ke dalam data class.
# Kondisi: Ketika Anda ingin mengelompokkan objek yang lebih besar dengan berbagai atribut.