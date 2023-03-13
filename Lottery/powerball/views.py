from django.shortcuts import render
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

def tickets(request):
    purchase_instance = LottoSimulation()
    purchase_instance.purchase_tickets()
    generated_tickets = purchase_instance.generated_tickets
    
    lotto_sim = LottoSimulation()
    lotto_sim.playthelotto()
    winning_combo = lotto_sim.winning_combo
    winning_first_five_numbers = winning_combo[:5]
    winning_powerball = winning_combo[5]
    
    ticket_containers = []
    
    for ticket in generated_tickets:
        first_five_numbers = ticket[:5]
        powerball = ticket[5]
        ticket_container = {'first_five_numbers': first_five_numbers, 'powerball': powerball}
        ticket_containers.append(ticket_container)
        
        context = {'ticket_containers': ticket_containers, 'winning_first_five_numbers': winning_first_five_numbers, "winning_powerball": winning_powerball}
        
    return render(request, "powerball/tickets.html", context)

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
            
    next_drawing_amt = data_dict['result']['next-jackpot']['amount']
    net_drawing_date = data_dict['result']['next-jackpot']['date']
    
    context = {"previous_white_balls":previous_white_balls, "previous_pb":previous_pb, "next_drawing_amt":next_drawing_amt, "net_drawing_date":net_drawing_date,}
    return render(request, "powerball/stats.html", context)
    