import random
import json
import http.client
import sys
import collections

#UNCOMMENT THIS WHEN READY TO USE API
# sys.path.append('api.py')
# from api import api_token


class LottoSimulation:
    """
    This class' methods simulate the purchasing of tickets and powerball drawing simulation.
    """    
    def __init__(self, ticket_quantity=0, ticket_cost=0, generated_tickets = [], winning_combo = []):
        self.ticket_quantity = ticket_quantity
        self.ticket_cost = ticket_cost
        self.generated_tickets = generated_tickets
        self.winning_combo = winning_combo
        
    def purchase_tickets(self):
        """
        Simulates the ticket purchasing process.
        """
        self.ticket_cost = 2
        self.ticket_quantity = int(input(f"Welcome to Powerball! Each quick pick costs ${self.ticket_cost}. \nHow many tickets would you like to purchase?  "))
        
        print(f"That will cost ${self.ticket_quantity * self.ticket_cost}. Please type how much cash you would like to give, we can make change (dollars only, no coins).  ")
        money_received = int(input("$ "))
        
        while money_received < self.ticket_quantity * self.ticket_cost:
            print(f"Sorry, you don't have enough money. How many tickets would you like to buy? ")
            self.ticket_quantity = int(input())
            print(f"That will cost ${self.ticket_quantity * self.ticket_cost}. Please type how much cash you would like to give, we can make change (dollars only, no coins).")
            money_received = int(input("$ "))
        
        if money_received > self.ticket_quantity * self.ticket_cost:
            print(f"Here is your change. ${money_received - (self.ticket_quantity * self.ticket_cost)}. Best of luck!")
        
        elif money_received == self.ticket_quantity * self.ticket_cost:
            print(f"Thank you. Good luck!")
        
        #ADDED AS A TEST
        #self.generatetickets()
        #self.playthelotto()
        
        return self.ticket_quantity, self.ticket_cost
    
    
    def generatetickets(self):
        """
        Simulates the generation of tickets.
        """
        #uses ticket_quantity and generates random tickets
        ticket_quantity = self.ticket_quantity
        self.generated_tickets = []
        white_balls = [x for x in range(1, 70)]
        power_ball = [x for x in range(1, 27)]
        
        #randomly generates x number quickpicks based on ticket_quantity
        for i in range(ticket_quantity):
            white_ball_picks = random.sample(white_balls, 5)
            white_ball_picks.sort()
            power_ball_pick = random.sample(power_ball, 1)
            ticket_combo = white_ball_picks + power_ball_pick
            self.generated_tickets.append(ticket_combo)
        
        
        
        print("############################################")
        print("       Your Purchased Ticket Combos:        ")
        print("############################################")
        print("")
        for ticket in self.generated_tickets:
            #test prints
            #print("TEST PRINT", ticket)
            #print("TEST PRINT 2", ticket[order_count])
            #ticket_number = self.generated_tickets.index(ticket) + 1
            ticket_number = self.generated_tickets.index(ticket) + 1
            print(f"                 Ticket # {ticket_number}:")
            print("")
            print(f"White Balls: {ticket[:5]}")
            print(f"PowerBall: {ticket[5]}")
            print("")
            print("############################################")
            print("")

        print("                 GOOD LUCK                  ")
        #test prints
        #print("self.generated_tickets", self.generated_tickets)
        
        #DRIVER CODE
        #self.playthelotto()
        #TEST PRINT
        print("SELF.GENERATED_TICKETS", self.generated_tickets)
        return self.generated_tickets   

    def playthelotto(self):
        #initializes the lists of possible balls
        white_balls = [x for x in range(1, 70)]
        power_ball = [x for x in range(1, 27)]

        """
        Selecting random white balls and powerball.
        random.sample(sequence, k)
        """
        winning_white_balls = random.sample(white_balls, 5)
        winning_white_balls.sort()
        winning_power_ball = random.sample(power_ball, 1)
        self.winning_combo = winning_white_balls + winning_power_ball
        
        #test print statements
        #print(white_balls)
        #print(power_ball)
        #print("winning_white_balls", winning_white_balls)
        #print("winning_power_ball", winning_power_ball)
        #print("winning_combo", winning_combo)
        print("############################################")
        print("             WINNING DRAWING:               ")
        print("############################################")
        print(f"White Balls: {self.winning_combo[:5]}")
        print(f"Winning Power Ball: {self.winning_combo[5]}")
        
        #DRIVER CODE
        #self.checkwinnings()
        print("SELF.WINNING_COMBO", self.winning_combo)
        return self.winning_combo
        
          
    def checkwinnings(self):
            """
            Simulates the calculation of winnings from purchased tickets after drawing takes place.
            """
            generated_tickets = self.generated_tickets
            winning_combo = self.winning_combo
            winnings = 0
            #Prizes List: [Number of Matching White Balls, Number of Matching Power Ball, prize] 
            prizes= {
                #(5,1): "Grand Prize", will check for grand prize earning separately 
                (5,0): 1000000,
                (4,1): 50000,
                (4,0): 100,
                (3,1): 100,
                (3,0): 7,
                (2,1): 7,
                (1,1): 4,
                (0,1): 4,
            }
            
            #print tests
            #for ticket in generated_tickets:
            #    print("WHITES", ticket[:5])
            #print("WINNING COMBO WHITES", winning_combo[:5])
            # for ticket in generated_tickets:
            #     print("POWERBALL", ticket[5])
            # print("WINNING POWERBALL", winning_combo[5])
            print("############################################")
            print("       Checking for winners!                ")
            print("############################################")
            
            
            #checking for winning balls ticket by ticket
            winning_ball_totals = [0,0] #winning_ball_totals[0] - matching white balls, winning_ball_totals[1] - matching powerball
            for ticket in self.generated_tickets:
                #checking for whiteball matches
                print(f"CHECKING TICKET #{self.generated_tickets.index(ticket)+1}:")
                for whiteball in ticket[:5]:
                    if whiteball in winning_combo[:5]:
                        winning_ball_totals[0] += 1
                #checking for powerball match
                if ticket[5] == winning_combo[5]:
                    winning_ball_totals[1] += 1
                    
                #check for grand prize winner
                if winning_ball_totals[0] == 5 and winning_ball_totals[1] == 1:
                    print("YOU WON THE GRAND PRIZE!!!")
                    return "YOU WON THE GRAND PRIZE!"
                
                #check for other prize winnings and incrementing winnings
                elif tuple(winning_ball_totals) in prizes.keys():
                    print(f"You matched {winning_ball_totals[0]} white balls and {winning_ball_totals[1]} powerballs.")
                    print(f"Congratulations, adding ${prizes[tuple(winning_ball_totals)]} to prize winnings.")
                    winnings += prizes[tuple(winning_ball_totals)]
                
                else:
                    print("Sorry, this ticket is not a winner.")
                
                #reset totals for next ticket
                winning_ball_totals = [0,0]
                
                
            print("############################################")
            print("              YOUR WINNINGS:                ")
            print("############################################")
            #resetting generated_tickets and winning_combo to empty lists
            # self.generated_tickets = []
            # self.winning_combo = []
            if winnings > 0:
                print(f"You paid ${self.ticket_cost * self.ticket_quantity} for {self.ticket_quantity} tickets.")
                print(f"Congratulations! You have won ${winnings}!")
                print(f"Your net earnings are: ${winnings - (self.ticket_cost * self.ticket_quantity)}")
            else:
                print(f"Sorry, you don't have any winning tickets, and you lost ${self.ticket_cost * self.ticket_quantity}. Better luck next time!")
            self.winnings = winnings
            
            return self.winnings        
        
        
        
    # def checkwinnings_django(self):
    #     #TODO: REMOVE generated_tickets_to_dict ... do not need this anymore (logic is checked within tickets.html)
    #     """
    #     Simulates the calculation of winnings from purchased tickets after drawing takes place for DJANGO app
    #     """
    #     generated_tickets = self.generated_tickets
    #     #TODO: ADDED AS TEST
    #     generated_tickets_to_dict = self.generated_tickets_to_dict
    #     winning_combo = self.winning_combo
    #     winnings = self.winnings
    #     #Prizes List: [Number of Matching White Balls, Number of Matching Power Ball, prize] 
    #     prizes= {
    #         #(5,1): "Grand Prize", will check for grand prize earning separately 
    #         (5,0): 1000000,
    #         (4,1): 50000,
    #         (4,0): 100,
    #         (3,1): 100,
    #         (3,0): 7,
    #         (2,1): 7,
    #         (1,1): 4,
    #         (0,1): 4,
    #     }
        
    #     #TEST PRINT
    #     print("generated_tickets",generated_tickets)
        
    #     """
    #     generated_tickets is a list of lists: generated_tickets [[11, 19, 21, 63, 67, 26], [14, 22, 49, 59, 62, 15]]
        
    #     Generated tickets list is converted to ordered dict and checked, bool is False by default:
    #     generated_tickets_to_dict = [{11:True, 19:False, 21:False, 63:True, 67: False, 26: False},{14:False, 22:False, 49:False, 59:True, 62:False, 15:False}]
    #     Each ticket is transformed into a dictionary where the number is the key, and the value is a bool depending on if it matches the winning_combo numbers

    #     Keeps track per ticket of number of winning balls
    #     winning_ball_totals = [0,0]     winning_ball_totals[0] is matching whiteballs, winning_ball_totals[1] is matching powerball
        
    #     Logic in tickets view will determine the color of the border around the ball of each number in each ticket
        
    #     #TODO: amount won per ticket and total transaction to the right in the tickets view
    #     """

        
    #     print("############################################")
    #     print("       Checking for winners!                ")
    #     print("############################################")

        
    #     #checking for winning balls ticket by ticket in winning_combo
    #     winning_ball_totals = [0,0] #winning_ball_totals[0] - matching white balls, winning_ball_totals[1] - matching powerball
    #     generated_tickets_to_dict = []
    #     for ticket in self.generated_tickets:
    #         #creating dictionary with keys for each number in the ticket, default value is False
    #         ticket_dict = collections.OrderedDict((number, False) for number in ticket)
    #         #adding ticket dictionary to ticket_containers list
    #         self.generated_tickets_to_dict.append(ticket_dict)
    #     #test print
    #     print("MODIFIED GENERATED_TICKETS", self.generated_tickets_to_dict)
    #     print("WINNING COMBO", self.winning_combo)
        
    #     #LOOP THROUGH DICT TO FIND WHITEBALL MATCHES
        
    #     for i in range(0, 5):
    #         for ticket in self.generated_tickets_to_dict:
    #             #print("TICKET BEFORE MODIFICATIONS", ticket)
    #             for whiteball, winnerbool in list(ticket.items())[:5]:
    #                 if whiteball in self.winning_combo[:5]:
    #                     ticket[whiteball] = True
    #                     winning_ball_totals[0] += 1
    #             #print("TICKET AFTER MODIFICATIONS", ticket)
    #             t_powerball = list(ticket.items())[-1][0]
    #             if t_powerball == self.winning_combo[-1]:
    #                 ticket[t_powerball] = True
    #                 winning_ball_totals[1] += 1
                
    #             #check for grand prize winner
    #             if winning_ball_totals[0] == 5 and winning_ball_totals[1] == 1:
    #                 print("YOU WON THE GRAND PRIZE!!!")
    #                 return "YOU WON THE GRAND PRIZE!"
                
    #             #check for other prize winnings and incrementing winnings
    #             elif tuple(winning_ball_totals) in prizes.keys():
    #                 print(f"You matched {winning_ball_totals[0]} white balls and {winning_ball_totals[1]} powerballs.")
    #                 print(f"Congratulations, adding ${prizes[tuple(winning_ball_totals)]} to prize winnings.")
    #                 self.winnings += prizes[tuple(winning_ball_totals)]
                
    #             else:
    #                 print("Sorry, this ticket is not a winner.")
                
    #             #reset totals for next ticket
    #             winning_ball_totals = [0,0]
    #     print("WINNING COMBO", self.winning_combo)
    #     print("############################################")
    #     print("              YOUR WINNINGS:                ")
    #     print("############################################")
    #     #resetting generated_tickets and winning_combo to empty lists
    #     # self.generated_tickets = []
    #     # self.winning_combo = []
    #     if self.winnings > 0:
    #         print(f"You paid ${self.ticket_cost * self.ticket_quantity} for {self.ticket_quantity} tickets.")
    #         print(f"Congratulations! You have won ${self.winnings}!")
    #         print(f"Your net earnings are: ${self.winnings - (self.ticket_cost * self.ticket_quantity)}")
    #     else:
    #         print(f"Sorry, you don't have any winning tickets, and you lost ${self.ticket_cost * self.ticket_quantity}. Better luck next time!")
    #     return self.generated_tickets_to_dict, self.winnings
        

        
        
    
        
        
        

        
        

