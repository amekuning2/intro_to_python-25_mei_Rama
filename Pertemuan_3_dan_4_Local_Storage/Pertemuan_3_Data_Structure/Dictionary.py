profile = {
    "nama" : "Rama",
    "Kelas" : 8,
    "jurusan" : ["design","engineer"]
}

print(f"Dictionary Data : {profile}")
print(f"Nama : {profile['nama']}")
print(f"Cara mengambil jurusan engineer : {profile['jurusan'][1]}")


profile['Kelas'] = 9
print(f"Dictionary Data : {profile}")
profile['ketua_kelas'] = "Ame"
print(f"Dictionary Data : {profile}")

del profile["ketua_kelas"]
print(f"Dictionary Data : {profile}")

