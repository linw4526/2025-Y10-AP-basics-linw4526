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
    width = num_check ('Width in meter:')
    height = num_check ('Height in meter:')
    price = num_check('Price per meter:')
    area = height * width
    perimeter = 2 * (height + width)
    totalprice = price * perimeter
    print()
    print(f'Perimeter: {perimeter} meters')
    print(f'Area: {area} meters')
    print(f'Price: {totalprice:.2f} NZD')
    keep_going = (input('Press enter to keep going or any key to quit'))
    print()
    print('Thanks')
