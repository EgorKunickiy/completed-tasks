import collections

def time_count(array_people: list, count_cash_reg: int) ->int:
    cash_registers = array_people[:count_cash_reg]
    que = collections.deque(array_people[count_cash_reg:])
    time = 0

    while max(cash_registers) != 0 or len(que) > 0:
        if 0 in cash_registers and len(que) != 0:
            cash_registers = map(lambda x: x if x != 0 else que.popleft(), cash_registers)
        cash_registers = list(map(lambda x: x-1, cash_registers))
        time += 1

    return time

if __name__ == "__main__":
    print(time_count([5, 3, 4], 1))
    print(time_count([10, 2, 3, 3], 2))
    print(time_count([2, 3, 10], 2))
