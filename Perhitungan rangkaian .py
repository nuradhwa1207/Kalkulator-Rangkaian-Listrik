

print()
print("=" * 10, "  WELCOME TO CALCILY  ", "=" * 10)
print("-" * 9, "CALculate CIrcuits easiLY", "-" * 9)
print()


# Menampilkan semua menu 
def tampilkan_menu_seri():
    print("-" * 12, "Menu Rangkaian Seri:", "-" * 12)
    print("1. Hitung Total Resistansi Seri")
    print("2. Hitung Total Arus Seri")
    print("3. Hitung Nilai Tegangan pada Setiap Resistor Seri")
    print("4. Kembali ke Menu Utama")
    print()
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    print()
    return pilihan

def tampilkan_menu_paralel():
    print("-" * 11, "Menu Rangkaian Paralel:", "-" * 11)
    print("1. Hitung Total Resistansi Paralel")
    print("2. Hitung Total Arus Paralel")
    print("3. Hitung Nilai Arus pada Setiap Resistor Paralel")
    print("4. Kembali ke Menu Utama")
    print()
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    print()
    return pilihan

def tampilkan_menu_campuran():
    print("-" * 10, "Menu Rangkaian Campuran:", "-" * 10)
    print("1. Hitung Total Resistansi Campuran")
    print("2. Hitung Total Arus Campuran")
    print("3. Kembali ke Menu Utama")
    print()
    pilihan = input("Masukkan pilihan (1/2/3): ")
    print()
    return pilihan

# Input nilai resistor
## input nilai resistor seri
def input_nilai_resistor_seri():
    nilai_resistor_seri = input("Masukkan nilai resistor seri  (pisahkan dengan koma untuk resistansi dalam rangkaian): ")
    resistors_seri = [float(resistor.strip()) for resistor in nilai_resistor_seri.split(',')]
    print()
    return resistors_seri

## input nilai resistor paralel
def input_nilai_resistor_paralel():
    nilai_resistor_paralel = input("Masukkan nilai resistor paralel (pisahkan dengan koma untuk resistansi dalam rangkaian): ")
    resistors_paralel = [float(resistor.strip()) for resistor in nilai_resistor_paralel.split(',')]
    return resistors_paralel

## input nilai resistor campuran
def input_nilai_resistor_campuran():
    resistors_seri = input_nilai_resistor_seri()
    resistors_paralel = input_nilai_resistor_paralel()
    return resistors_seri, resistors_paralel

# menghitung resistansi total,arus, dan tegangan 
##  Rangkaian seri
def hitung_resistansi_seri(resistors):
    total_resistansi_seri = sum(resistors)
    return total_resistansi_seri

def total_arus_seri(tegangan, total_resistance_seri):
    arus_seri = tegangan / total_resistance_seri
    return arus_seri

def hitung_tegangan_seri(tegangan, resistors):
    total_resistance_seri = sum(resistors)
    tegangan_per_resistor = [resistor * (tegangan / total_resistance_seri) for resistor in resistors]
    return tegangan_per_resistor

## Rangkaian Paralel
def hitung_resistansi_paralel(resistors):
    total_resistansi_paralel = 1 / sum(1 / resistor for resistor in resistors)
    return total_resistansi_paralel

def total_arus_paralel(tegangan, total_resistance_paralel):
    arus_paralel = tegangan / total_resistance_paralel
    return arus_paralel

def hitung_arus_paralel(tegangan, resistors):
    arus_per_resistor = [tegangan / resistor for resistor in resistors]
    return arus_per_resistor

## Ragnkaian Campuran
def hitung_resistansi_campuran(resistors_seri, resistors_paralel):
    total_resistansi_seri = hitung_resistansi_seri(resistors_seri)
    total_resistansi_paralel = hitung_resistansi_paralel(resistors_paralel)
    total_resistansi_campuran = total_resistansi_seri + total_resistansi_paralel
    return total_resistansi_campuran

def total_arus_campuran(tegangan, total_resistance_campuran):
    arus_campuran = tegangan / total_resistance_campuran
    return arus_campuran


