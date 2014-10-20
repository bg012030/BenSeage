score = [] ; score2 = [0.2,0.3,0.5]
for w in range(1,4):
  score.append(int(input("請輸入第%s個成績\n" % (w))))
score.sort()
for w in range(0,3):
  score[w] = int(score[w]) * score2[w]
print ("期末成績為", score[0]+score[1]+score[2])