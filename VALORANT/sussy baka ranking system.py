# This is just a dumb project to imitate the Valorant ranking system
# This code has more autism than me, and I;m pretty autistic.
import random
import os

def cc():   # shortened this long command to cc()
    os.system("cls" if os.name == "nt" else "clear")
cc()

ranks = [
"iron1", "iron2", "iron3", 
"bronze1", "bronze2", "bronze3", 
"silver1", "silver2", "silver3", 
"gold1", "gold2", "gold3", 
"platinum1", "platinum2", "platinum3", 
"diamond1", "diamond2", "diamond3", 
"immortal1", "immortal2", "immortal3", 
"radiant"]

current_rank = ranks[13]
current_rank_rr = 50

def main():
    global current_rank
    global current_rank_rr
    global ranks
    #team_a = 9 # this is the default team. If team A loses, then RR is taken away
    #team_b = 13


    def random_scores():
        global team_a
        global team_b
        team_win = random.randint(0,1)
        if team_win == 0:
            team_a = 13
            team_b = random.randint(0,11)
        else:
            team_a = random.randint(0,11)
            team_b = 13
    random_scores()

    #team_a = random.randint(0,13)   # does not account for ties! fix this
    #team_b = random.randint(0,13)
    #average_kills = 15 # this wil lbe used for performance bonus RR



    score_diff_win = team_a - team_b
    score_diff_loss = team_b - team_a


    #game_num = 1 # this will be used for placement matches. 
    # after 3 placements you will get your rank

    # there is 100RR in a rank
    # once you hit 100 you get promoted
    # once you hit -1 you get demoted (you can can 0 RR and still stay in the same rank)


    """
    # round difference, then RR gained
    win_rr_gains = (
        (0, 3),
        (1, 15),
        (2, 15),
        (3, 17),
        (4, 17),
        (5, 20),
        (6, 20),
        (7, 20),
        (8, 20),
        (9, 20),
        (10, 20),
        (11, 20),
        (12, 20),
        (13, 20),
    )
        
    for (round_diff, rr) in win_rr_gains:
        if score_diff_win == round_diff:
            current_rank_rr += rr
            print("gained " + str(rr) + "RR")
            
    possible "better" way of doing this rather than 
    the if statements mess below. The if statements
    can account for overtime where many rounds are played,
    but the above list is fixed. In the future the whole
    system should be revamped

    """


    print("Starting rank is " + current_rank)

    #needs a system to carry over rr from previous rank.
    # if you are 90RR iron 1 and gain 20RR, you should be iron 2 with 10RR.
    # right now it just resets to 0 on a promotion

    # Team A wins/ties
    if team_a > team_b or team_a == team_b:
        print("Team A wins!")
        print("The score is " + str(team_a) + " to " + str(team_b))
        print()
        if score_diff_win > 12:
            current_rank_rr += 30
            print("gained 30RR")

        elif score_diff_win > 10:
            current_rank_rr += 26
            print("gained 26RR")

        elif score_diff_win > 8:
            current_rank_rr += 25
            print("gained 25RR")

        elif score_diff_win > 6:
            current_rank_rr += 24
            print("gained 24RR")

        elif score_diff_win > 3:
            current_rank_rr += 23
            print("gained 23RR")

        elif score_diff_win > 0:
            current_rank_rr += 19
            print("gained 19RR")

        elif score_diff_win == 0:
            current_rank_rr += 3
            print("Draw, gained 3RR")

    # Team A loses
    elif team_b > team_a:
        print("Team B wins!")
        print("The score is " + str(team_b) + " to " + str(team_a))
        print()
        if score_diff_loss > 12:
            current_rank_rr += 29
            print("Lost 29RR")

        elif score_diff_loss > 10:
            current_rank_rr -= 25
            print("Lost 25RR")

        elif score_diff_loss > 8:
            current_rank_rr -= 24
            print("Lost 24RR")

        elif score_diff_loss > 6:
            current_rank_rr -= 23
            print("Lost 23RR")

        elif score_diff_loss > 3:
            current_rank_rr -= 20
            print("Lost 20RR")

        elif score_diff_loss > 0:
            current_rank_rr -= 17
            print("Lost 17RR")


    # Promotion
    if current_rank_rr >= 100 and current_rank != ranks[21]: # if you are radiant you cant be promoted
        current_rank = ranks[ranks.index(current_rank) + 1] # promotes your rank
        print("You have been promoted to " + str(current_rank))
        current_rank_rr = 0
        print("Current RR is " + str(current_rank_rr))

    # Demotion
    elif current_rank_rr <= -1 and current_rank != ranks[0]: # if you are iron1 you cant be demoted
        current_rank = ranks[ranks.index(current_rank) - 1]
        print("You have been demoted to " + current_rank)
        current_rank_rr = 90
        print("Current RR is " + str(current_rank_rr))

    # No rank change
    elif current_rank_rr >= 0 and current_rank_rr <= 99 and current_rank != ranks[21]:
        print("Rank not changed")
        print("Current RR is " + str(current_rank_rr))

    elif current_rank == ranks[21]:
        print("You are Radiant")
        print("Current RR is " + str(current_rank_rr))

    replay = input("Play again? ")
    main()


"""
For testing
run = 0
for i in range(1000):
    run += 1
    print(run)
    cc()
    main()"""


main()



