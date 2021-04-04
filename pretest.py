#import modul mysql connector
import mysql.connector
import os

#koneksi dengan mysql
db = mysql.connector.connect(
    host="localhost", #host dari database
    user="root", #user dari database
    passwd="", #password dari database
    database="db_ims" #nama database yang digunakan
)

#mengecek koneksi
if db.is_connected():
    print("Koneksi Berhasil")

#membuat cursor untuk execute kode sql
cursor = db.cursor()

def create_peserta(db): #membuat class create_peserta
    #input data yang diperlukan sesuai database
    nama_depan = input ("Masukan Nama Depan: ")
    nama_belakang = input ("Masukan Nama Belakang: ")
    alamat = input ("Masukan Nama Alamat: ")
    no_telp = input ("Masukan No Telepon: ")
    id_rank = input ("Masukan ID Rank: ")
    val = (nama_depan, nama_belakang, alamat, no_telp, id_rank) #variable inputan data
    cursor = db.cursor() #membuat cursor execute dari kode SQL
    sql = "INSERT INTO tb_peserta (nama_depan, nama_belakang, alamat, no_telp, id_rank) VALUES (%s, %s, %s, %s, %s)" #insert data ke databse
    cursor.execute(sql, val)#menjalankan sql
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil disimpan".format(cursor.rowcount)) #print data berhasil 

def create_pertandingan(db):
    #meinputkan data yang diperlukan pada databases 
    id_peserta_a = input ("Masukan ID Peserta Pertama: ")
    id_peserta_b = input ("Masukan ID Peserta Kedua: ")
    hasil = input ("Masukan Hasil Pertandingan: ")
    mulai = input ("Masukan Mulai Pertandingan: ")
    selesai = input ("Masukan Selesai Pertandingan: ")
    val = (id_peserta_a, id_peserta_b, hasil, mulai, selesai) #variable yang dibutuhkan
    cursor = db.cursor() #membuat cursor execute dari kode SQL
    sql = "INSERT INTO tb_pertandingan (id_peserta_a, id_peserta_b, hasil, mulai, selesai) VALUES (%s, %s, %s, %s, %s)" #insert data ke database
    cursor.execute(sql, val)#menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil disimpan".format(cursor.rowcount)) #menampilkan pesan

def create_rank(db):
    #menginputkan data yang diperlukan dari database
    rank = input ("Masukan Ranking: ")
    deskripsi = input ("Masukan Deskripsi: ")
    val = (rank, deskripsi) #membuat variable
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    sql = "INSERT INTO tb_rank (rank, deskripsi) VALUES (%s, %s)" #insert data ke database
    cursor.execute(sql, val) #menjalankan SQL
    db.commit()  #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil disimpan".format(cursor.rowcount)) #menampilkan pesan

def show_peserta(db): #membuat class
    cursor = db.cursor() #membuat cursor execute kode SQL
    sql = "SELECT * FROM tb_peserta" #mengambil data pada tb_peserta
    cursor.execute(sql) #menjalankan SQL
    results = cursor.fetchall() #membuat perulangan yang berisikan kode data SQL yang sudah dijalankan
    if cursor.rowcount < 0: #jika data dibawah 0
        print("Tidak ada data") #tampilkan pesan
    else: #jika tidak
        for data in results: #perulangan data pada result
            print(data) #tampilkan data 

def show_pertandingan(db): #membuat class
    cursor = db.cursor() #membuat cursor execute kode SQL
    sql = "SELECT * FROM tb_pertandingan" #mengambil data pada tb_pertandingan
    cursor.execute(sql) #menjalankan SQL
    results = cursor.fetchall() #membuat perulangan yang berisikan kode data SQL yang sudah dijalankan
    if cursor.rowcount < 0: #jika data dibawah 0
        print("Tidak ada data") #tampilkan pesan
    else: #jika tidak
        for data in results: #perulangan data pada result
            print(data) #tampilkan data

def show_rank(db): #membuat class 
    cursor = db.cursor() #membuat cursor execute kode SQL
    sql = "SELECT * FROM tb_rank" #mengambil data pada tb_rank
    cursor.execute(sql) #menjalankan SQL
    results = cursor.fetchall() #membuat perulangan yang berisikan kode data SQL yang sudah dijalankan
    if cursor.rowcount < 0: #jika di bawah 0
        print("Tidak ada data") #tampilkan pesan
    else: #jika tidak
        for data in results: #perulangan data pada result
            print(data) #tampilkan data

