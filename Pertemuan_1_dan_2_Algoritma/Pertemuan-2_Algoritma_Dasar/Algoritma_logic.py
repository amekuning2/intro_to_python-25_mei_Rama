# study kasus
nilai_rapot = 100

# if
# format dasar
# if kondisi :
#   apa yang akan kamu lakukan jika kondisin terpenuhi
# kalau tidak terpenuhi program akan tetap berjalan

print("=========if=========")
nilai_rapot = 50
if nilai_rapot >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
print("Program akan terus berlanjut")

print("=========if=========")
nilai_rapot = 50
if nilai_rapot >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
else:
    print("Kamu tidak lulus !!")


print("=========Tenery=========")
nilai_rapot = 50
pesan = "Lulus" if nilai_rapot >= 100 else "Tidak Lulus"
print(f"{pesan}")

#cek on : if, else, tenery

print("=========if elif else")
nilai_rapot = 60

if nilai_rapot >= 100:
    print("Selamat kamu lulus dalam test ini !")
elif nilai_rapot >= 50 and nilai_rapot < 100:
    print("Kamu lulus dengan nilai paspasan")
else:
    print("Kamu tidak lulus!")

# cek on : if elif else

print("=========if nesterd(bersarang)")
nilai_rapot = 60

if nilai_rapot >= 100:
    print("Selamat kamu lulus dalam test ini !")
elif nilai_rapot >= 50 and nilai_rapot < 100:
    if nilai_rapot > 70: # ini disebut if nesterd bersarang
        print("Kamu lulus")
    else:
        print("Kamu lulus dengan nilai paspasan!")
else:
    print("Kamu tidak lulus")

# cek on : if nesterd

# tips penulisan coding profesional = cari syarat yang paling sedikit


# switch case
# command ini dipakai saat tau spesifik apa yang akan di lakukan user

print("=========Switch Case=========")
print("=========Menu=========")
print("1.Start")
print("2.End")
select = input("Select => ")
match select:
    case "1":
        print("Start")
    case "2":
        print("End")
    case _ :
        print("Invalid input type !")

