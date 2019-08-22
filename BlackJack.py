import random

class Human:
    def __init__(self, deposit,cards):
        self.deposit=deposit
        self.cards=cards
        self.cards_sum = cards[0].value+cards[1].value
        self.bet=  0
        
        
    def lose(self):
        self.deposit-=self.bet
        print(f'You lose {self.bet}$')
    def win(self):
        self.deposit+=self.bet
        print(f'You won {self.bet}$')
    def print_cards(self):
        print(f"Player's BET: {self.bet}$")
        print("PLAYER'S CARDS")
        for card in self.cards:
            print(card.name)
        print(f"Player's SUM: {self.cards_sum}")
            
    def make_bet(self):
        while True:
            try:
                self.bet=int(input('Make a BET'))
                if self.bet>self.deposit:
                    print('not enough money!')
                else:
                    break
            except:
                print('Wrong input!!!')
            
                
    def card_add(self,card):
        self.cards.append(card)
        self.cards_sum+=card.value
        if self.cards_sum>21:
            for item in self.cards:
                if item.name == "Ace":
                    item.name ="small ace"
                    item.value-=10
                    self.cards_sum-=10
                    break
            else:
                print('HA!HA! LOOOSER!!')
                self.lose()
                return "player_lost"
        else:
            return "player_continue"
        
        
    def ask_player(self,deck):
        
        while True:
            choice = input("Do you wanna draw a card?/n Input 'yes' or 'no'")
            if choice == "yes":
                end_game = self.card_add(deck.pop_card())
                break
            elif choice == "no":
                end_game="player_stop"
                break
            else:
                print('Wrong input')
        return end_game
                
            
                
        
    
class Card():
    def __init__(self, name, value):
        self.name=name
        self.value=value
    def __str__(self):
        return self.name



class Deck():
    def __init__(self):
        self.cards = [Card(name = "Ace",value = 11), Card(name = "King",value = 10),
                      Card(name = "Queen",value = 10), Card(name = "Jack",value = 10),
                      Card(name = "10",value = 10), Card(name = "9",value = 9),
                      Card(name = "8",value = 8), Card(name = "7",value = 7),
                      Card(name = "6",value = 6), Card(name = "5",value = 5),
                      Card(name = "4",value = 4), Card(name = "3",value = 3),
                      Card(name = "2",value = 2)]*4
        self.count=52
    def shuffle(self):
        random.shuffle(self.cards)
    
    def pop_card(self):
        
        result = self.cards[-1]
        del self.cards[-1]
        return result
    
class Dealer():
    def __init__(self, cards):        
        self.cards=cards
        self.cards_sum = cards[0].value+cards[1].value
    
    def print_cards(self):
        print("DEALER'S CARDS")
        for card in self.cards:            
            print(card.name)
        print(f"DEALER'S SUM:{self.cards_sum}")
            
        
    def card_add(self,card,player):
        self.cards.append(card)
        self.cards_sum+=card.value
        if self.cards_sum>21:
            for item in self.cards:
                if item.name == "Ace":
                    item.name ="small ace"
                    item.value-=10
                    self.cards_sum-=10
                    break
            else:
                player.win()
                return "dealer_lost"
        if self.cards_sum>player.cards_sum:
            print('SER, BbI Bce npourpaJIu')
            player.lose()
            return "player_lost"
            #tyt end'
        elif self.cards_sum == player.cards_sum:
            
            print('Seems like Dead Heat') 
            return "dealer_lost"
            #vernut        
        else:
            return "dealer_continue"
def print_table():
    print("------------------------------------------------------------------------------------")
    print(f"Your deposit is:{Player.deposit}")
    
    MyDealer.print_cards()
    Player.print_cards()
    print("------------------------------------------------------------------------------------")
    
    
    
          
    
while True:
        try:
            money = (int(input('HOW MUCH MONEY YOU GOT? ')))
            print(f"okey, here is your {money}$")
            break

        except:
            print("wrong input! Try Again..")
answer="yes"    
    
while answer=="yes":
    
    print("------------------------------------------------------------------------------------")
    MyDeck = Deck()
    MyDeck.shuffle()
    Player = Human(money,[MyDeck.pop_card(),MyDeck.pop_card()])
    Player.make_bet()
    end_game="player_continue"

    MyDealer = Dealer([MyDeck.pop_card(),MyDeck.pop_card()])
    
    print_table()
    while end_game!="player_lost" and end_game!="player_stop" :

        end_game = Player.ask_player(MyDeck)
        print_table()

    while end_game!= "player_lost" and end_game!="dealer_lost":
        end_game = MyDealer.card_add(MyDeck.pop_card(),Player)
    print_table()
    money = Player.deposit
    while True:                
        if Player.deposit==0:
            answer="no"
            print("YOU LOST ALL YOUR MONEY")
            break
        answer=input("DO YOU WANNA PLAY AGAIN?\nInput'yes' or 'no'")
        if answer=="yes" or answer=="no":
            break
        else:
            print("wrong input")