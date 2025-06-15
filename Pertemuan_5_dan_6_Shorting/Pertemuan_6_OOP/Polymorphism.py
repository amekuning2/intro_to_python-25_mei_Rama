from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def menyalakanMesin(self):
        pass

class Motor(Kendaraan):
    def menyalakanMesin(self):
        print("Status Motor : Mogok")

class Mobil(Kendaraan):
    def menyalakanMesin(self):
        print("Status Mobil : Hidup")

class Pesawat(Kendaraan):
    def menyalakanMesin(self):
        print("Status Pesawat : Terbang")

class Kapal(Kendaraan):
    def menyalakanMesin(self):
        print("Status Kapal : Berlayar")

# teknik polymorphism
def menyalakanMesin(Kendaraan):
    Kendaraan.menyalakanMesin()


Matic = Motor()
Supra = Mobil()
Boeing = Pesawat()
Titanic = Kapal()

menyalakanMesin(Matic)
menyalakanMesin(Supra)
menyalakanMesin(Boeing)
menyalakanMesin(Titanic)
# Output:
# Status Motor : Mogok
# Status Mobil : Hidup
# Status Pesawat : Terbang
# Status Kapal : Berlayar
# Kode ini mendemonstrasikan polimorfisme di Python menggunakan kelas abstrak dan metode overriding.
# Setiap subclass mengimplementasikan metode abstrak `menyalakanMesin` dengan caranya sendiri.
# Fungsi `menyalakanMesin` menerima sebuah instance dari `Kendaraan` dan memanggil metode `menyalakanMesin` miliknya,
# menunjukkan polimorfisme dengan memungkinkan berbagai jenis kendaraan diperlakukan secara seragam.
# Output menunjukkan perilaku spesifik dari setiap jenis kendaraan saat metode tersebut dipanggil.