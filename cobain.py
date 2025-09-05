piket_hari_ini= ['azuka', 'rezad', 'vannn', ]
print("jadwal pket hari ini:")
for nama in piket_hari_ini:
    print(f"- {nama}")

print("-------------------------")
rukun_islam = ['syahadat', 'shalat', 'zakat', 'puasa', 'haji']
print("rukun islam:")
for index in range (len(rukun_islam)):
    print(f"{index + 1}. {rukun_islam[index]}")



print("----------------------------")
kitab_pelajaran = ['aqidahtuna', 'fathul aly', 'nabiyyuna']
print("kitab pelajaran:")
for kitab in kitab_pelajaran:
    print(f"{kitab}")

print("---------------------------------")
biodata = {'nama':'moch.ridh syawaludien',
           'kelas':' x-c', 
           'hafalan_juz':' 14juz'}
print("biodata santri:")
for key, value in biodata.items():
    print(f"{key}:,{value}")