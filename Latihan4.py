class kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("meow")

class dog:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("guk..guk..")

kucing1 = kucing("tom", 3)
anjing1 = dog("plash", 5)

for hewan in (kucing1, anjing1):
    hewan.bersuara()

