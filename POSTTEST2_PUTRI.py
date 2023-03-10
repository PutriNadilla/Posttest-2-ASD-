def Jump_Searching( list_array , x , n ):
    langkah = n**(1/2)
    prev = 0
    for y in range(len(list_array)):
        if type(list_array[y]) == list:  
            output1 = Jump_Searching(list_array[int(y)],x,len(list_array[int(y)]))
            if output1 == -1:
                list_array[int(y)] = 'z'
            else:
                print(x,"ada di indeks",int(y),"kolom ",output1)
                exit()
    while list_array[int(min(langkah, n)-1)] < x:
                prev = langkah
                langkah += n**(1/2)
                if prev >= n:
                    return -1
    while list_array[int(prev)] < x:        
                prev += 1
                if prev == min(langkah, n):
                    return -1
    if list_array[int(prev)] == x:
            return int(prev)
    return -1
def Linear_Search(arr,x):
    for j in range(len(arr)):
        if type(arr[j]) == list:
            hasil_x = Linear_Search(arr[j],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {j} kolom {hasil_x}')
                exit()
        elif arr[j] == x:
            return j
    return -1

list_NAMA = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
panjanglist = len(list_NAMA)
while True:
    print(f'''
Daftar ASLAB
-------------
|No | Nama  |
-------------
| 1 Arsel   |
| 2 Avivah  |
| 3 Daiva   |
| 4 Wahyu   |
| 5 Wibi    |
-------------
''')
    print('''
    ----------------------
    | 1. Linear Search   |
    | 2. Jump Search     |
    ----------------------
    ''')
    p1 = int(input("Masukan pilihan search yang ingin anda gunakan : "))
    input_nama = input("Masukan nama ASLAB yang ingin dicari indeksnya : ")
    if p1 == 1:
        search_linear = Linear_Search(list_NAMA,input_nama)
        if search_linear == -1:
            print(input_nama," tidak ditemukan")
        else:
            print(input_nama," ditemukan di indeks ",search_linear)
        exit()
    elif p1 == 2:
        search_fib = Jump_Searching(list_NAMA,input_nama,panjanglist)
        if search_fib == -1:
            print(input_nama," tidak ditemukan")
        else:
            print(input_nama," ditemukan di indeks ",search_fib)
        exit()

    else:
        print("Input Yang Anda Masukan Salah Atau Tidak Ada")