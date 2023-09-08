def win_team(team1,team2):
    if team1>team2:
        return 1
    elif team1==team2:
        return 2
    else:
        return 3
    
iran_win=spain_win=portugal_win=morocco_win=int(0)
iran_loss=spain_loss=portugal_loss=morocco_loss=int(0)
iran_drow=spain_drow=portugal_drow=morocco_drow=int(0)
iran_difference=spain_difference=portugal_difference=morocco_difference=int(0)
iran_goal_plus=spain_goal_plus=portugal_goal_plus=morocco_goal_plus=int(0)
iran_goal_less=spain_goal_less=portugal_goal_less=morocco_goal_less=int(0)

game0=input().split('-')
iran_goal=int(game0[0])
spain_goal=int(game0[1])
result=win_team(iran_goal,spain_goal)
iran_goal_plus+=iran_goal
iran_goal_less+=spain_goal
spain_goal_plus+=spain_goal
spain_goal_less+=iran_goal
if result==1:
    iran_win+=1
    spain_loss+=1
elif result==2:
    iran_drow+=1
    spain_drow+=1
elif result==3:
    iran_loss+=1
    spain_win+=1

game1=input().split('-')
iran_goal=int(game1[0])
portugal_goal=int(game1[1])
result=win_team(iran_goal,portugal_goal)
iran_goal_plus+=iran_goal
iran_goal_less+=portugal_goal
portugal_goal_plus+=portugal_goal
portugal_goal_less+=iran_goal
if result==1:
    iran_win+=1
    portugal_loss+=1
elif result==2:
    iran_drow+=1
    portugal_drow+=1
elif result==3:
    iran_loss+=1
    portugal_loss+=1

game2=input().split('-')
iran_goal=int(game2[0])
morocco_goal=int(game2[1])
result=win_team(iran_goal,morocco_goal)
iran_goal_plus+=iran_goal
iran_goal_less+=morocco_goal
morocco_goal_plus+=morocco_goal
morocco_goal_less+=iran_goal
if result==1:
    iran_win+=1
    morocco_loss+=1
elif result==2:
    iran_drow+=1
    morocco_drow+=1
elif result==3:
    iran_loss+=1
    morocco_win+=1

game3=input().split('-')
spain_goal=int(game3[0])
portugal_goal=int(game3[1])
result=win_team(spain_goal,portugal_goal)
spain_goal_plus+=spain_goal
spain_goal_less+=portugal_goal
portugal_goal_plus+=portugal_goal
portugal_goal_less+=spain_goal
if result==1:
    spain_win+=1
    portugal_loss+=1
elif result==2:
    spain_drow+=1
    portugal_drow+=1
elif result==3:
    spain_loss+=1
    portugal_win+=1

game4=input().split('-')
spain_goal=int(game4[0])
morocco_goal=int(game4[1])
result=win_team(spain_goal,morocco_goal)
spain_goal_plus+=spain_goal
spain_goal_less+=morocco_goal
morocco_goal_plus+=morocco_goal
morocco_goal_less+=spain_goal
if result==1:
    spain_win+=1
    morocco_loss+=1
elif result==2:
    spain_drow+=1
    morocco_drow+=1
elif result==3:
    spain_loss+=1
    morocco_win+=1

game5=input().split('-')
portugal_goal=int(game5[0])
morocco_goal=int(game5[1])
result=win_team(portugal_goal,morocco_goal)
portugal_goal_plus+=portugal_goal
portugal_goal_less+=morocco_goal
morocco_goal_plus+=morocco_goal
morocco_goal_less+=portugal_goal
if result==1:
    portugal_win+=1
    morocco_loss+=1
elif result==2:
    portugal_drow+=1
    morocco_drow+=1
elif result==3:
    portugal_loss+=1
    morocco_win+=1
#score
iran_score=(int(iran_win)*3)+(int(iran_drow)*1)
spain_score=(int(spain_win)*3)+(int(spain_drow)*1)
portugal_score=(int(portugal_win)*3)+(int(portugal_drow)*1)
morocco_score=(int(morocco_win)*3)+(int(morocco_drow)*1)
#difrence
iran_difference=iran_goal_plus-iran_goal_less
spain_difference=spain_goal_plus-spain_goal_less
portugal_difference=portugal_goal_plus-portugal_goal_less
morocco_difference=morocco_goal_plus-morocco_goal_less

#sort
all_team=[
    ('Iran',iran_win,iran_loss,iran_drow,iran_difference,iran_score),
    ('Spain',spain_win,spain_loss,spain_drow,spain_difference,spain_score),
    ('Portugal',portugal_win,portugal_loss,portugal_drow,portugal_difference,portugal_score),
    ('Morocco',morocco_win,morocco_loss,morocco_drow,morocco_difference,morocco_score)
]
all_team_sort=sorted(all_team , key=lambda x:(-x[5],-x[1],x[0]))

#output
for i in all_team_sort:
    print(str(f"{i[0]}  wins:{i[1]} , loses:{i[2]} , draws:{i[3]} , goal difference:{i[4]} , points:{i[5]}"))
    