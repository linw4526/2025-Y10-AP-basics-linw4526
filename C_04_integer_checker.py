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

for item in range (0, 2):
    integer = int_check ("Integer: ",0)
    print (integer)
for item in range (0, 2):
    width = int_check ("Width: ", 1)
    print (width)       