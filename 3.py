s = int(input("請輸入數字[1-100]\n"))
n = int(input("請輸入參加人數\n"))
i = 0
list1 = []
list2 = []
while i < n:
  list1.append(input("請輸入'稱號 數字'\n"))
  i = i + 1
  
str(list1)

for w in list1:
  list2.append(abs(int(w[3:]) - s))

w = 0
while w < n:
  if int(list2[w]) == sorted(list2, reverse=True)[0]:
     name = list1[w][0:2]
  w = w + 1

print ("=================")
print (name , "要喝金盃拉茶")