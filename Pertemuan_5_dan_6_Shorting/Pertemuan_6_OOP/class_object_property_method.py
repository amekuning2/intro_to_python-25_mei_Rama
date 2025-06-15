# case mobil

class Mobil: # mobil itu disebut class
    roda = 4 # roda adalah property atau object dari class mobil public
    # property public adalah nilai yang bisa diubah dari luar class.
    _warna = "default" # warna memiliki property private.
    # property private adalah nilai yang hanya bisa diubah jika di izinkan.
    __merk = "default" # merk memiiki property protected.( __ )
    # property protected adalah nilai yang tidak bisa diubah di luar class apapun.

    def __init__(self, brand:str = None, warna:str = None, merk:str = None): # init adalah method constructor
        self.__merk = merk
        self._brand = brand
        self._warna = warna

    # method
    def getDetails(self):
        print(f"Nama Brand : {self._brand}")
        print(f"Warna : {self._warna}")
        print(f"Merk : {self.__merk}")
        print(f"Jumlah Roda : {self.roda}")
    # method ini adalah method untuk mendapatkan detail dari mobil

    # cara memanggil method
Toyota = Mobil("Toyota","Supra","Hitam")
Toyota.getDetails()
    # Toyota adalah objek dari class Mobil
    # Toyota.getDetails() akan memanggil method getDetails dari class Mobil