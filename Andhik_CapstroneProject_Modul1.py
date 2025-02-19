data_pasien = [
    {
        'No Pasien': 10001,
        'Nama': 'Galih Yudha',
        'Jenis Kelamin': 'Pria',
        'Umur': 33,
        'Diagnosis': 'Diabetes'
    },
    {
        'No Pasien': 10002,
        'Nama': 'Zuhdi Saifal',
        'Jenis Kelamin': 'Pria',
        'Umur': 28,
        'Diagnosis': 'Diabetes'
    },
    {
        'No Pasien': 10003,
        'Nama': 'Gracia',
        'Jenis Kelamin': 'Wanita',
        'Umur': 25,
        'Diagnosis': 'Influenza'
    },
]

# Pilihan untuk menampilkan semua data pasien
def daftar_pasien():
    print('\n===========================================================================================')
    text = ('Data Pasien RS. PURWADIKA')
    print(text.center(91))
    print('===========================================================================================')
    print('-------------------------------------------------------------------------------------------')
    print('| No  |    No Pasien   |        Nama        |   Jenis Kelamin    |   Umur   |  Diagnosis  |')
    print('+-----+----------------+--------------------+--------------------+----------+-------------+')
    for i in range(len(data_pasien)):
        print('|{:^5}|{:^16}|{:^20}|{:^20}|{:^10}|{:^13}|'.format(i+1, data_pasien[i]['No Pasien'], data_pasien[i]['Nama'], data_pasien[i]['Jenis Kelamin'], data_pasien[i]['Umur'], data_pasien[i]['Diagnosis']))
        print("+-----+----------------+--------------------+--------------------+----------+-------------+")

# Pilihan untuk no.1  read menu dari report data pasien
def report_pasien():
    while True:
        reportMenu = input('''
+=========================================+
|        Menu Report Data Pasien          |
+=========================================+
|                                         |
|   1. Menampilkan semua data pasien      |
|   2. Menampilkan data pasien tertentu   |
|   3. Kembali ke menu utama              |
+-----------------------------------------+
Silahkan pilih daftar di atas [1-3] : ''')
        if reportMenu == '1':
            daftar_pasien()
        elif reportMenu == '2':
            data_tertentu()
        elif reportMenu == '3':
            menu_awal()
        else:
            print('*** Anda memasukkan pilihan yang salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-3] ')
            continue

# Menampilkan pilihan no 2 pada fitur menu report (data tertentu)
def data_tertentu():
    while True:
        input_nop = input('Masukkan Nomor Pasien : ')
        if input_nop.isnumeric():
            input_nop = int(input_nop)
            for i in range(len(data_pasien)):
                if input_nop == data_pasien[i]['No Pasien']:
                    print('\n===========================================================================================')
                    text = ('Data Pasien RS. PURWADIKA')
                    print(text.center(91))
                    print('===========================================================================================')
                    print('-------------------------------------------------------------------------------------------')
                    print('| No  |    No Pasien   |        Nama        |   Jenis Kelamin    |   Umur   |   Diagnosis |')
                    print('+-----+----------------+--------------------+--------------------+----------+-------------+')
                    print(f'''|{i+1:^5}|{data_pasien[i]['No Pasien']:^16}|{data_pasien[i]['Nama']:^20}|{data_pasien[i]['Jenis Kelamin']:^20}|{data_pasien[i]['Umur']:^10}|{data_pasien[i]['Diagnosis']:^13}|''')
                    print("+-----+----------------+--------------------+--------------------+----------+-------------+")
                    report_pasien()
                    break
                elif i == len(data_pasien) - 1:
                    print('\n\t\t***Data Pasien tidak ditemukan***\n')
        else:
            print("\n***Nomor Pasien harus berupa angka, silahkan ketikkan Nomor Pasien yang benar***\n")

