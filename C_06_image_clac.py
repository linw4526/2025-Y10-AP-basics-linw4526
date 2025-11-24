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
image_ans = image_calc()
print(image_ans)