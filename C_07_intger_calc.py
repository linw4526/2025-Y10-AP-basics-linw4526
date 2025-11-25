def int_check (question,low):
    """Checks integers are higher than a given number"""
    error = f"please enter a number that is more than zero {low}\n"
    while True:
        try:
            response = int(input(question))
            if response >= low:
                return response
            else:
                print (error)
        except ValueError:
            print (error)

def integer_calc():
    integer = int_check ("Integer: ",0)
    raw_binary = bin(integer)
    binary = raw_binary[2:]
    num_bits = len(binary)
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."
    return answer
integer_ans = integer_calc()
print(integer_ans)