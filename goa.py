import random

welcome_message = "WELCOME TO GOA MU GAMES!"
cuypy_position = random.randint(1, 4)

print("******************************")
print(f"** {welcome_message} **")
print("******************************")

nama_user = input("masukan nama kamu: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini  
|_| |_| |_| |_|
''')
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
            break
        else:
            print("\nMaaf kamu kalah!")
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
            