# case mobil

class Mobil: 
    roda = 4
    _warna = "default"
    __merk = "default"

    def __init__(self, brand:str = None, warna:str = None, merk:str = None):
        self.__merk = merk
        self._brand = brand
        self._warna = warna

    def getDetails(self):
        print(f"Nama Brand : {self._brand}")
        print(f"Warna : {self._warna}")
        print(f"Warna : {self.getWarna()}")
        print(f"Merk : {self.__merk}")
        print(f"Jumlah Roda : {self.roda}")
    
# set and get
# set
# kalau ada kata awalan set ini sifatnya untuk mengubah nilai dari property

    def setWarna(self, warna):
        self._warna = warna

# get
# kalau ada kata awalan get ini sifatnya untuk mengambil nilai dari property
    def getWarna(self):
        return f"{self._warna} Gross"

toyota = Mobil("Toyota", "Supra", "Hitam")
toyota.roda = 2
toyota.setWarna("Merah")
toyota.getDetails()