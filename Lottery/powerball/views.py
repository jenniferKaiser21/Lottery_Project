from django.shortcuts import render, redirect
import sys
# sys.path.append('Lottery_Project/lottery.py')
# from lottery import LottoSimulation
from .lottery import LottoSimulation, RealPB


# Create your views here.
def home(request):
    return render(request, "powerball/home.html")

def drawing(request):
    lotto_sim = LottoSimulation()
    lotto_sim.playthelotto()
    winning_combo = lotto_sim.winning_combo
    first_five_numbers = winning_combo[:5]
    powerball = winning_combo[5]
    context = {'first_five_numbers': first_five_numbers, "powerball": powerball}
    return render(request, "powerball/drawing.html", context)

def tickets(request, lotto_sim):
    # purchase_instance = LottoSimulation()
    # purchase_instance.purchase_tickets()
    # generated_tickets = purchase_instance.generated_tickets
    
    #SIMULATION DRIVER CODE
    #lotto_sim = LottoSimulation()
    #lotto_sim.purchase_tickets()
    lotto_sim.generatetickets()
    lotto_sim.playthelotto()
    lotto_sim.checkwinnings()
    
    generated_tickets = lotto_sim.generated_tickets
    winning_combo = lotto_sim.winning_combo
    winnings = lotto_sim.winnings
    money_spent = (lotto_sim.ticket_cost * lotto_sim.ticket_quantity)
    net_earnings = winnings - money_spent
    
    #TEST PRINT
    print("WINNING COMBO FROM VIEW", winning_combo)
    #print(lotto_sim.winning_combo)
    print("GENERATED_TICKETS FROM VIEW", generated_tickets)
    #print(lotto_sim.generated_tickets)
    print("WINNINGS FROM VIEW", winnings)
    
    
    winning_first_five_numbers = lotto_sim.winning_combo[:5]
    winning_powerball = lotto_sim.winning_combo[-1]
    
    ticket_containers = []
    
    #winnings = lotto_sim.winnings

    for ticket in generated_tickets:
        first_five_numbers = ticket[:5]
        powerball = ticket[5]
        ticket_outcome = ticket[-1]
        ticket_container = {'first_five_numbers': first_five_numbers, 'powerball': powerball, 'ticket_outcome': ticket_outcome}
        ticket_containers.append(ticket_container)
        context = {'money_spent': money_spent, 'net_earnings':net_earnings, 'winnings': winnings, 'ticket_containers': ticket_containers, 'winning_first_five_numbers': winning_first_five_numbers, "winning_powerball": winning_powerball}    
#    return render(request, "powerball/tickets.html", context)
    return render(request, "powerball/tickets_new.html", context)



def purchase(request):
    if request.method =='POST':
        ticket_quantity = int(request.POST.get('ticket_quantity'))
        #money_received = int(request.POST.get('money_received'))
        print("TICKET_QUANTITY IN VIEW", ticket_quantity)
        lotto_sim = LottoSimulation()
        lotto_sim.purchase_tickets(ticket_quantity)
        ticket_cost = lotto_sim.ticket_cost
        
        
        message = f"You have purchased {ticket_quantity} tickets for ${ticket_quantity * ticket_cost}. Good luck!"

        return tickets(request, lotto_sim)
        #return render(request, 'powerball/purchase.html', {"message": message})
    return render(request, "powerball/purchase.html")





def stats(request):
    stats_instance = RealPB()
    stats_instance.read_api_results()
    data_dict = stats_instance.data_dict
    print("THIS IS IN STATS VIEW", data_dict)
    previous_white_balls = []
    for k,v in data_dict['result']['numbers'].items():
        if k != "pb":
            previous_white_balls.append(int(v))

    previous_pb = 0
    for k, v in data_dict['result']['numbers'].items():
        if k == "pb":
            previous_pb = int(v)
            
    previous_drawing_date = data_dict['result']['date']
    print("PREVIOUS DRAWING DATE", previous_drawing_date)
    
    previous_jackpot = data_dict['result']['jackpot']
    print("PREVIOUS JACKPOT: ", previous_jackpot)
    next_drawing_amt = data_dict['result']['next-jackpot']['amount']
    next_drawing_date = data_dict['result']['next-jackpot']['date']
    
    context = {"previous_white_balls":previous_white_balls, "previous_pb":previous_pb, "next_drawing_amt":next_drawing_amt, "next_drawing_date":next_drawing_date, "previous_drawing_date":previous_drawing_date, "previous_jackpot":previous_jackpot,}
    return render(request, "powerball/stats.html", context)
    