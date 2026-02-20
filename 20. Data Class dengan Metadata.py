from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    id: int
    grades: List[int] = field(default_factory=list)

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("Alice", 1, [80, 90, 85])
print(f"Average grade: {student.average_grade()}")
# Fungsi: Mengelola data siswa dan menghitung rata-rata nilai.
# Kondisi: Ketika Anda ingin menjaga informasi siswa dan menghitungnya secara bersamaan.