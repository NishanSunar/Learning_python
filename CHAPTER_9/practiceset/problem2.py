import random
def game():
    print("YOu are playing a game..")
    score = random.randint(1,100)
    print(f"Your score: {score}")
    
    
    with open("CHAPTER_9/practiceset/highscore.txt") as hi:
        hiscore = hi.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    if(score>hiscore or hiscore==""):
        
        with open("CHAPTER_9/practiceset/highscore.txt","w") as f:
            f.write(str(score))
        
        
    return score


game()