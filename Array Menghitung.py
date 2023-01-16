#Deklarasi Array
array = []
#Membuat Variable Total
total=0
#membuat variable n untuk menampung jumlah array
#n jumlah elemen
n = int(input("Masukan Jumlah Elemen :"))
for x in range(n):
    #input nilai
    nilai= float(input("Masukan Nilai ke-{}:".format(x+1)))
    array.append(nilai)
    print("\nHasil Total Adalah : {}".format(sum(array)))
    print("Hasil Rata-Rata Nilai Adalah : {}".format(sum(array)/n))