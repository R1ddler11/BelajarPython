import random

welcome_message = "WELCOME TO GOA MU GAMES!"
cuypy_position = random.randint(1, 4)

print("******************************")
print(f"** {welcome_message} **")
print("******************************")

nama_user = input("masukan nama kamu: ")


bentuk = "|_|" 
goasebelum = [bentuk] * 4 
goa = goasebelum.copy()
goa[cuypy_position - 1] = "|0_0|"

print(f'''Halo {nama_user} coba tebak dimana cuypy berada!''')
print(" ".join(goasebelum))

while True:
    pilihan_user = int(input("\nMenurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
    
    while True:
        konfirmasi = input(f"\napakah kamu yakin pilihanmu adalah {pilihan_user}?. y/n: ").lower()
        if konfirmasi in["y", "n"]:
            break
        else:
            print("\nKamu hanya boleh memasukkan y/n!")
        
    if konfirmasi == "n":
        continue
        
    else:
        if pilihan_user == cuypy_position:
            print("\nSelamat Kamu Menang!")
            print(f''' '''.join(goa))
            break
        else:
            print("\nMaaf kamu kalah!")
            print(" ".join(goa))
            print(f'''
Posisi cuypy berada di goa nomor {cuypy_position}
''')
            while True:
                coba = input("\nIngin mencoba lagi?. tekan enter jika ingin mencoba lagi!. ketik 'exit' jika ingin keluar: ")
                if coba == "exit":
                    exit()
                elif coba == "":
                    break
                elif coba != "exit":
                    print("\n!!! kamu hanya bisa mengetik exit !!!")
                    continue
                else:
                    continue
            