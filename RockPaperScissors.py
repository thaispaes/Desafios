def scissors(rp1, rp2):
    
    if(rp1 == 'scissors' and rp2 == 'paper'):
        return "Player 1 won!"
    elif (rp1 == 'paper' and rp2 == 'scissors'):
        return "Player 2 won!"
    elif (rp1 == 'scissors' and rp2 == 'scissors'):
        return "Draw!"
    elif (rp1 == 'scissors' and rp2 == 'rock'):
        return "Player 2 won!"
    elif (rp1 == 'rock' and rp2 == 'scissors'):
        return "Player 1 won!"
            
def paper(rp1, rp2):
    
    if(rp1 == 'paper' and rp2 == 'rock'):
        return "Player 1 won!"
    elif (rp1 == 'rock' and rp2 == 'paper'):
        return "Player 2 won!"
    elif (rp1 == 'paper' and rp2 == 'paper'):
        return "Draw!"
    elif(rp1 == 'scissors' and rp2 == 'paper'):
        return "Player 1 won!"
    elif (rp1 == 'paper' and rp2 == 'scissors'):
        return "Player 2 won!"
            
def rock(rp1, rp2):
    
    if(rp1 == 'rock' and rp2 == 'scissors'):
        return "Player 1 won!"
    elif (rp1 == 'scissors' and rp2 == 'rock'):
        return "Player 2 won!"
    elif (rp1 == 'rock' and rp2 == 'rock'):
        return "Draw!"
    elif(rp1 == 'paper' and rp2 == 'rock'):
        return "Player 1 won!"
    elif (rp1 == 'rock' and rp2 == 'paper'):
        return "Player 2 won!"

def rps(p1, p2):
    if (p1 == 'scissors' or p2 == 'scissors'):
        return scissors(p1, p2)
    elif (p1 == 'paper' or p2 == 'paper'):
        return paper(p1, p2)
    elif (p1 == 'rock' or p2 == 'rock'):
        return rock(p1, p2)
        
        
p1 = input()
p2 = input()
    
rps(p1, p2)
