from random import choices
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
    
    def __init__(self, ticket_quantity=0):
        self.ticket_quantity = ticket_quantity
        
    def purchase_tickets(self):
        """
        Simulates the ticket purchasing process.
        """
        ticket_cost = 2
        self.ticket_quantity = int(input(f"Welcome to Powerball! Each quick pick costs ${ticket_cost}. \nHow many tickets would you like to purchase?  "))
        
        print(f"That will cost ${self.ticket_quantity * ticket_cost}. Please type how much cash you would like to give, we can make change (dollars only, no coins).  ")
        money_received = int(input("$ "))
        
        while money_received < self.ticket_quantity * ticket_cost:
            print(f"Sorry, you don't have enough money. How many tickets would you like to buy? ")
            self.ticket_quantity = int(input())
            print(f"That will cost ${self.ticket_quantity * ticket_cost}. Please type how much cash you would like to give, we can make change (dollars only, no coins).")
            money_received = int(input("$ "))
        
        if money_received > self.ticket_quantity * ticket_cost:
            print(f"Here is your change. ${money_received - (self.ticket_quantity * ticket_cost)}. Best of luck!")
        
        elif money_received == self.ticket_quantity * ticket_cost:
            print(f"Thank you. Good luck!")
            
        return self.ticket_quantity, ticket_cost

    def playthelotto(ticket_quantity, ticket_cost):
        #TODO: implement logic here
        #use ticket_quantity
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

# p1 = LottoSimulation() # create an instance of the LottoSimulation class
# p1.purchase_tickets() #b calls the purchase_tickets() method