# Menampilkan menu utama
def main():
    while True:

        print("=" * 15," MENU UTAMA ", "=" * 15)
        print("1. Rangkaian Seri")
        print("2. Rangkaian Paralel")
        print("3. Rangkaian Campuran")
        print("4. Keluar")
        print()
        pilihan_utama = input("Masukkan pilihan (1/2/3/4): ")
        

        if pilihan_utama == '1':
            while True:
                pilihan_seri = tampilkan_menu_seri()
                
                if pilihan_seri == '1':
                    resistors = input_nilai_resistor_seri()
                    total_resistansi_seri = hitung_resistansi_seri(resistors)
                    print(f"Total resistansi dalam rangkaian seri adalah: {total_resistansi_seri} Ohm\n")
                    
                
                elif pilihan_seri == '2':
                    tegangan = float(input("Masukkan nilai tegangan: "))
                    resistors = input_nilai_resistor_seri()
                    total_resistansi_seri = hitung_resistansi_seri(resistors)
                    arus_seri = total_arus_seri(tegangan, total_resistansi_seri)
                    print(f"Arus dalam rangkaian seri adalah: {arus_seri} Ampere\n")
                    
                
                elif pilihan_seri == '3':
                    tegangan = float(input("Masukkan nilai tegangan: "))
                    resistors = input_nilai_resistor_seri()
                    tegangan_per_resistor = hitung_tegangan_seri(tegangan, resistors)
                    for i, tegangan in enumerate(tegangan_per_resistor):
                        print(f"Tegangan pada Resistor {i + 1} adalah: {tegangan} Volt\n")
                     
                elif pilihan_seri == '4':
                    break
                    
                else:
                    print("Pilihan tidak valid. Masukkan pilihan yang benar.\n")
        
        elif pilihan_utama == '2':
            while True:
                pilihan_paralel = tampilkan_menu_paralel()
                
                # Implementasikan fungsionalitas untuk rangkaian paralel
                
                if pilihan_paralel == '1':
                    resistors = input_nilai_resistor_paralel()
                    total_resistance_parallel = hitung_resistansi_paralel(resistors)
                    print(f"Total resistansi dalam rangkaian paralel adalah: {total_resistance_parallel} Ohm\n")
                
                elif pilihan_paralel == '2':
                    tegangan = float(input("Masukkan nilai tegangan: "))
                    resistors = input_nilai_resistor_paralel()
                    total_resistance_parallel = hitung_resistansi_seri(resistors)  # Ubah ke serial untuk menghitung arus
                    arus = total_arus_paralel(tegangan, total_resistance_parallel)
                    print(f"Arus dalam rangkaian paraalel adalah: {arus} Ampere\n")

                elif pilihan_paralel == '3':
                    tegangan = float(input("Masukkan nilai tegangan: "))
                    resistors = input_nilai_resistor_paralel()
                    arus_per_resistor = hitung_arus_paralel(tegangan, resistors)
                    for i, arus in enumerate(arus_per_resistor):
                        print(f"Arus pada Resistor {i + 1} adalah: {arus} Ampere\n")
                    print()

                elif pilihan_paralel == '4':
                    break
                
                else:
                    print("Pilihan tidak valid. Masukkan pilihan yang benar.\n")
        
        elif pilihan_utama == '3':
            while True:
                pilihan_campuran = tampilkan_menu_campuran()
                
                # Implementasikan fungsionalitas untuk rangkaian campuran
                if pilihan_campuran == '1':
                    resistors_seri, resistors_paralel = input_nilai_resistor_campuran()
                    total_resistansi_campuran = hitung_resistansi_campuran(resistors_seri, resistors_paralel)
                    print(f"Total resistansi dalam rangkaian campuran adalah: {total_resistansi_campuran} Ohm\n")
                
                elif pilihan_campuran == '2':
                   tegangan = float(input("Masukkan nilai tegangan: "))
                   resistors_seri, resistors_paralel = input_nilai_resistor_campuran()
                   total_resistansi_campuran = hitung_resistansi_campuran(resistors_seri, resistors_paralel)
                   arus_campuran = total_arus_campuran(tegangan, total_resistansi_campuran)
                   print(f"Arus dalam rangkaian campuran adalah: {arus_campuran} Ampere\n")
         
                elif pilihan_campuran == '3':
                    break
                
                else:
                    print("Pilihan tidak valid. Masukkan pilihan yang benar.\n")
        
        elif pilihan_utama == '4':
            print("Terima kasih, telah menggunakan layanan CALCILY.")
            break
        
        else:
            print("Pilihan tidak valid. Masukkan pilihan yang benar.\n")
# Tampilkan Hasil
if __name__ == "__main__":
    main()