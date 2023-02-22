import os.path

#Variabel directory untuk filie baru
save_path = 'C:\Users\ASUS\Documents\Semester 6\Sistem Tersebar\Python-Pararel_SISTER\Chapter01'

f = open ('test.txt', 'w')
f.write ('first line of file \n') 

f.write ('second line of file \n') 

f.close()

f = open ('test.txt')
content = f.read()
print (content)

f.close()

print("\n ### Membuat sendiri File Handling dalam Python ### \n")

direktori = os.path.join(save_path, "testNew"+".txt")

filePertama = open(direktori, "w")

filePertama.write('Ini adalah percobaan pembuatan file dalam python')

filePertama.close()

print("\n ### Isi dari File terbaru ### \n")

# Mencetak isi dari file baru
filePertama = open ('Chapter01/testNew.txt')
content = filePertama.read()
print (content)

filePertama.close()