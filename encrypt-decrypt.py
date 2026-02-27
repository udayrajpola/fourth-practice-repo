
alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





# def encrypt(original_text,shift_amount):
#     encrypted_text=""
#
#     for letter in original_text:
#         if letter in alphabet:
#             letter_index=alphabet.index(letter)
#             new_index=letter_index+shift_amount
#             new_index=new_index % len(alphabet)
#             encrypted_text+=alphabet[new_index]
#         elif letter not in alphabet:
#             encrypted_text+=letter
#     print(encrypted_text)
#
#
# def decrypt(original_text,shift_amount):
#     decrypted_text=""
#
#     for letter in original_text:
#         if letter in alphabet:
#             if direction.lower()=="decode":
#                 shift_amount=-1*shift_amount
#
#             letter_index=alphabet.index(letter)
#             new_index=letter_index-shift_amount
#             new_index=new_index % len(alphabet)
#             decrypted_text+=alphabet[new_index]
#         elif letter not in alphabet:
#             decrypted_text+=letter
#     print(decrypted_text)

def caeser(original_text,shift_amount,direction):
        encrypted_text=""
        if direction.lower() == "decode":
            shift_amount = -1 * shift_amount
        for letter in original_text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_index = letter_index + shift_amount
                new_index = new_index % len(alphabet)
                encrypted_text += alphabet[new_index]
            elif letter not in alphabet:
                encrypted_text += letter
        print(encrypted_text)

uday=True
while uday:
    direct = input("Do you want to encode or decode the data\n")
    text = input("Enter your text\n")
    shift = int(input("Enter the amount you want to shift\n"))
    caeser(original_text=text,shift_amount=shift,direction=direct)
    again=input("Do you want to do encrypt or decrypt again if yes type yes or else no?")
    if again.lower()=="yes":
        uday=True
    elif again.lower()=="no":
        uday=False
    else:
        uday=True
        print("typed Invalid response")

print("end of encrypt and decrypt")

