def num_check (question):
    error = "please enter a number that is more than zero\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print (error)
        except ValueError:
            print (error)
keep_going = ''
while keep_going == '':
    width = num_check ('Width:')
    height = num_check ('Height:')
    area = height * width
    perimeter = 2 * (height + width)
    print()
    print(f'Perimeter: {perimeter} units')
    print(f'Area: {area} units')
    keep_going = (input('Press enter to keep going or any key to quit'))
    print()
    print('Thanks')