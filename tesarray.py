kotak = ["Alfarez", "Ridho", "Ghaizan"]
kotak.append("Syahid")
kotak.append("Dika")

while True:
    nomor = input("Masukkan sebuah nomor 0-4: ")
    
    if not nomor.isdigit():
        print("\nAnda hanya boleh menggunakan nomor!")
        continue
    
    nomor =int(nomor)
    
    if nomor < 0 and nomor > 4:
        print("\nAnda hanya boleh menggunakan nomor 0-4!")
        continue
    
    print("\n anda memilih: ", kotak[4 - nomor])
    
    coba = input("apakah anda ingin mencoba lagi?. enter jika ya atau ketik exit untuk keluar: ")
    
    if coba == "exit":
        exit()
        
    else:
        continue
    
