# Folder Arsitektur
# MVC, MVP, MVVM
# Monolithic vs Mikro Service

# Search those word

# Apa List?
# inisialisasi
# teknik program menyediakan memory yang akan dipakai

makanan = ["nasi","sayur","ayam"]

# cara mencetak ; Read (R)
print(f"List Makanan : {makanan}")

# read spesifik
print(f"Index of 1 : {makanan[1]}")
print(f"Index of -1 : {makanan[-1]}")

# Update (U)
makanan[1] = "daging"
print(f"List Makanan setelah di update: {makanan}")

# tambah data 'append' (a)
makanan.append("sayur")
print(f"List Makanan setelah di add : {makanan}")

makanan.remove("nasi")
print(f"List Makanan setelah di delete: {makanan}")

buah = ["semangka","melon","nanas"]

makanan += buah
print(f"List makanan setelah di add list: {makanan}")
