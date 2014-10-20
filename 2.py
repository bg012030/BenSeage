score1 = int(input ("請輸入第一個成績\n"))
score2 = int(input ("請輸入第二個成績\n"))
score3 = int(input ("請輸入第三個成績\n"))
list1 = [score1,score2,score3]
list1.sort()
list1[0] = int(list1[0]) * 0.2
list1[1] = int(list1[1]) * 0.3
list1[2] = int(list1[2]) * 0.5
print ("期末成績為" , list1[0]+list1[1]+list1[2])