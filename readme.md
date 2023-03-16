# Full-Stack Powerball Simulation Project
<p>Jennifer Kaiser 2023 
<p>
<a href="www.jenniferkaiser.tech">www.jenniferkaiser.tech</a>
<p>
<a href="www.linkedin.com/in/jenniferkaiser-tech">www.linkedin.com/in/jenniferkaiser-tech</a>
<p>
<a href="www.github.com/jenniferkaiser21">www.github.com/jenniferkaiser21</a>

# Demo of Working Code
<a href="https://youtu.be/Y5tQHNiYaMo">https://youtu.be/Y5tQHNiYaMo</a>

 # Data Source(s):
<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/e2c490be9ac10987f6daf616188e22a84ad390a7/images/powerball_chart.jpg">
Source: <a href="www.powerball.com">www.powerball.com</a>

# Languages Used:
* Python (Version 3.9.12)

# Packages/Libraries Used:
* Django 
* random 
* sys 
* json

# IDE Used:
* VSCode

# Version Control:
* Git

# Summary of Project:
This project simulates aspects of playing the Powerball Lottery game (including purchasing of tickets, tendering change, simulation of drawing, and checking prize earnings based on the official prize chart), as well as queries an API that returns the latest official drawing data. Front-end web visualization is implemented using Django, HTML, and CSS. Back-end components for this project incorporate Python, Bash scripting, Object-Oriented Programming (OOP), and JSON data processing.

Upon launch, the homepage displays the most recently drawn Powerball result, including information about date and jackpot amount, and future drawing date and jackpot amount. The user has the option to select from two main categories: Powerball Simulation or Recent Powerball Stats. 

<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/60b7a80c80495c4de15efbb0056b9287211a4601/screenshots/home.png">

Within the Powerball Simulation section, there is a link to "use the stand-alone powerball drawing", which acts like a "quick-pick" generator.

<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/60b7a80c80495c4de15efbb0056b9287211a4601/screenshots/quickpick.png">

Clicking on the main link to "play Powerball Simulation", the user will be prompted to input the number of tickets they wish to simulate purchasing. 

<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/60b7a80c80495c4de15efbb0056b9287211a4601/screenshots/purchase.png">

Upon clicking Purchase, the user is then directed to a page that has the simulated Powerball winning combo displayed on the left, and all of their simulated generated tickets on the right. Any matching balls will have a green border around the individual ball, and any ticket that wins a prize (according to the prize chart from above) will have a green border around the entire ticket. Each ticket has feedback on the right side that describes the prize winnings (if any). Under the winning drawing on the left, a box displays the results for the overall simulated ticket purchase, including Total Amount spent on tickets, Gross Winnings, and Net earnings (taking cost of purchase into account).

<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/60b7a80c80495c4de15efbb0056b9287211a4601/screenshots/drawing.png">

The user has the option to view Recent Powerball Stats, which uses information parsed from a JSON file, originally fetched from on API (see additional notes regarding API).

<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/60b7a80c80495c4de15efbb0056b9287211a4601/screenshots/stats.png">


The user is prompted to select how many Powerball tickets they wish to purchase and the program calculates the cost and potential change made to the customer, the program then simulates the random distribution of lotto numbers. Once the user has purchased the Powerball ticket(s), it will begin the simulation of picking 5 random white balls and one powerball, and references the users' ticket(s) to notify them if they have won a prize, and total their net winnings (or losses).


# Additional Notes:
API: 

For security, the API key used to call the API has been obscured. An API key can be generated by visiting <a href="collectapi.com">collectapi.com</a>. The API calling portion of the code is currently commented out, as to not hit the limit per month.
<p>
<img src="https://github.com/jenniferKaiser21/Lottery_Project/blob/81d16621b90a0034d4d218bb1d2fca90b2b07a08/images/API_call_example.jpeg">

Standalone Python program:

This project began as a stand-alone terminal-driven Python program, and the code was eventually modified to use Django to display a graphical user interface to interact with the various methods written. The original code (standalone Python program) can be found in the "Standalone_program" directory.

Please note that both the final project (using Django) and the standalone Python program include printing output to the terminal for debugging purposes.
