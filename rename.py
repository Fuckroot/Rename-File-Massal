import os, sys
print(" ~ First Filename ~")
ffdari = raw_input("[+] Dari : ")
ffke = raw_input("[+] Ke : ")
print("")
print(" ~ Last Filename ~")
lfdari = raw_input("[+] Dari : ")
lfke = raw_input("[+] Ke : ")
print("")
print(" ~ Jumlah ~")
jdari = input("[+] Dari : ")
jdari -= 1
jke = input("[+] Ke : ")
print("")
ext = raw_input("[+] Extensi : ")
i = 0
for i in range(jdari, jke):
    i += 1
    os.system("mv "+str(ffdari)+str(i)+str(lfdari)+"."+str(ext)+" "+str(ffke)+str(i)+str(lfke)+"."+str(ext))

os.system("ls")