def update_rank(db): #membuat class
    cursor = db.cursor() #membuat cursor untuk exxecute kode SQL
    show_rank(db) #memanggil class  
    id_rank = input("Pilih ID Rank: ") #memilih id yang akan diupdate
    rank = input("Rank Baru: ") #menginput rank baru 
    deskripsi = input("Deskripsi Baru:") #menginput deskripsi baru
    sql = "UPDATE tb_rank SET rank=%s, deskripsi=%s WHERE id_rank=%s" #perintah update pada database
    val = (rank, deskripsi, id_rank) #variable
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil diubah".format(cursor.rowcount)) #menampilkan pesan

def update_peserta(db): #membuat class
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    show_peserta(db) #memanggil class
    id_peserta = input("Pilih ID Peserta: ") #memilih id yang ingin di update
    nama_depan = input("Nama Depan Baru: ") #mengubah data baru
    nama_belakang = input("Nama Belakang Baru: ") #mengubah data baru
    alamat = input("Alamat Baru: ") #mengubah data baru
    no_telp = input("No Telepon Baru:") #mengubah data baru 
    id_rank = input("ID Rank Baru:") #mengubah data baru
    sql = "UPDATE tb_peserta SET nama_depan=%s, nama_belakang=%s, alamat=%s, no_telp=%s, id_rank=%s WHERE id_peserta=%s" #perintah update untuk database
    val = (nama_depan, nama_belakang, alamat, no_telp, id_rank, id_peserta) #variabel
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil diubah".format(cursor.rowcount)) #menampilkan pesan

def update_pertandingan(db):
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    show_pertandingan(db) #memanggil class
    id_pertandingan = input("Pilih ID Pertandingan: ") #memilih id yang ingin di update
    id_peserta_a = input("ID Baru Peserta Pertama: ") #mengubah data 
    id_peserta_b = input("ID Baru Peserta Kedua: ") #mengubah data
    hasil = input("Hasil Baru:") #mengubah data
    mulai = input("Mulai Baru:") #mengubah data
    selesai = input("Selesai Baru:") #mengubah data
    sql = "UPDATE tb_pertandingan SET id_peserta_a=%s, id_peserta_b=%s, hasil=%s, mulai=%s, selesai=%s WHERE id_pertandingan=%s" #perintah update pada database
    val = (id_peserta_a, id_peserta_b, hasil, mulai, selesai, id_pertandingan) #variabel
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil diubah".format(cursor.rowcount)) #menampilkan pesar

def delete_rank(db): #membuat class
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    show_rank(db) #memanggil class
    id_rank = input("Pilih ID Rank: ") #memilih id yang akan di delete
    sql = "DELETE FROM tb_rank WHERE id_rank=%s" #menjalankan perintah delete pda database
    val = (id_rank,) #variabel
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil dihapus".format(cursor.rowcount)) #menampilkan pesar

def delete_peserta(db): #membuat class
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    show_peserta(db) #memanggil class
    id_peserta = input("Pilih ID Peserta: ") #memilih id yang akan didelete
    sql = "DELETE FROM tb_peserta WHERE id_peserta=%s" #menjalankan perintah delete pada database
    val = (id_peserta,) #variabel
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil dihapus".format(cursor.rowcount)) #menampilkan pesan

def delete_pertandingan(db): #membuat class
    cursor = db.cursor() #membuat cursor untuk execute kode SQL
    show_pertandingan(db) #memanggil class
    id_pertandingan = input("Pilih ID Pertandingan: ") #memilih id yang akan di delete
    sql = "DELETE FROM tb_pertandingan WHERE id_pertandingan=%s" #menjalankan perintah delete pada database
    val = (id_pertandingan,) #variabel
    cursor.execute(sql, val) #menjalankan SQL
    db.commit() #Mengembalikan isi dari db kembali seperti semula dikarekana digunakan sebelumnya
    print("{} data berhasil dihapus".format(cursor.rowcount)) #menampilkan pesan

def peringkat(db):
    cursor = db.cursor() # Membuat cursor execute dari kode sql
    sql = "SELECT * FROM tb_peserta JOIN tb_rank ON tb_peserta.id_rank = tb_rank.id_rank WHERE id_rank IS NOT NULL ORDER BY id_rank ASC" # SQL querry untuk show tb_rank
    cursor.execute(sql) # Menjalankan/execute menu sql
    results = cursor.fetchall() # Membuat perulangan yang berisi data dari kode sql yang sudah dijalankan
    if cursor.rowcount < 0: # Jika data yang tampil dibawah 0
        print("Tidak ada data") # Menampilkan tidak ada data
    else: # Jika bukan
        for data in results: # Perulangan dari result ke dalam data
            print(data) # Menampilkan data

