#Tinh tổng n số chẵn,lẻ đầu tiên
n= int(input("Nhập vào số số đầu tiên : "))
tongchan=0
tongle=0
for i in range (1,n+1):
    tongchan += i*2
    tongle +=i*2-1
print("Tổng các số chẵn: ",tongchan)
print("Tổng các số lẻ: ",tongle)
