# ================================
# KODE SEBELUM REFACTOR (BURUK)
# ================================

class ValidatorManager:
    """
    Class ini melanggar:
    - SRP: menangani banyak validasi sekaligus
    - OCP: jika ada validasi baru harus menambah if/else
    - DIP: bergantung pada logic konkret
    """

    def validate(self, student_name, sks, prerequisite_met):
        if sks > 24:
            print(f"{student_name}: Validasi gagal, SKS melebihi batas.")
            return False
        elif not prerequisite_met:
            print(f"{student_name}: Validasi gagal, prasyarat belum terpenuhi.")
            return False

        print(f"{student_name}: Registrasi berhasil.")
        return True


# --- PROGRAM UTAMA ---
validator = ValidatorManager()

validator.validate(
    student_name="kekeb",
    sks=77,
    prerequisite_met=True
)

validator.validate(
    student_name="bekek",
    sks=7,
    prerequisite_met=False
)
