nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM-nya: ")
if nim[2:4] == '22' :
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")
elif nim[2:4] == '21' :
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")
elif nim[2:4] == '20' :
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")
else:
    print(nama,"bukan merupakan mahasiswa informatika angkatan 20 hingga 22")