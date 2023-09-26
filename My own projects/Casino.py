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
    "D": 8,
}
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def chekc_winnings(colums, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = colums[0][line]
        for column in colums:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        colums.append(column)

    return colums

def print_slot_machine(colums):
    # transposing
    for row in range(len(colums[0])):
        for i, column in enumerate(colums):
            if i != len(colums) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deopsit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Must be higher than zero:")
        else:
            print("pelase enter a number")

    return amount

def get_number_of_line():
        while True:
            lines = input("enter the number of lines to bet on from (1-" + str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("enter a valid number of lines")
            else:
                print("please enter a valid number")

        return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}:")
        else:
            print("pelase enter a number")

    return amount


def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enought money, you current balance is: ${balance}")
        else:
            break

    
    print(f"you are betting {bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = chekc_winnings(slots, lines, bet, symbol_values)
    print(f"you won ${winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin = input("press enter to spin (q to quit)")
        if spin == 'q':
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

main()