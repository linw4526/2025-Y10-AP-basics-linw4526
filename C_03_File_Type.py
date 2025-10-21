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
while True:
    file_type = get_filetype()
    if file_type == 'i':
        want_image = input("press 1 for an integer or 2 for image ")
        if want_image == '1':
            file_type = 'integer'
        elif want_image == "2":
            file_type = 'image'

    print (f"you chose{file_type}")
    if file_type == "xxx":
        break
