import sports

#main switch board
def main():
    print('Welcome to the Sports Statistics Program!')
    print('')
    print('What sport would you like scores for? (type number)')
    print('1. Football\n2. Soccer\n3. Basketball\n4. Baseball\n5. Hockey\n6. Tennis\n7. Rugby-League\n8. Volleyball\n9. Cricket\n10. Handball\n11. Rugby-Union')
    sport = int(input('> ')) 
    get_scores(sport)


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

        
    
    
    for score in scores:
        print(score)

if __name__ == '__main__':
    main()

