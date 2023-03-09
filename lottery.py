import random
import json
import http.client
import sys
sys.path.append('api.py')
from api import api_token


class LottoSimulation:
    """
    This class' methods simulate the purchasing of tickets and powerball drawing simulation.
    """
    #Prizes List: [Number of Matching White Balls, Number of Matching Power Ball, prize] 
    prizes = [[5, 1, "Grand Prize"], # 5 white balls + PB
              [5, 0, "$1,000,000"], # 5 white balls
              [4, 1, "$50,000"], # 4 white balls + PB
              [4, 0, "$100"], # 4 white balls
              [3, 1, "$100"], # 3 white balls + PB
              [3, 0, "$7"], # 3 white balls
              [2, 1, "$7"], # 2 white balls + PB
              [1, 1, "$4"], # 1 white ball + PB
              [0, 1, "$4"], # PB
              ]
    
    def __init__(self, ticket_quantity=0, ticket_cost=0, customer_tickets = []):
        self.ticket_quantity = ticket_quantity
        self.ticket_cost = ticket_cost
        self.customer_tickets = customer_tickets
        
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
            
        return self.ticket_quantity, self.ticket_cost

    def playthelotto(self):
        #initializes the lists of possible balls
        white_balls = [x for x in range(1, 70)]
        power_ball = [x for x in range(1, 27)]
        winning_white_balls = []
        winning_power_ball = []
        white_balls_in_play = white_balls.copy()
        power_ball_in_play = power_ball.copy()
        
        #picking 5  white balls
        """
        random.sample(sequence, k)
        """
        winning_white_balls = random.sample(white_balls_in_play, 5)
        
        #picking powerball
        winning_power_ball = random.sample(power_ball_in_play, 1)
        
        winning_combo = [winning_white_balls[:],winning_power_ball[0]]
        #test print statements
        print(white_balls)
        print(power_ball)
        print("winning_white_balls", winning_white_balls)
        print("winning_power_ball", winning_power_ball)
        print("winning_combo", winning_combo)
        return white_balls, power_ball, winning_combo
        
    def generatetickets(self):
        #uses ticket_quantity and generates random tickets
        #TODO: Implement logic here, use random.sample(sequence, k)
        ticket_quantity = self.ticket_quantity
        customer_tickets = [[]] * ticket_quantity
        
        for i in range(ticket_quantity):
            #customer_tickets[i].append(#TODO: append in format winning_combo [[2, 59, 25, 41, 63], 12])
            pass                           
        
        
        
        

class RealPB: 
    """
    This class' methods handle the API calls and manipulation of JSON data from real Powerball data
    """
    def __init__(self):
        #initializes empty data_dict for instance
        self.data_dict = None
        
    def query_api(self):
        """
        Connects to Powerball API to obtain the most recent Powerball drawing results and saves it to data_dict.
        
        API connection code provided by:
        https://collectapi.com/api/chancegame/lottery-api
        limit 10 connections/calls per month. 
        Pulled data on 3/8/23 and saved to api_results.json for further parsing
        """
        
       # Check if the api_results.json file exists (this is only because I hit the 10 API limit while developing)
        try:
            with open('api_results.json', 'r') as f:
                data_dict = json.load(f)
                if data_dict:
                    print("Using data from api_results.json file")
                    return data_dict
        except FileNotFoundError:
            #Query the API for information
            conn = http.client.HTTPSConnection("api.collectapi.com")
            headers = {
                'content-type': "application/json",
                'authorization': api_token
            }
            conn.request("GET", "/chancegame/usaPowerball", headers=headers)
            res = conn.getresponse()
            data = res.read()
            data_dict = json.loads(data.decode("utf-8"))
            #print(data.decode("utf-8"))
            if data_dict['success'] == True:
                print("Powerball API was queried successfully.")
            else:
                print("There was an error accessing the Powerball API. Please try again later.")
            
            #Saving data to api_results.json file
            with open('api_results.json', 'w', encoding='utf8') as outfile:
                json.dump(data_dict, outfile)
            return data_dict

    def read_api_results(self):
        """
        opening json file in read mode for further use
        """
        with open('api_results.json', 'r') as f:
            data_dict = json.load(f)
        print(data_dict)
        return data_dict


    def previous_pb_stats(self):
        """
        Displays previously won Powerball numbers and Powerball for most recent drawing.
        """
        data_dict = self.query_api()
            
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
        data_dict = self.query_api()
        
        #accessing next jackpot
        print("############################################")
        print("        UPCOMING POWERBALL DRAWING")
        print("############################################")
        print("Next Jackpot amount: ", data_dict['result']['next-jackpot']['amount'])
        print("Next Drawing: ", data_dict['result']['next-jackpot']['date'])
            




"""
TEST CODE
"""
# p1 = RealPB()  # create an instance of the RealPB class
# p1.previous_pb_stats()  # call the previous_pb_stats method
# p1.future_pb() # call the future_pb method

p1 = LottoSimulation() # create an instance of the LottoSimulation class
p1.purchase_tickets() #b calls the purchase_tickets() method
p1.playthelotto() # calls the playthelotto(), simulating the play
print(p1.ticket_cost) # checks the assigned ticket_cost 
print(p1.ticket_quantity) # checks the assigned ticket_quantity