import sports

#main switch board
def main():
    print('Welcome to the Sports Statistics Program!\n')
    print('I can provide you with all types of scores!\n')
    print('What sport would you like scores for? (type number)\n')
    print('1. Football\n2. Soccer\n3. Basketball\n4. Baseball\n5. Hockey\n6. Tennis\n7. Rugby-League\n8. Volleyball\n9. Cricket\n10. Handball\n11. Rugby-Union\n 12. Type in Team \n')
    sport = input('Q for quit or a number: ')
    
    while True:
        if sport.isdigit():
            sport = int(sport)
        if sport == "Q":
            print('Thanks for using the Sports Statistics Program.')
            break
        else:
            get_scores(sport)
            sport = str(input('Q for quit or another number: ')) 

def get_scores(sport):
    if sport == 1:
        scores = sports.get_sport(sports.FOOTBALL)
    
    elif sport == 2:
        scores = sports.get_sport(sports.SOCCER)
    elif sport == 3:
        scores = sports.get_sport(sports.BASKETBALL)
    elif sport == 4:
        scores = sports.get_sport(sports.BASEBALL)
    elif sport == 5:
        scores = sports.get_sport(sports.HOCKEY)
    elif sport == 6:
        scores = sports.get_sport(sports.TENNIS)
    elif sport == 7:
        scores = sports.get_sport(sports.RUGBY_L)
    elif sport == 8:
        scores = sports.get_sport(sports.VOLLEYBALL)
    elif sport == 9:
        scores = sports.get_sport(sports.CRICKET)
    elif sport == 10:
        scores = sports.get_sport(sports.HANDBALL)
    elif sport == 11:
        scores = sports.get_sport(sports.RUGBY_U)
    elif sport == 12:  # this is for specific teams
        team_name = str(input("Type the name of the baseball team"))
        team_data = sports.get_team("baseball", team_name)
    elif sport == 13:  # this is for specific teams
        team_name = str(input("Type the name of the football team"))
        team_data = sports.get_team("football", team_name)
    elif sport == 14:  # this is for specific teams
        team_name = str(input("Type the name of the hockey team"))
        team_data = sports.get_team("hockey", team_name)
    elif sport == 15:  # this is for specific teams
        team_name = str(input("Type the name of the basketball team"))
        team_data = sports.get_team("basketball", team_name)

    if sport < 12:  # if it is just a sport     
        for score in scores:
            print(score)
    else: 
        print(team_data)        

if __name__ == '__main__':
    main()

