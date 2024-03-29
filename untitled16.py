# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GyEU3xf4D17DK3TDuW5QgttvfO2IsHdu
"""

import numpy as np

#每個酒類品項的酒精重量(g)
beer_w=[14, 36, 43.75 , 12]
beer_w=[i*0.8 for i in beer_w]
beer_w

# bw_g=0.49
# bw_b=0.58
# weight=[73,48,48,88,73.5,63,69,75]
# sd=[1.4,3,6.25,1.2] #10G
# sd_new=[i*0.789 for i in sd]
# mr_g=0.017
# mr_b=0.015
# ebac=[]


# for i in range(8):
#   alcohol=[]
#   for j in range(len(sd_new)):
#     if i == 1 or 2:
#       z=(0.806*sd_new[j]*1.2)/(bw_g*weight[i])-mr_g*d[0]*(1/60) #d[0]:飲酒後時間[小時]
#     else:
#       z=(0.806*sd_new[j]*1.2)/(bw_b*weight[i])-mr_b*d[0]*(1/60)
#     alcohol.append(z)
#   ebac.append(alcohol)
# ebac

# 分組 (0,4)(1,5)(2,6)(3,7)
def divide_group():
  s1=[0,1,2,3]
  s2=[4,5,6,7]
  team1=[]
  team2=[]
  for i in range(4):
    p=np.random.uniform(0,1)

    if p<0.5:
      team1.append(s1[i])
      team2.append(s2[i])
    else:
      team1.append(s2[i])
      team2.append(s1[i])

  return(team1, team2)

def select_beer():
  beer=[0,1,2,3]
  p=np.random.uniform(0,1)
  if 0<p<=0.25:
    return beer[0]
  elif 0.25<p<=0.5:
    return beer[1]
  elif 0.5<p<=0.75:
    return beer[2]
  else:
    return beer[3]

#每場比賽選人
def select_people(team1, team2, player_combination1, player_combination2, store, non_drop1, non_drop2):
  if len(non_drop1)==1 and len(non_drop2)==1:
    player=[]
    player.append(non_drop1[0])
    player.append(non_drop2[0])
  elif len(non_drop1)==1 and len(non_drop2)!=1:
    player=[non_drop1[0], player_combination2[-1]]
    while player[1]==player_combination2[-1]:
      p2=np.random.uniform(0,1)
      player[1]= prob_decide_player(non_drop2, p2, team2)
  elif len(non_drop1)!=1 and len(non_drop2)==1:
    player=[player_combination1[-1]]
    while player[0]==player_combination1[-1]:
      p1=np.random.uniform(0,1)
      player[0]= prob_decide_player(non_drop1, p1, team1)
    player.append(non_drop2[0])
  else:
    if store==0:
      player=[]
      p1=np.random.uniform(0,1)
      p2=np.random.uniform(0,1)
      prob=[p1, p2]
      team=[team1, team2]
      player=[prob_decide_player(non_drop1, p1, team1), prob_decide_player(non_drop2, p2, team2)]

    else:
      player=[player_combination1[-1], player_combination2[-1]]
      while player_combination1[-1]== player[0] or player_combination2[-1]== player[1]:
        #print('eee')
        p1=np.random.uniform(0,1)
        p2=np.random.uniform(0,1)
        prob=[p1, p2]
        team=[team1, team2]
        player=[prob_decide_player(non_drop1, p1, team1), prob_decide_player(non_drop2, p2, team2)]
  return player

def prob_decide_player(non_drop, p, team):
  prob_interval=[0]
  interval= 1/len(non_drop)
  for i in range(len(non_drop)-1):
    prob_interval.append((i+1)*interval)
  prob_interval.append(1)
  #print(prob_interval)

  for i in range(len(prob_interval)-1):
    if prob_interval[i]<p<=prob_interval[i+1]:
      #print('player_idx',i)
      return team[i]

# 代謝率
def meta(player_w, alcohol):
  consumption= alcohol/(player_w* 0.1)*60
  return consumption

bw_g=0.49
bw_b=0.58
weight=[73,48,63,88,73,48,88,63]
sd=[1.4,3,4.375,1.2] #10G
sd_new=[i*0.789 for i in sd]
mr_g=0.017
mr_b=0.015
speed_hr= 4000#(每小時幾公尺)
speed_mi= 4000/60
def ebac_consumption(player, dist, sd_new):
  if player==1 or 2: #選到女生的代謝率
    z=(0.806*sd_new*1.2)/(bw_g*weight[player])-mr_g*dist/speed_hr
  else:              #選到男生的代謝率
    z=(0.806*sd_new*1.2)/(bw_b*weight[player])-mr_b*dist/speed_hr
  return z

#假設: 玩家在每場遊戲中一分鐘內喝完
# def ebac(player, sd_new):
#   if player==1 or 5:
#     z=(0.806*sd_new*1.2)/(bw_g*weight[player])-mr_g
#   else:
#     z=(0.806*sd_new*1.2)/(bw_b*weight[player])-mr_b
#   return z

#每個人喝醉和喝吐的beta
def decide_param():
  drunk_param_temp=[]
  throw_param_temp=[]
  for i in range(4):
    a1= np.random.uniform(0.06, 0.09)
    a2= np.random.uniform(0.1, 0.299)
    for j in range(2):
      drunk_param_temp.append(a1)
      throw_param_temp.append(a2)
  drunk_param_temp.sort()
  throw_param_temp.sort()
  drunk_param=[drunk_param_temp[4],drunk_param_temp[0],drunk_param_temp[2],drunk_param_temp[6],drunk_param_temp[5],drunk_param_temp[1],drunk_param_temp[3],drunk_param_temp[7]]
  throw_param=[throw_param_temp[4],throw_param_temp[0],throw_param_temp[2],throw_param_temp[6],throw_param_temp[5],throw_param_temp[1],throw_param_temp[3],throw_param_temp[7]]
  return (drunk_param, throw_param)

bw_g=0.49
bw_b=0.58
weight=[73,48,48,88,73.5,63,69,75]
sd=[1.4,3,4.375,1.2] #10G
sd_new=[i*0.789 for i in sd]
mr_g=0.017
mr_b=0.015
speed= 4000#(每小時幾公尺) #人走路速度

def ebac_matrix(dist):
  ebac=[]
  for i in range(8):
    alcohol=[]
    for j in range(len(sd_new)):
      if i == 1 or 5:
        z=(0.806*sd_new[j]*1.2)/(bw_g*weight[i])-mr_g*dist/speed

      else:
        z=(0.806*sd_new[j]*1.2)/(bw_b*weight[i])-mr_b*dist/speed


      alcohol.append(z)
    ebac.append(alcohol)
  return(ebac)

# simulation
import math
#血液中的酒精濃度達0.08%以上為醉酒
#血液中的酒精濃度達0.1%~0.299%會出現嘔吐現象
#血液中的酒精濃度達0.299%以上會出現昏迷和死亡的風險
#用ebac算是否醉酒
#d=[]
#team1=[0,5,6,3]
#team2=[4,1,2,7]
def simulation(team1, team2, min):
  time=0
  beer_l=[]
  #team1, team2=divide_group()
  non_drop1=team1
  non_drop2=team2
  i=0

  player_combination1, player_combination2= [],[]
  player_ebac=[0,0,0,0,0,0,0,0]
  player_ebac_list=[[0],[0],[0],[0],[0],[0],[0],[0]]
  #variable

  d=[math.ceil(np.random.exponential(min))]
  for di in range(100):
    z=math.ceil(np.random.exponential(min)) #每一間的時間

    d.append(z)
  print('dist',d)
  while True and i<100 :
    if i>1:
      for m in range(len(team1)):
        for mm in range(len(player_combination1)-1,-1,-1):
          if player_combination1[-mm]==team1[m]:
            if player_ebac[team1[m]]- ebac_consumption(team1[m], 1, sd_new[beer_l[mm]])>=0:
              player_ebac[team1[m]]=  player_ebac[team1[m]]- ebac_consumption(team1[m], 1, sd_new[beer_l[mm]])
              player_ebac_list[team1[m]].append(player_ebac[team1[m]])
            else:
              player_ebac[team1[m]]=0.06
              player_ebac_list[team1[m]].append(0.06)
            break
      for m in range(len(team2)):
        for mm in range(len(player_combination2)-1,-1,-1):
          if player_combination2[-mm]==team2[m]:
            if player_ebac[team2[m]]- ebac_consumption(team2[m], 1, sd_new[beer_l[mm]])>=0:
              player_ebac[team2[m]]=  player_ebac[team2[m]]- ebac_consumption(team2[m], 1, sd_new[beer_l[mm]])
              player_ebac_list[team2[m]].append(player_ebac[team2[m]])
            else:
              player_ebac[team2[m]]=0.06
              player_ebac_list[team2[m]].append(0.06)
            break
    #print('i',i,'d[i]',round((sum(d[:i+1]))))
    if time==round((sum(d[:i+1]))):

      #print('yes')
      ebac= ebac_matrix(d[i])
      ac_per_store=[]
      player=[9,9]
      # player= select_people(team1, team2)
      beer= select_beer()
      beer_l.append(beer)
      # ac_per_store1= weight[player[0]]*0.1*d[i]/speed
      # ac_per_store2= weight[player[1]]*0.1*d[i]/speed#行走在兩間超商之間的player消耗濃度
      # player_ebac[player[0]]+= ebac[player[0], beer]- ac_per_store1
      # player_ebac[player[1]]+= ebac[player[1], beer]- ac_per_store2
      # player1_meta= np.random.exponential(meta(weight[player[0]],beer_w[beer] ))#player2的代謝率(隨機變數)
      # player2_meta= np.random.exponential(meta(weight[player[1]],beer_w[beer] ))#player1的代謝率(隨機變數)

      # player_drunk1= np.random.exponential(drunk[player[0], beer])
      # player_drunk2= np.random.exponential(drunk[player[1], beer])
      # player_throw1= np.random.exponential(throw[player[0], beer])
      # player_throw2= np.random.exponential(throw[player[1], beer])
      #假設在超商內喝完酒才能走
      #喝醉判斷
      ac_per_store1_temp,ac_per_store2_temp=0,0
      while (player[0]  not in non_drop1) or (player[1] not in non_drop2):
        player= select_people(team1, team2, player_combination1, player_combination2, i, non_drop1, non_drop2)
      player_combination1.append(player[0])

      player_combination2.append(player[1])

      ac_per_store1=ebac_consumption(player[0], d[i], sd_new[beer])
      ac_per_store2=ebac_consumption(player[1], d[i], sd_new[beer])
      # for m in range(len(team1)):
      #   for mm in range(len(player_combination1)-1,-1,-1):
      #     if player_combination1[-mm]==team1[m]:
      #       player_ebac[team1[m]]=  player_ebac[team1[m]]- ebac_consumption(team1[m], d[i], sd_new[beer_l[mm]])
      #       break
      player_ebac[player[0]]+= ebac[player[0]][beer]
      player_ebac[player[1]]+= ebac[player[0]][beer]
      drunk_param, throw_param= decide_param()
      #喝醉判斷
      if ebac[player[0]][beer]<=drunk_param[player[0]] and drunk_param[player[1]]<=ebac[player[1]][beer]<=throw_param[player[1]]:
        if player[1] in non_drop2:
          non_drop2.remove(player[1])#team1 win
          print('team1', player_combination1)
          print('team2', player_combination2)
      if ebac[player[1]][beer]<=drunk_param[player[1]] and drunk_param[player[0]]<=ebac[player[0]][beer]<=throw_param[player[0]]:
        if player[0] in non_drop1:
          non_drop1.remove(player[0])
          win= 'team2' #team2 win
          print('team1', player_combination1)
          print('team2', player_combination2)
      if non_drop1==[] and non_drop2==[]:
        print('fair')
        #print(i)
        break
      #喝吐判斷
      if throw_param[player[0]]<=ebac[player[0]][beer] and ebac[player[1]][beer]<throw_param[player[1]]:
        win= 'team2' #team2 win
        print('team1', player_combination1)
        print('team2', player_combination2)
        #winner=3
        #print(i)
        break #有一對喝到吐即比賽結束
      if throw_param[player[1]]<=ebac[player[1]][beer] and ebac[player[0]][beer]<throw_param[player[0]]:
        win= 'team1' #team1 win
        print('team1', player_combination1)
        print('team2', player_combination2)
        #winner=4
        #print(i)
        break
      d.append(math.ceil(np.random.exponential(min)))
      i+=1
    time+=1
  print(i)
  return ( time, player_ebac_list)#, team1,player_combination1, team2, player_combination2)



# num=10
# def random_search(measurement):

#     time_1=[] #period_cost
#     count=0 #跑num次

#     while time_1==[]:
#       winner, y_best=simulation()
#       if winner==1 or winner==3:
#         time_1.extend(y_best for i in range(num))
#         count+=num
#       else:
#         time_1.extend(y_best for i in range(num))
#         count+=num
#     while(count<measurement):
#         y2, winner=simulation()
#         if (y2>y_best and (winner==1 or winner==3)):
#           y_best=y2
#         count+=num
#         time_1.extend(y_best for i in range(num))



#     return time_1

num=10
def random_search(measurement, min):
    time_1=[] #period_cost

    count=num #跑num次
    team1, team2=divide_group()
    y_best, best_player_ebac=simulation(team1, team2, min)
    time_1.extend(y_best for i in range(num))
    while(count<measurement):
        team1, team2=divide_group()
        y2,player_ebac=simulation(team1, team2, min)
        if (y2>y_best):
          y_best=y2
          best_player_ebac= player_ebac
        count+=num
        time_1.extend(y_best for i in range(num))

    return (time_1, best_player_ebac)

random_search_time5, best_player_ebac5=random_search(10000, 5)

best_player_ebac5

random_search_time10, best_player_ebac10=random_search(10000, 10)

random_search_time15, best_player_ebac15=random_search(10000, 15)

title='ebac'
for j in range(8):
  plt.plot([i for i in range(len(best_player_ebac5[j]))],best_player_ebac5[j])
#plt.legend(['player0','player1','player2','player3','player4','player5','player6','player7'],loc='upper right')
plt.title(title)
plt.xlabel('time(min)')
plt.ylabel('player_ebac')

best_player_ebac5[5]

def pic_ebac(best_player_ebac5, title):

  fig, ax = plt.subplots(2,4, figsize=(20,10))

  ax[0][0].plot([i for i in range(len(best_player_ebac5[0]))],best_player_ebac5[0])
  ax[0][1].plot([i for i in range(len(best_player_ebac5[1]))],best_player_ebac5[1])
  ax[0][2].plot([i for i in range(len(best_player_ebac5[2]))],best_player_ebac5[2])
  ax[0][3].plot([i for i in range(len(best_player_ebac5[3]))],best_player_ebac5[3])
  ax[1][0].plot([i for i in range(len(best_player_ebac5[4]))],best_player_ebac5[4])
  ax[1][1].plot([i for i in range(len(best_player_ebac5[5]))],best_player_ebac5[5])
  ax[1][2].plot([i for i in range(len(best_player_ebac5[6]))],best_player_ebac5[6])
  ax[1][3].plot([i for i in range(len(best_player_ebac5[7]))],best_player_ebac5[7])
  ax[0, 0].set_title("player0")
  ax[0, 1].set_title("player1")
  ax[0, 2].set_title("player2")
  ax[0, 3].set_title("player3")
  ax[1, 0].set_title("player4")
  ax[1, 1].set_title("player5")
  ax[1, 2].set_title("player6")
  ax[1, 3].set_title("player7")

  plt.show()

pic_ebac(best_player_ebac5, 'mu=5')

pic_ebac(best_player_ebac5, 'mu=10')

pic_ebac(best_player_ebac5, 'mu=15')

def pic1(time5, time10, time15, title):
  plt.plot([i for i in range(len(time5))],time5,color='blue')
  plt.plot([i for i in range(len(time10))],time10,color='green')
  plt.plot([i for i in range(len(time15))],time15,color='red')
  plt.legend(['mu=5','mu=10','mu=15'],loc='upper right')
  plt.title(title)
  plt.xlabel('observation')
  plt.ylabel('time')

pic1(random_search_time5,random_search_time10,random_search_time15,'Performance Trajectories (different average)')