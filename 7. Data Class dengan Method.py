from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float

    def give_raise(self, amount: float) -> None:
        self.salary += amount

emp = Employee("Bob", 50000)
emp.give_raise(5000)
print(emp)
# Fungsi: Menambahkan metode untuk mengubah data dalam data class.
# Kondisi: Ketika Anda ingin mengelola perilaku di dalam kelas data.