# Tambah data pasien
def add_pasien():
    while True:
        input_pasien_baru = input('''
+=============================+
|  Menu Tambah Data Pasien    |         
+=============================+
|                             |
| 1. Tambah data Pasien       |
| 2. Kembali ke menu utama    |
+-----------------------------+    
Silahkan pilih daftar di atas [1-2] : ''')
        if input_pasien_baru == '1':
            daftar_pasien()
            while True:
                input_nop = input("\n Masukkan Nomor Pasien : ")
                if input_nop.isnumeric():
                    input_nop = int(input_nop)
                    if any(pasien['No Pasien'] == input_nop for pasien in data_pasien):
                        print('''
                     *** Data yang anda tambahkan sudah terdaftar ***
                              Silahkan masukkan data yang lain
                     +----------------------------------------------+ ''')
                        add_pasien()
                    else:
                        nama_pasien = input(' Nama : ').title()
                        jenis_kelamin = input(' Jenis Kelamin : ').title()
                        umur = int(input(' Umur : '))
                        diagnosis = input(' Diagnosis : ').title()
                        break
            while True:
                new_data = input('\nApakah data yang anda masukkan sudah benar(Y/T) :  ').upper()
                if new_data == 'Y':
                    data_pasien.append({
                        'No Pasien': input_nop,
                        'Nama': nama_pasien,
                        'Jenis Kelamin': jenis_kelamin,
                        'Umur': umur,
                        'Diagnosis': diagnosis
                    })
                    daftar_pasien()
                    print('''
                     *** Data Pasien telah berhasil ditambahkan ***''')
                    add_pasien()
                    continue
                elif new_data == 'T':
                    print('''
                     *** Tidak Jadi Menambah Data Pasien ***''')
                    add_pasien()
                else:
                    print('''\n
                    *** Pilihan yang anda masukkan salah *** \n
                    ------------------------------------------                     
                         Silahkan masukkan pilihan (Y/T) \n''')
        elif input_pasien_baru == '2':
            menu_awal()
        else:
            print('\n*** Pilihan yang anda masukkan salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-2] \n')

# update data pasien
def change_pasien():
    while True:
        update_data = input('''
+==============================+
| Menu Perubahan Data Pasien   |
+==============================+
|                              |
| 1. Update data pasien        |
| 2. Kembali ke menu utama     |
-------------------------------- 
Silahkan pilih daftar di atas [1-2] : ''')  
        if update_data == '1':
            daftar_pasien()
            while True:
                input_nop = input('\nMasukkan Nomor Pasien : ')
                if input_nop.isnumeric():
                    input_nop = int(input_nop)
                    for i in range(len(data_pasien)):
                        if input_nop == data_pasien[i]['No Pasien']:
                            print("-------------------------------------------------------------------------------------------")
                            print("| No  |    No Pasien   |        Nama        |   Jenis Kelamin    |   Umur  |   Diagnosis  |")
                            print("+-----+----------------+--------------------+--------------------+----------+-------------+")
                            print(f'''|{i+1:^5}|{data_pasien[i]['No Pasien']:^16}|{data_pasien[i]['Nama']:^20}|{data_pasien[i]['Jenis Kelamin']:^20}|{data_pasien[i]['Umur']:^10}|{data_pasien[i]['Diagnosis']:^13}|''')
                            print("+-----+----------------+--------------------+--------------------+----------+-------------+")
                            while True:
                                new_data = input('Apakah data yang anda masukkan sudah benar(Y/T) :  ').upper()
                                if new_data == 'Y':
                                    while True:
                                        ubah_data = (input('\n1.No Pasien\n2.Nama\n3.Jenis Kelamin\n4.Umur\n5.Diagnosis\nPilih kategori yang ingin di ubah : '))
                                        if ubah_data.isnumeric():
                                            if ubah_data == '1':
                                                ubah_data = 'No Pasien'
                                                ubah_data1 = int(input(f'Masukkan {ubah_data} baru : '))
                                            elif ubah_data == '2':
                                                ubah_data = 'Nama'
                                                ubah_data1 = input(f'Masukkan {ubah_data} baru : ').title()
                                            elif ubah_data == '3':
                                                ubah_data = 'Jenis Kelamin'
                                                ubah_data1 = input(f'Masukkan {ubah_data} baru : ').title()
                                            elif ubah_data == '4':
                                                ubah_data = 'Umur'
                                                ubah_data1 = int(input(f'Masukkan {ubah_data} baru : '))
                                            else:
                                                ubah_data = 'Diagnosis'
                                                ubah_data1 = input(f'Masukkan {ubah_data} baru : ').title()
                                            
                                            while True:
                                                new_data = input('''
                                                Apakah data yang anda masukkan sudah benar (Y/T) : ''').upper()
                                                if new_data == 'Y':
                                                    data_pasien[i][ubah_data] = ubah_data1
                                                    daftar_pasien()
                                                    print('\n\t---- Data baru anda sudah tersimpan ----')
                                                    change_pasien()
                                                elif new_data == 'T':
                                                    print('\n\t***Anda tidak jadi menambahkan data***')
                                                    change_pasien()
                                                else:
                                                    print(''' \n
                                                    *** Pilihan yang anda masukkan salah *** \n
                                                    ------------------------------------------                     
                                                    Silahkan masukkan pilihan (Y/T) \n''')
                                        else:
                                            print("\n*** Anda memasukkan pilihan yang salah ***")
                                elif new_data == 'T':
                                    change_pasien()
                                else:
                                    print(''' \n
                                    *** Pilihan yang anda masukkan salah *** \n
                                    ------------------------------------------                     
                                    Silahkan masukkan pilihan (Y/T) \n''')
                        elif i == len(data_pasien) - 1:
                            print('\n *** Maaf No Pasien yang anda masukkan salah***')
                else:
                    print("\n***Nomor Pasien harus berupa angka, silahkan ketikkan Nomor Pasien yang benar***\n")           
        elif update_data == '2':
            menu_awal()
        else:
            print(' *** Pilihan yang anda masukkan salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-2] ')

