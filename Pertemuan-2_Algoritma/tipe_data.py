#integer (int)
#ini bilangan bulat
# contoh 0123
x = 32767
print("Ini contoh tipe data Integer : {0}".format(x))

#float (bilangan desimal)
y = 3.14
print("Ini contoh tipe data float : {0}".format(y))

# kompleks
z = 2 + 3j
print("Ini contoh tipe data kompleks : {0}".format(z))


# tipe data squenc
a = [1,2,3] # List sifat tipe data nya value nya sebisa mungkin tipedatanya
print("Ini contoh tipe data list : {0}".format(a))
b = (4,5,6) #truplet sifat tipe data nya tidak bisa diganti
print("Ini contoh tipe data truplet : {0}".format(b))
c = range(0,5)
print("Ini contoh tipe data range : {0}".format(c))


#text
nama = "Ame" #tipe data string karena pakai tanda quote
print("Ini contoh tipe data float : {0}".format(y))

#sejarah string terdiri dari 255 karakter
karakter = 'A' #pakai tanda akostrop

# set
f = {1,2,3} # set tipe data uang tidak bisa di ubah
print("Ini contoh tipe data set : {0}".format(f))
g = frozenset({4,5,6}) #frozenset
print("Ini contoh tipe data frozenset : {0}".format(g))


#tipe data kondisi
#booleal (bool)
#inisnya hanya dua True (1) atau False (0)
kondisi_badan = True

#tipe data binary
i = 0b1000001
desimal = int(i)
print("Conversi binary to Desimal : {0}".format(desimal))
char = chr(desimal)
print("Conversi Desimal to char : {0}".format(char))

print("Singkat binary to char : {0}".format(chr(int(i))))

j = bytearray(a)
print("Isi binary dalam array variable a : {0}".format(j))

z = memoryview(j)
print("lokasi array dalam memory (RAM) : {0}".format(z))

