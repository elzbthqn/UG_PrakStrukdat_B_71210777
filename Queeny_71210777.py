stop = True
while stop:
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("Q.Exit")
    print()
    menu = input("Pilih menu : ")
    print()
    if menu ==  "1":
        bil1 = int(input(" Masukkan bilangan pertama :"))
        bil2 = int(input(" Masukkan bilangan kedua :"))
        hasil = bil1 + bil2
        print(hasil)

    elif menu ==  "2":
        bil1 = int(input(" Masukkan bilangan pertama :"))
        bil2 = int(input(" Masukkan bilangan kedua :"))
        hasil = bil1 - bil2
        print(hasil)

    elif menu ==  "3":
        bil1 = int(input(" Masukkan bilangan pertama :"))
        bil2 = int(input(" Masukkan bilangan kedua :"))
        hasil = bil1 * bil2
        print(hasil)
    
    elif menu ==  "4":
        bil1 = int(input(" Masukkan bilangan pertama :"))
        bil2 = int(input(" Masukkan bilangan kedua :"))
        hasil = bil1 / bil2
        print(hasil)
    
    elif menu ==  "Q":
        print("Thanks")
        stop = False