class RealPB: 
    """
    This class' methods handle the API calls and manipulation of JSON data from real Powerball data
    """
    def __init__(self):
        #initializes empty data_dict for instance
        self.data_dict = None
    
    #UNCOMMENT TO QUERY API
    # def query_api(self):
    #     """
    #     Connects to Powerball API to obtain the most recent Powerball drawing results and saves it to data_dict.
        
    #     API connection code provided by:
    #     https://collectapi.com/api/chancegame/lottery-api
    #     limit 10 connections/calls per month. 
    #     Pulled data on 3/8/23 and saved to api_results.json for further parsing
    #     """
        
    #    # Check if the api_results.json file exists (this is only because I hit the 10 API limit while developing)
    #     try:
    #         with open('api_results.json', 'r') as f:
    #             data_dict = json.load(f)
    #             if data_dict:
    #                 print("Using data from api_results.json file")
    #                 return data_dict
    #     except FileNotFoundError:
    #         #Query the API for information
    #         conn = http.client.HTTPSConnection("api.collectapi.com")
    #         headers = {
    #             'content-type': "application/json",
    #             'authorization': api_token
    #         }
    #         conn.request("GET", "/chancegame/usaPowerball", headers=headers)
    #         res = conn.getresponse()
    #         data = res.read()
    #         data_dict = json.loads(data.decode("utf-8"))
    #         #print(data.decode("utf-8"))
    #         if data_dict['success'] == True:
    #             print("Powerball API was queried successfully.")
    #         else:
    #             print("There was an error accessing the Powerball API. Please try again later.")
            
    #         #Saving data to api_results.json file
    #         with open('api_results.json', 'w', encoding='utf8') as outfile:
    #             json.dump(data_dict, outfile)
    #         return data_dict

    def read_api_results(self):
        """
        opening json file in read mode for further use
        """
        with open('api_results.json', 'r') as f:
            data_dict = json.load(f)
        #TEST PRINT STATEMENT
        #print(data_dict)
        self.data_dict = data_dict
        #TESTING
        #self.previous_pb_stats()
        #self.future_pb()
        return self.data_dict


    def previous_pb_stats(self):
        """
        Displays previously won Powerball numbers and Powerball for most recent drawing.
        """
        data_dict = self.read_api_results()
        #UNCOMMENT TO USE API DATA
        #data_dict = self.query_api()
            
        #accessing previously won numbers (White balls)
        temp = []
        print("############################################")
        print("        PREVIOUS POWERBALL DRAWING")
        print("############################################")
        for k, v in data_dict['result']['numbers'].items():
            if k != "pb":
                temp.append(int(v))
        print("White balls :", (temp))
        #accessing previously won powerball (red ball)
        for k, v in data_dict['result']['numbers'].items():
            if k == "pb":
                print("Powerball: ", v)
        
        
    def future_pb(self):
        """
        Displays future Powerball drawing information.
        """
        data_dict = self.read_api_results()
        #UNCOMMENT TO USE API DATA
        #data_dict = self.query_api()
        
        #accessing next jackpot
        print("############################################")
        print("        UPCOMING POWERBALL DRAWING")
        print("############################################")
        print("Next Jackpot amount: ", data_dict['result']['next-jackpot']['amount'])
        print("Next Drawing: ", data_dict['result']['next-jackpot']['date'])
            




"""
TEST CODE
"""
#REAL POWERBALL TEST CODE
# p1 = RealPB()  # create an instance of the RealPB class
# p1.previous_pb_stats()  # call the previous_pb_stats method
# p1.future_pb() # call the future_pb method

# #LOTTO SIMULATION TEST CODE
# p1 = LottoSimulation() # create an instance of the LottoSimulation class
# p1.purchase_tickets() #b calls the purchase_tickets() method
# p1.generatetickets() #calls the generatetickets method which generates random tickets
# p1.playthelotto() # calls the playthelotto() method, simulating the play
# p1.checkwinnings_django() #calls the checkwinnings_django() method, simulating checking potential winnings
# # p1.checkwinnings() #calls the checkwinnings() method, simulating checking potential winnings
