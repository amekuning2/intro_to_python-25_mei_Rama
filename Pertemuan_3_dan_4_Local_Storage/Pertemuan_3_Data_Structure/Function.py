Employee = [
    {
        "nama" : "Rama",
        "pekerjaan" : "Design Engineer",
        "gaji" : 8000000
    },
    {
        "nama" : "Ame",
        "pekerjaan" : "Engineer",
    }
]

print("=========Daftar Employee=========")
# function void
def detail_pekerja(nama,pekerjaan, gaji = None):
    print(f"Nama : {nama}")
    print(f"Pekerjaan : {pekerjaan}")
    print(f"Gaji :{gaji}")

# cara print
detail_pekerja(Employee[0]['nama'],Employee[0]['pekerjaan'],Employee[0]['gaji'])
detail_pekerja(Employee[1]['nama'],Employee[1]['pekerjaan'])

def penjumlahan (a,b):
    return a + b

hasil_penjumlahan = penjumlahan(10,12)
print(f"hasil dari penjumlahan : {hasil_penjumlahan}")

