class Transfortasi :
    def intro (self):
        print("Banyak jenis transfortasi di indonesia dan semua transfortasi memiliki bentuk dan jenis yang berbeda")

    def Jenis(self):
        print("Jenis  ransfortasi ada darat, laut, udara")

class keretaApi(Transfortasi):
    def Jenis(self):
        print("Termasuk jenis transfortasi darat")

class Pesawat(Transfortasi):
    def Jenis(self):
        print("Termasuk jenis transfortasi udara")

class Kapal(Transfortasi):
    def Jenis(self):
        print("Termasuk jenis transfortasi laut")

class Angkot(Transfortasi):
    def Jenis(self):
        print("Termasuk jenis transfortasi darat")

obj_transfortasi = Transfortasi()
obj_keretaapi = keretaApi()
obj_pesawat = Pesawat()
obj_kapal = Kapal()
obj_angkot = Angkot()

print("--------------------------------------------------------------------------")
obj_transfortasi.intro()
obj_transfortasi.Jenis()
print("--------------------------------------------------------------------------")

obj_keretaapi.intro()
obj_keretaapi.Jenis()
print("--------------------------------------------------------------------------")

obj_pesawat.intro()
obj_pesawat.Jenis()
print("--------------------------------------------------------------------------")

obj_kapal.intro()
obj_kapal.Jenis()
print("--------------------------------------------------------------------------")

obj_angkot.intro()
obj_angkot.Jenis()
print("--------------------------------------------------------------------------")