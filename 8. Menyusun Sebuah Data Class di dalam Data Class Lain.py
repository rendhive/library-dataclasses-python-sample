from dataclasses import dataclass
from typing import List

@dataclass
class Department:
    name: str
    employees: List[str]

dept = Department("HR", ["Alice", "Bob"])
print(dept)
# Fungsi: Menyusun satu data class di dalam data class lainnya.
# Kondisi: Ketika Anda ingin membangun struktur data yang lebih terorganisir.