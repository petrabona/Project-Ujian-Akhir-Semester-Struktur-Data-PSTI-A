class MatrixManager:
    def __init__(self):
        self.matrices = [None, None]
    def _get_matrix_input(self):
        while True:
            try:
                rows = []
                print("Masukkan baris matriks (misalnya, '1 2 3'). Ketik 'done' pada baris baru saat selesai:")
                while True:
                    line = input("> ").strip()
                    if line.lower() == 'done':
                        break
                    if not line:
                        continue
                    rows.append(list(map(float, line.split())))
                if not rows:
                    print("Tidak ada baris yang dimasukkan. Silakan coba lagi.")
                    continue
                num_cols = len(rows[0])
                if not all(len(row) == num_cols for row in rows):
                    print("Semua baris harus memiliki jumlah kolom yang sama. Silakan coba lagi.")
                    continue
                return rows
            except ValueError:
                print("Masukan tidak valid. Harap masukkan angka yang dipisahkan spasi.")
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}")
    def set_matrix(self, slot_index):
        if slot_index not in [0, 1]:
            print("Indeks slot tidak valid. Pilih 0 atau 1.")
            return
        print(f"--- Masukan untuk Matriks {slot_index + 1} ---")
        self.matrices[slot_index] = self._get_matrix_input()
        print(f"Matriks {slot_index + 1} berhasil diatur.\n")
    def get_matrix(self, slot_index):
        if slot_index not in [0, 1]:
            print("Indeks slot tidak valid. Pilih 0 atau 1.")
            return None
        return self.matrices[slot_index]
    def display_matrices(self):
        print("\n--- Matriks Tersimpan ---")
        for i, matrix in enumerate(self.matrices):
            print(f"Matriks {i + 1}:")
            if matrix is not None:
                for row in matrix:
                    print(row)
            else:
                print("Slot kosong")
        print("------------------------\n")