# Delete data pasien
def del_pasien():
    while True:
        del_data = input('''
 +======================================+
 |       Menu Hapus Data Pasien         |
 +======================================+
 |                                      |
 | 1. Hapus data pasien                 | 
 | 2. Kembali ke menu utama             |
 +--------------------------------------+   
Silahkan pilih daftar di atas [1-2] : ''')
        if del_data == '1':
            daftar_pasien()
            input_nop = input('\nMasukkan Nomor Pasien : ')
            if input_nop.isnumeric():
                input_nop = int(input_nop)
                for i in range(len(data_pasien)):
                    if input_nop == data_pasien[i]['No Pasien']:
                        print("-------------------------------------------------------------------------------------------")
                        print("| No  |    No Pasien   |        Nama        |   Jenis Kelamin    |   Umur  |   Diagnosis  |")
                        print("+-----+----------------+--------------------+--------------------+----------+-------------+")
                        print(f'''{i+1:^5}|{data_pasien[i]['No Pasien']:^16}| {data_pasien[i]['Nama']:20}|{data_pasien[i]['Jenis Kelamin']:20}|{data_pasien[i]['Umur']:10}|{data_pasien[i]['Diagnosis']:13}''')
                        print("|-----+----------------+--------------------+--------------------+----------+-------------|")
                        while True:
                            new_data = input('''Apakah data yang anda masukkan sudah benar(Y/T) :  ''').capitalize()
                            if new_data == 'Y':
                                del data_pasien[i]
                                daftar_pasien()
                                print('\t----Data Pasien berhasil di hapus ----')
                                del_pasien()
                            elif new_data == 'T':
                                del_pasien()
                            else:
                                print('''\n
                                    *** Pilihan yang anda masukkan salah *** \n
                                    ------------------------------------------                     
                                    Silahkan masukkan pilihan benar (Y/T) \n''')
                        break
                    elif i == len(data_pasien) - 1:
                        print('\n*** Data yang anda masukkan tidak terdaftar ***')
                        del_pasien()
            else:
                print("\n***Nomor Pasien harus berupa angka, silahkan ketikkan Nomor Pasien yang benar***\n")
        elif del_data == '2':
            menu_awal()
        else:
            print(' \n*** Pilihan yang anda masukkan salah ***\nMohon masukkan pilihan sesuai dengan menu di atas [1-2] ')

# Menampilkan Menu Awal 
def menu_awal():
    print('''
 +=================================================+
 |           Data Pasien RS. Purwadika             |
 +=================================================+           
 
 Berikut daftar pilihan menu yang dapat anda gunakan
 ---------------------------------------------------
    1. Melihat Daftar Pasien
    2. Menambahkan Data Pasien
    3. Mengubah Data Pasien
    4. Menghapus Data Pasien
    5. Keluar dari program''')

    while True:
        daftar_menu = input('\n Silahkan pilih daftar yang di atas [1-5] : ')
        if daftar_menu == '1':
            report_pasien()
        elif daftar_menu == '2':
            add_pasien()
        elif daftar_menu == '3':
            change_pasien()
        elif daftar_menu == '4':
            del_pasien()
        elif daftar_menu == '5':
            print('''\n--- Terima kasih telah menggunakan program data pasien RS. Purwadika ---\n\n''')
            break
        else:
            print("\n*** Maaf yang anda masukkan salah, mohon masukkan sesuai dengan menu di atas [1-5] ***")

# run the program
menu_awal()