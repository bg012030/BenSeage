s = int(input("請輸入數字[1-100]\n"))
n = int(input("請輸入參加人數\n"))
list1 = []
list2 = []
for w in range(0,n):
  a = input("請輸入第%s位的「稱號 數字」\n" % (w+1))
  list1.extend( a.split(" "))
  list2.append( abs(int(list1[w*2+1]) - s) )

print ("==========================")
for w in range(0,n):
  if int(list2[w]) == sorted(list2)[n-1]:
    print (list1[w*2] , "要喝金盃拉茶")