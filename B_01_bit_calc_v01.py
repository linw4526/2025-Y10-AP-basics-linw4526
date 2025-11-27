def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")
def instructions():
    statement_generator("Instructions", "-")
    statement_generator("Instructions", "-")
    print('''
    Instructions go here.
    -instruction 1
    -instruction 2
    -etc
    ''')
def get_filetype():
    while True:
        response = input("File type:").lower()
        if response == "xxx" or response == "i":
            return response
        elif response in ['integer', 'int']:
            return 'integer'
        elif response in ['image', 'picture', 'img', 'p']:
            return 'image'
        elif response in ['text', 'txt', 't']:
            return 'text'
        else:
            print('Please enter a valid file type')

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

def image_calc():
    height = int_check ("Height: ",0)
    width = int_check ("Width: ", 1)
    num_pixels = width * height
    num_bits = num_pixels * 24
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f" \nNumber of bits: {num_pixels} x24 = {num_bits}")
    return answer

def integer_calc():
    integer = int_check("Integer: ", 0)
    raw_binary = bin(integer)
    binary = raw_binary[2:]
    num_bits = len(binary)
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."
    return answer

def calc_text_bits():
    response = input("Enter some text")
    nun_chars = len(response)
    num_bits = nun_chars * 8
    answer = (f"{response} has {nun_chars} characters. "
            f"\nWe need {nun_chars} x 8 bits to represent it "
            f"\nwhich is {num_bits} bits")
    return answer

    num_pixels = width * height
    num_bits = num_pixels * 24
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f" \nNumber of bits: {num_pixels} x24 = {num_bits}")
    return answer

want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()
    if file_type == "xxx":
        break
    if file_type == 'i':
        want_image = input("press 1 for an integer or 2 for image ")
        if want_image == '1':
            file_type = 'integer'
        elif want_image == "2":
            file_type = 'image'

    if file_type == 'image':
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)



