class namakelas:
    common = 10
    def __init__ (self):
        self.myvariable = 3
    def myfunction (self, arg1, arg2):
        return self.myvariable

instance = namakelas()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))

instance2 = namakelas()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)

namakelas.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)

instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
namakelas.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)

class AnotherClass (namakelas):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))

instance.test = 10
print("instance.test " , instance.test)

#Percobaan sendiri
print("\n ### Ini adalah hasil dari Class yang dibuat sendiri ### \n")

class Meong:
    umur = 2
    def __init__(self):
        self.ekor = 1
        self.kaki = 4
    def berlari(self, majikan):
        activity = "Meong memiliki" + str(self.ekor) + " buah ekor dan sedang berlari dengan"
        return activity + ' ' + majikan

# Memanggil function berlari
percobaan = Meong()
print("percobaan.berlari(kiko)" , percobaan.berlari("Kiko"))

percobaanKedua = Meong()
print("percobaanKedua.berlari(kuka)", percobaan.berlari("Kuka"))

# Memanggil umur
print("percobaanKedua.umur", percobaanKedua.umur)
percobaanKedua.umur = 5

# Memanggil umur yang sudah di assign dengan nilai baru
print("percobaanKedua.umur", percobaan.umur)
print("percobaan.umur", percobaan.umur)

print("\n ### Membuat Class turunan dari Meong ### \n")

# Membuat Class baru yang Inherit dari class Meong
class Kitten (Meong):
    def __init__(self, komen):
        self.ekor = 1
        print(komen)
    def belajar(self, teman):
        return teman

percobaanKetiga = Kitten("Ini adalah komentar")

print("percobaanKetiga.umur" , percobaanKetiga.umur)

# Memanggil fuction dari class induk
print("percobaanKetiga.berlari" , percobaanKetiga.berlari("nino"))

# Memanggil Buatan sendiri
print("percobaanKetiga.belajar" , percobaanKetiga.belajar("Mimi"))
