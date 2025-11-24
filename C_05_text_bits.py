from multiprocessing.connection import answer_challenge


def clac_text_bits():
    response = input("Enter some text")
    nun_chars = len(response)
    num_bits = nun_chars * 8
    answer = (f"{response} has {nun_chars} characters. "
                f"\nWe need {nun_chars} x 8 bits to represent it "
                f"\nwhich is {num_bits} bits")
    return answer
text_ans = clac_text_bits()
print(text_ans)