def show_menu(db):
    print("====== TURNAMEN CATUR =======") # Tampilan Menu Utama
    print("1. Menu Peserta") # Tampilan Menu Utama
    print("2. Menu Pertandingan") # Tampilan Menu Utama
    print("3. Menu Ranking") # Tampilan Menu Utama
    print("4. Rekap Ranking") # Tampilan Menu Utama
    print("0. Keluar") # Tampilan Menu Utama
    print("=======================================") # Tampilan Menu Utama
    menu = input("Pilih Menu: ") # Input menu1

    os.system("cls") # Clear screen

    if menu == "1": # Jika menu adalah 1
        print("====== MENU PESERTA =======") # Tampilan Menu 1
        print("1. Create Data Peserta") # Tampilan Menu 1
        print("2. Update Data Peserta") # Tampilan Menu 1
        print("3. Delete Data Peserta") # Tampilan Menu 1
        print("4. Show Data Peserta") # Tampilan Menu 1
        print("0. Keluar") # Tampilan Menu 1
        print("================================") # Tampilan Menu 1
        menu2 = input("Pilih Menu: ") # Input menu2

        if menu2 == "1": # Jika menu2 adalah 1
            create_peserta(db) # Menjalankan fungsi create_peserta parameter db
        elif menu2 == "2": # Jika menu2 adalah 2
            update_peserta(db) # Menjalankan fungsi update_peserta parameter db
        elif menu2 == "3": # Jika menu2 adalah 3
            delete_peserta(db) # Menjalankan fungsi delete_peserta parameter db
        elif menu2 == "4": # Jika menu2 adalah 3
            show_peserta(db) # Menjalankan fungsi show_peserta parameter db
        elif menu2 == "0": # Jika menu2 adalah 0
            exit() # Menjalankan fungsi exit
        else: # Jika tidak sesuai
            print("Menu yang anda masukan salah!") # Tampilan pesan salah

    if menu == "2": # Jika menu adalah 2
        print("====== MENU PERTANDINGAN =======") # Tampilan Menu 2
        print("1. Create Data Pertandingan") # Tampilan Menu 2
        print("2. Update Data Pertandingan") # Tampilan Menu 2
        print("3. Delete Data Pertandingan") # Tampilan Menu 2
        print("4. Show Data Peserta") # Tampilan Menu 2
        print("0. Keluar") # Tampilan Menu 2
        print("=====================================") # Tampilan Menu 2
        menu2 = input("Pilih Menu: ") # Input menu2

        if menu2 == "1": # Jika menu2 adalah 1
            create_pertandingan(db) # Menjalankan fungsi create_pertandingan parameter db
        elif menu2 == "2": # Jika menu2 adalah 2
            update_pertandingan(db) # Menjalankan fungsi update_pertandingan parameter db
        elif menu2 == "3": # Jika menu2 adalah 3
            delete_pertandingan(db) # Menjalankan fungsi delete_pertandingan parameter db
        elif menu2 == "4": # Jika menu2 adalah 4
            show_pertandingan(db) # Menjalankan fungsi show_pertandingan parameter db
        elif menu2 == "0": # Jika menu2 adalah 0
            exit() # Menjalankan fungsi exit
        else: # Jika tidak sesuai
            print("Menu yang anda masukan salah!") # Tampilan pesan salah

    if menu == "3": # Jika menu adalah 3
        print("====== MENU RANKING =======") # Tampilan Menu 2
        print("1. Create Data Ranking") # Tampilan Menu 2
        print("2. Update Data Ranking") # Tampilan Menu 2
        print("3. Delete Data Ranking") # Tampilan Menu 2
        print("4. Show Data Ranking") # Tampilan Menu 2
        print("0. Keluar") # Tampilan Menu 2
        print("================================") # Tampilan Menu 2
        menu2 = input("Pilih Menu: ") # Input menu2

        if menu2 == "1": # Jika menu2 adalah 1
            create_rank(db)  # Menjalankan fungsi create_rank parameter db
        elif menu2 == "2": # Jika menu2 adalah 2
            update_rank(db)  # Menjalankan fungsi update_rank parameter db
        elif menu2 == "3": # Jika menu2 adalah 3
            delete_rank(db)  # Menjalankan fungsi delete_rank parameter db
        elif menu2 == "4": # Jika menu2 adalah 4
            show_rank(db) # Menjalankan fungsi show_rank parameter db
        elif menu2 == "0": # Jika menu2 adalah 0
            exit() # Menjalankan menu exit
        else: # Jika tidak sesuai
            print("Menu yang anda masukan salah!") # Tampilan pesan salah

    if menu == "4": # Jika menu adalah 4
        os.system("cls") # Clear screen
        print("====== Peringkat =======") # Tampilan Menu 2
        peringkat(db)
        os.system("pause") # Clear screen

if __name__ == "__main__": # Jika name sama dengan main
    while(True): # Ketika bernilai benar
        show_menu(db) # Menampilkan fungsi show_menu parameter db
