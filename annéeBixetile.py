import os
annee = input("une année : ")
annee = int(annee)

if annee%4 == 0 or annee%400 == 0:
	 print("bixetile")
else:
	print("pas bixetile")
os.system ("pause")
