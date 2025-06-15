# Case Ibu dan Anak

class Ibu:
    Panggilan = "Ibu"
    Sifat = "Penuh kasih sayang"

    def setSifat(self, sifat):
        self._Sifat = sifat
    
    def getSifat(self):
        return f"Sifat Subject : {self._Sifat}"
    
    def getPanggilan(self):
        return f"Panggilan : {self.Panggilan}"

class Anak(Ibu): # ini disebut encapsulation
    def disuruh(self):
        return f"Iya, ada apa Ibu ?"


# cara memanggil
Toni = Anak()
Toni.Panggilan = "Tonsky"
Toni.setSifat("Ramah")
print(Toni.getPanggilan())
print(Toni.getSifat())

