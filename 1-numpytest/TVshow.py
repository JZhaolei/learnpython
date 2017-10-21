import numpy.random as random
random.seed(42)

n_tests = 10000 #1000次实验
winning_doors = random.randint(0,3,n_tests) #0表示第一扇门，1表示2，2表示3,生成每次奖品所在门的编号
change_mind_wins = 0 #记录改变主意中奖次数
insist_wins = 0 # 记录坚持中奖次数

for winning_door in winning_doors: #winning_door就是获胜门所在的编号
      first_try = random.randint(0,3) #第一次随便选了一扇门
      remaining_choices = [i for i in range(3) if i != first_try]#其他门编号
      wrong_choices = [i for i in range(3) if i != winning_door]#没有奖品的门编号
      if first_try in wrong_choices:
              wrong_choices.remove(first_try)
 #如果一开始选的是错的，那么主持人只能选另一扇错的，所以需要在主持人能选的门中把选手选的错误门去掉
      screened_out = random.choice(wrong_choices)#被揭晓的空门,但如果一开始选对了，那么这时主持人随便开一扇门
      remaining_choices.remove(screened_out)#从剩余门中去掉揭晓的门，此时剩余的是正确的门
      
      changed_mind_try = remaining_choices[0]#选手改变主意时的选择
      
      change_mind_wins +=1 if changed_mind_try == winning_door else 0
      #若改变主意是对的就给改变主意获胜次数加一
      insist_wins +=1 if first_try == winning_door else 0
      #若他之前是对的就给坚持获胜的次数加一

#打印结果
print(
      'You win {1} out of {0} tests if you changed your mind\n'
      'You win {2} out of {0} tests if you insist on the initial choices'.format(
                           n_tests, change_mind_wins, insist_wins
                           )
)
      

