import psycopg2

conn = psycopg2.connect(
    database='pawtopia',
    user ='postgres',
    password='310304',
    host ='localhost',
    port=5432,
)

cur = conn.cursor()

#menampilkan product foods
def read_product_food():
    query = 'select p.nama_produk, p.harga_produk, p.stock, p.deskripsi ,k.nama_kategori from produk p join kategori k on p.id_kategori = k.id_kategori where p.id_kategori = 1 order by harga_produk'
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)

    cur.close()
    conn.close()

#menampilkan product acessoriess
def read_product_acessories():
    query = 'select p.nama_produk, p.harga_produk, p.stock, p.deskripsi ,k.nama_kategori from produk p join kategori k on p.id_kategori = k.id_kategori where p.id_kategori = 2 order by harga_produk'
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)

    cur.close()
    conn.close()

#create product
def create_produk():
    nama_produk = input('nama produk : ')
    harga_Produk = float(input('harga       : '))
    stock = int(input("stok produk  : "))
    deskripsi = input("deskripsi produk   : ")
    print (F'katrgori:\n1. Foods \n2. Acessoriess')
    id_kategori = int(input('pilih kategori : '))
    query = 'insert into produk(nama_produk, harga_produk, stock, deskripsi, id_kategori) values( %s, %s, %s, %s, %s)'
    cur.execute(query, vars=(nama_produk, harga_Produk, stock, deskripsi, id_kategori))
    conn.commit()
    cur.close()
    conn.close()

#delete product
def delete_produk():
    id_produk = (input('id product yang akan dihapus : '))
    query = (f'delete from produk where id_produk = {id_produk}')
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

#update product
def update_produk():
    produk_update = input('masukan nama product yang akan di update:  ')

    print ('\n1. Nama_produk')
    print ('2. Harga')
    print ('3. Stok')
    print ('4. Deskripsi')
    print ('5. Kategori')
    kolom = int(input('maasukan bagian yang ingin diubah: '))

    match kolom :
        case 1:
            nama_produk = input ('nama baru: ')
            query= (f"update produk set nama_produk = '{nama_produk}' where nama_produk = '{produk_update}'")
            cur.execute(query)
        case 2:
            harga_produk = float(input ('harga baru: '))
            query= (f"update produk set harga_produk = '{harga_produk}' where nama_produk = '{produk_update}'")
            cur.execute(query)
        case 3:
            stock = int(input ('stock baru: '))
            query= (f"update produk set stock = '{stock}' where nama_produk = '{produk_update}'")
            cur.execute(query)
        case 4:
            deskripsi = input ('deskripsi baru: ')
            query= (f"update produk set deskripsi = '{deskripsi}' where nama_produk = '{produk_update}'")
            cur.execute(query)
        case 5:
            print ('1. Foods')
            print ('2. Acessories')
            kategori = int(input ('kategori baru (angka): '))
            query= (f"update produk set id_kategori = '{kategori}' where nama_produk = '{produk_update}'")
            cur.execute(query)

    conn.commit()
    cur.close()
    conn.close()

# update_produk()
read_product_acessories()