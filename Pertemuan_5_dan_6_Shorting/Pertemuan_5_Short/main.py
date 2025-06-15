import random 
# ini disebut library, library ini berisi kumpulan fungsi yang bisa kita pakai
# Packaga (Java), Library (Python), Module (JavaScript), Header (C, C++, C#)
# Shorting
# Shorting adalah proses mengurutkan data
# Ada beberapa algoritma shorting yang sering di pakai
# Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort
def random_generate(jumlah_data):
    list_data = []
    for index in range(jumlah_data):
        value = random.randint(1,100)
        list_data.append(value)
    return list_data


def bubble_sort(data):
    n = len(data) #len adalah fungsi untuk menghitung jumlah data dalam list
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp

                # rumus di atas adalah rumus jadul untuk menukar posisi data

                # tukar posisi
                data[j],data[j+1] = data[j+1],data[j]

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]
        merge_sort(L) # rekursif ini berbahaya bisa menyebabkan infinite loop
        merge_sort(R)

        # i = 0
        # j = 0
        # k = 0
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1


def main():
    banyak_data = int(input("Banyak data yang ingin di generate : "))
    list_data = random_generate(banyak_data)
    print("===List Data Random :")
    print(list_data)
    input("Please Press Enter to next step...")
    # selection_sort(list_data)
    # insertion_sort(list_data)
    insertion_sort(list_data)
    print("===List Data Setelah di Shorting :")
    print(list_data)
    # Error Handling
    # teknik program agar terus berjalan meskipun ada error
    # try:
            # banyak_data = int(input("Banyak data yang ingin di generate : "))
        # # validation
        # # teknik untuk melakukan pengecekan lebih lanjut
        # if banyak_data <= 0:
        #     print("Banyak data harus lebih dari 0")
        #     main()
        # else:
            # list_data = random_generate(banyak_data)
            # print("===List Data Random :")
            # print(list_data)
            # input("Please Press Enter to next step...")
            # # bubble_sort(list_data)
            # selection_sort(list_data)
            # # print("===List Data Setelah di Shorting (Bubble Sort) :")
            # print("===List Data Setelah di Shorting :")
            # print(list_data)
       

        # list_data = random_generate(banyak_data)
        # print("===List Data Random :")
        # print(list_data)
    #     # input("Please Press Enter to next step...")


    # except:
    #     print("Masukan data dengan tipe numerik!")
    #     main()


if __name__ == "__main__":
    main()