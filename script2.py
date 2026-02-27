
alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt():
    direction = input("Do you want to Encrypt or decrypt the data\n")
    Uday=False
    while not Uday:
        if direction.lower() == "encrypt":
            original_text = input("Enter your text\n")
            shift_amount = int(input("Enter the amount you want to shift\n"))
            list=[]
            encrypted_word=""
            for letters in original_text:
                if letters in alphabet:
                    if alphabet.index(letters)+shift_amount <26:
                        list.append(letters)
                        word_index = alphabet.index(letters)
                        new_index = word_index + shift_amount
                        encrypted_word += alphabet[new_index]
                        print(alphabet[new_index])
                    elif alphabet.index(letters)+shift_amount >26:
                        list.append(letters)
                        word_index = alphabet.index(letters)
                        new_index = (word_index + shift_amount)-26
                        encrypted_word += alphabet[new_index]
                        print(alphabet[new_index])
                else:
                    list.append(letters)
                    encrypted_word+=letters
            print(list)
            print(encrypted_word)
        elif direction.lower() == "decrypt":
            # original_text = input("Enter your text\n")
            # shift_amount = int(input("Enter the amount you want to shift\n"))
            list2 = []
            decrypted_word=""
            for letters in encrypted_word:
                if letters in alphabet:
                    if alphabet.index(letters) + shift_amount < 26:
                        list2.append(letters)
                        word_index = alphabet.index(letters)
                        new_index2 = word_index - shift_amount
                        decrypted_word+= alphabet[new_index2]
                        print(alphabet[new_index2])
                    elif alphabet.index(letters) + shift_amount > 26:
                        list2.append(letters)
                        word_index = alphabet.index(letters)
                        new_index2 = (word_index - shift_amount)
                        decrypted_word += alphabet[new_index2]
                        print(alphabet[new_index2])
        else:
            print("Wrong Input")
        user_input = input("Do you want to do again\n")
        if user_input.lower() == "yes":
            encrypt()
        else:
            Uday=True


encrypt()
