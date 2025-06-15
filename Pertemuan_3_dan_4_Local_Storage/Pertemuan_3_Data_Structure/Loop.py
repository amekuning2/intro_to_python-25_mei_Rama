def main():
    # while
    # saat kita tau syarat tapi masih ragu dengan jalan menuju syaratnya
    # sifat utamanya
    # check terlebih dahulu baru dijalankan

    index = 0
    while index <= 10:
        print(f"{index}, Sorry Beb !!")
        index += 1
        # do while
        # sidat di kerjakan dulu baru di check
        # tidak ada di python tapi ada di java, javascript, atau keluarga C, C++, dan C#
        print("======for======")
        # for 
        # for di pakai saat kamu tau syarat dan cara menujunya
        for value in range (1,10+1) :
            print(f"Index of {value}")
        
        makanan = ['daging', 'ayam', 'sayur', 'semangka', 'melon', 'nanas']
        for value in makanan:
            print(f"List Makanan : {value}")


if __name__ =="__main__":
    main()
# format dasar untuk memberitahukan kalau program yang di jalankan adalah file ini