from .petra058 import add_matrices, invert_matrix, create_identity_matrix, multiply_matrices
from .petra058_manager import MatrixManager
def main():
    manager = MatrixManager()
    while True:
        print("\n--- Menu Operasi Matriks ---")
        print("1. Atur Matriks 1")
        print("2. Atur Matriks 2")
        print("3. Lihat Matriks Tersimpan")
        print("4. Tambah Matriks (Matriks 1 + Matriks 2)")
        print("5. Invers Matriks 1")
        print("6. Invers Matriks 2")
        print("7. Buat Matriks Identitas")
        print("8. Kalikan Matriks (Matriks 1 * Matriks 2)")
        print("0. Keluar")
        choice = input("Masukkan pilihan Anda: ").strip()
        if choice == '1':
            manager.set_matrix(0)
        elif choice == '2':
            manager.set_matrix(1)
        elif choice == '3':
            manager.display_matrices()
        elif choice == '4':
            m1 = manager.get_matrix(0)
            m2 = manager.get_matrix(1)
            if m1 is not None and m2 is not None:
                try:
                    result = add_matrices(m1, m2)
                    print("\n--- Hasil Penjumlahan (Matriks 1 + Matriks 2) ---")
                    for row in result:
                        print(row)
                    print("--------------------------------------------------\n")
                except ValueError as e:
                    print(f"Kesalahan: {e}\n")
            else:
                print("Harap atur Matriks 1 dan Matriks 2 terlebih dahulu.\n")
        elif choice == '5':
            m1 = manager.get_matrix(0)
            if m1 is not None:
                try:
                    inverted = invert_matrix(m1)
                    print("\n--- Matriks 1 yang Diinvers ---")
                    for row in inverted:
                        print(row)
                    print("---------------------------\n")
                except ValueError as e:
                    print(f"Kesalahan: {e}\n")
            else:
                print("Harap atur Matriks 1 terlebih dahulu.\n")
        elif choice == '6':
            m2 = manager.get_matrix(1)
            if m2 is not None:
                try:
                    inverted = invert_matrix(m2)
                    print("\n--- Matriks 2 yang Diinvers ---")
                    for row in inverted:
                        print(row)
                    print("---------------------------\n")
                except ValueError as e:
                    print(f"Kesalahan: {e}\n")
            else:
                print("Harap atur Matriks 2 terlebih dahulu.\n")
        elif choice == '7':
            try:
                size_input = input("Masukkan ukuran matriks identitas (misalnya, 3 untuk 3x3): ").strip()
                size = int(size_input)
                identity_matrix = create_identity_matrix(size)
                print("\n--- Matriks Identitas yang Dibuat ---")
                for row in identity_matrix:
                    print(row)
                slot_choice = input("Pilih slot (1 atau 2) untuk menyimpan matriks identitas: ").strip()
                slot_index = int(slot_choice) - 1
                if slot_index in [0, 1]:
                    manager.matrices[slot_index] = identity_matrix
                    print(f"Matriks Identitas berhasil disimpan di Slot {slot_index + 1}.\n")
                else:
                    print("Pilihan slot tidak valid. Matriks identitas tidak disimpan.\n")
            except ValueError:
                print("Masukan tidak valid. Harap masukkan bilangan bulat.\n")
        elif choice == '8':
            m1 = manager.get_matrix(0)
            m2 = manager.get_matrix(1)
            if m1 is not None and m2 is not None:
                try:
                    result = multiply_matrices(m1, m2)
                    print("\n--- Hasil Perkalian (Matriks 1 * Matriks 2) ---")
                    for row in result:
                        print(row)
                    print("--------------------------------------------------\n")
                except ValueError as e:
                    print(f"Kesalahan: {e}\n")
            else:
                print("Harap atur Matriks 1 dan Matriks 2 terlebih dahulu.\n")
        elif choice == '0':
            print("Keluar dari Menu Operasi Matriks.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()