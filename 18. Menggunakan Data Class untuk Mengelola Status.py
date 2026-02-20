from dataclasses import dataclass
from enum import Enum

class TaskStatus(Enum):
    NEW = "New"
    IN_PROGRESS = "In Progress"
    COMPLETE = "Complete"

@dataclass
class Task:
    title: str
    status: TaskStatus

task = Task("Finish Report", TaskStatus.IN_PROGRESS)
print(task)
# Fungsi: Menyimpan status tugas dalam proyek.
# Kondisi: Ketika Anda ingin melacak status dengan cara yang terdefinisi dengan baik.