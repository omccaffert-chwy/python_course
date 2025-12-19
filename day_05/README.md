# Day 5 – Dictionaries & State (Udemy Day 9–10)

**Udemy days to assign:**

* **Day 9** – dictionaries, nesting, Secret Auction
* **Day 10** – functions with outputs, calculator project

**Robotics project (replace Secret Auction / Calculator):**
🛠 **Robot Inventory & Config Manager**

* Use dictionaries to store a robot's configuration: motors, sensors, ranges, etc.
* Functions that **calculate** derived values (e.g., total sensor count, max reachable distance).

**1-hour lesson:**

* Explain dicts: `{ "sensor_type": "lidar", "range": 5.0 }`
* Show list of dicts to represent multiple robots.
* Demonstrate a function that **returns** a computed config stat.

**1-hour work:**

* Students build **Inventory & Config Manager**.
* Stretch: allow user to add new robots and print a summary table.


sec auction:
The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)
Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the highest bid and prints it.
 Hint 1 
 Hint 2 
Flowchart
If you want to see my flowchart, you can download it here.
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


calc:
The goal is to build a calculator program.

Demo
https://appbrewery.github.io/python-day10-demo/

Storing Functions as a Variable Value
You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
Program asks the user to type the first number.
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
Program asks the user to type the second number.
Program works out the result based on the chosen mathematical operator.
Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py
 Hint 1 
 Hint 2 
 def add(n1, n2):
    return n1 + n2


