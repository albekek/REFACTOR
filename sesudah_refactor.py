# ================================
# KODE SESUDAH REFACTOR (SOLID)
# ================================

from abc import ABC, abstractmethod
from dataclasses import dataclass

# --- MODEL ---
@dataclass
class Student:
    name: str
    sks: int


# --- ABSTRAKSI (DIP & OCP) ---
class IValidationRule(ABC):
    @abstractmethod
    def validate(self, student: Student) -> bool:
        pass


# --- IMPLEMENTASI KONKRIT (SRP) ---
class SksValidation(IValidationRule):
    def validate(self, student: Student) -> bool:
        if student.sks > 24:
            print(f"{student.name}: Validasi SKS gagal.")
            return False
        return True


class PrerequisiteValidation(IValidationRule):
    def __init__(self, prerequisite_met: bool):
        self.prerequisite_met = prerequisite_met

    def validate(self, student: Student) -> bool:
        if not self.prerequisite_met:
            print(f"{student.name}: Validasi prasyarat gagal.")
            return False
        return True


# --- SERVICE COORDINATOR (SRP & DIP) ---
class RegistrationService:
    """
    Bertanggung jawab mengoordinasi proses registrasi,
    tidak mengetahui detail validasi.
    """
    def __init__(self, validations: list[IValidationRule]):
        self.validations = validations

    def register(self, student: Student) -> bool:
        for rule in self.validations:
            if not rule.validate(student):
                print("Registrasi ditolak.\n")
                return False

        print("Registrasi diterima.\n")
        return True


# --- PEMBUKTIAN OCP (CHALLENGE) ---
class IpkValidation(IValidationRule):
    def __init__(self, ipk: float):
        self.ipk = ipk

    def validate(self, student: Student) -> bool:
        if self.ipk < 2.75:
            print(f"{student.name}: Validasi IPK gagal.")
            return False
        return True


# --- PROGRAM UTAMA ---
student1 = Student("mul", 22)

validations1 = [
    SksValidation(),
    PrerequisiteValidation(prerequisite_met=True)
]

registration1 = RegistrationService(validations1)
registration1.register(student1)


student2 = Student("yono", 20)

validations2 = [
    SksValidation(),
    PrerequisiteValidation(prerequisite_met=True),
    IpkValidation(ipk=3.1)  # Validasi BARU tanpa ubah service
]

registration2 = RegistrationService(validations2)
registration2.register(student2)
