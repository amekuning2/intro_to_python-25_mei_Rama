from abc import ABC, abstractmethod

class Hewan(ABC):
    
    def suara():
        print("Hewan bersuara")


class Kucing(Hewan):
    def suara():
        return ("Meong Meong")
    

Tom = Kucing()
Tom.suara()