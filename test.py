import os

def clear():
    # fungsi clear screen cross-platform
    os.system('cls' if os.name == 'nt' else 'clear')

user = (input("Masukkan Nama: "))
while True:
    nilai = (input('''=======================
0. Keluar Permainan
1. Belajar
2. Bermain Basket
3. Makan
pilih lah antara 3 pilihan diatas: '''))


    if nilai == "1":
        print(f'''========================================
{user} menjadi sangat stress karena dia tidak suka belajar!''')

    
    elif nilai == "2":
        print(f'''===========================================
{user} menjadi sangat senang karena dia suka bermain basket!''')

    
    elif nilai == "3":
        print(f'''======================================================
{user} menjadi sangat gemuk (obesitas) karena dia terlalu bayak makan!''')

    elif nilai == "0":
        print(f'''==============================
Sampai jumpa {user}👋 ''')

    
    elif user == nilai:
        print('''======================================
kenapa malah masukin nama lu!''')
        continue
        
    else:
        print('''======================================
Masukkan nomor 1-3!''')
        continue
    
    while True:            
        ulang = input('''================================ 
Apakah anda ingin mengulang? y/n: ''').lower()
            
        if ulang == "n":
                print(f'''==============================
Sampai jumpa {user}👋 ''')
                exit()
                
        if ulang == "y":
            break

            
            
        else:
            print("\nmasukkan y/n saja!")
            
        
        
    

