import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
	"A": 2,
	"B": 4,
	"C": 6,
	"D": 8
}

symbol_value = {
	"A": 2,
	"B": 4,
	"C": 6,
	"D": 8
}

def check_winnings(columns, lines, bet, value):
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_to_check =  column[line]
			if symbol != symbol_to_check:
				break
			else:
				winnings += value[symbol] * bet
				winning_lines.append(line + 1)
	return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	columns = []
	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):	
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
		columns.append(column)
	return columns

def print_slot_machine(columns):
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) - 1:
				print(column[row], end=" | ")
			else:
				print(column[row], end="")
		print()
	
	
def deposit():
	while True:
		amout = input("What u would like to deposit? $")
		if amout.isdigit():	
			amout = int(amout)
			if amout > 0:
				break
			else:
				print("Amout must be greater than 0")
		else:
			print("please enter a number")
	return amout



def Get_number_of_lines():
	while True:
		lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
		if lines.isdigit():	
			lines = int(lines)
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("Enter a valid number of lines.")
		else:
			print("please enter a number")
	return lines


def get_bet():
	while True:
		amout = input("What u would like to bet on each line? $")
		if amout.isdigit():	
			amout = int(amout)
			if MIN_BET <= amout <= MAX_BET:
				break
			else:
				print(f"Amout must be between  ${MIN_BET} - ${MAX_BET}")
		else:
			print("please enter a number")
	return amout

def spin(balance):
	lines = Get_number_of_lines()
	while True:
		bet = get_bet()
		total_bet = bet * lines
		if total_bet > balance:
			print(f"you do not have enough to bet that amout, your balance is ${balance}")
		else:
			break

	print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
	slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
	winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
	print(f"You won ${winnings}.")
	print(f"you won on: ", *winning_lines)
	print_slot_machine(slots)
	return winnings - total_bet
	

def main():
	balance = deposit() 
	while True:
		print(f"current Balance is: ${balance}")
		spins = input("press Enter to play(q to quit) ")
		if spins == "q":
			break
		balance += spin(balance)
	print(f"You left with ${balance}")

main()