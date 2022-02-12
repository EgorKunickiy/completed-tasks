import math

def recurs_multiplic (value, coefficient, times):
    result = 0
    for i in range(times):
        value *= coefficient
        result += value
    return math.ceil(result)

def compare(card, ticket, perc):
    total_cards_pr = card
    total_ticket_pr = ticket
    count = 1
    while True:
        if total_ticket_pr > total_cards_pr:
            print(total_ticket_pr)
            print(total_cards_pr)
            return count
        else:
            count += 1
            total_ticket_pr = ticket * count
            total_cards_pr = card + recurs_multiplic(ticket, perc, count)


if __name__ == '__main__':
    print(compare(500, 15, 0.9))
    print(compare(100, 10, 0.95))