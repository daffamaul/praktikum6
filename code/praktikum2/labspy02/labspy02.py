# mengurutkan data
a = input("masukkan nilai a = ")
b = input("masukkan nilai b = ")
c = input("masukkan nilai c = ")

if a > b:
	if a > c:
		maks = a
		print("nilai terbesar = ",a)
elif b > c:
		maks = b
		print("nilai terbesar = ", b)
else:
	print("nilai terbesar = ",c)
