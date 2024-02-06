#Imports
#Functions

def encryption(message,shifter_key):
    encryption_result = ""

    #go through every character 
    for i in range (len(message)):
        letter = message[i]

        if (letter.isalpha()):
            if (letter.isupper()):
                encryption_result += chr((ord(letter) + shifter_key - 65)%26 +65)
            elif (letter.islower()):
                encryption_result += chr((ord(letter) + shifter_key - 97)%26 +97)
        elif (letter.isnumeric()):
            encryption_result += letter
        else:
            if (letter == " "):
                encryption_result += " "
            if (letter == "."):
                encryption_result += "."
    return encryption_result

def decryption(message,shifter_key):
    decryption_result = ""

    #go through every character 
    for i in range (len(message)):
        letter = message[i]

        if (letter.isalpha()):
            if (letter.isupper()):
                decryption_result += chr((ord(letter) - shifter_key - 65)%26 +65)
            elif (letter.islower()):
                decryption_result += chr((ord(letter) - shifter_key - 97)%26 +97)
        elif (letter.isnumeric()):
            decryption_result += letter
        else:
            if (letter == " "):
                decryption_result += " "
            if (letter == "."):
                decryption_result += "."
    return decryption_result
print(encryption("Prem Vir", 5))
print(decryption("Uwjr Anw",5))


'''#logical functions
#Moving text to Decrytion Box/ Encrypter
def move_text_to_decryption_box():
    empty_message = ("Error! The Encryption box or shifter key box is empty")
    moving_text = encryptionn_box.get("1.0",mn.tkinter.END)
    shifter_key_number = shifter_key_box.get("1.0",mn.tkinter.END)
    
    if (len(moving_text)< 2) or (len(shifter_key_number)<2):
        decryptionn_box.insert("1.0", empty_message)
    else:
        decryptionn_box.insert("1.0", mn.MainWindow.encryption(moving_text,moving_text,int(shifter_key_number)))
        encryptionn_box.delete("1.0", mn.tkinter.END)

#Moving text to Encryption Box/ Decrypter
def move_text_to_encryption_box():
    empty_message = ("Error! The Encryption box or shifter key box is empty")
    moving_text = decryptionn_box.get("1.0",mn.tkinter.END)
    shifter_key_number = shifter_key_box.get("1.0",mn.tkinter.END)
    
    if (len(moving_text)< 2) or (len(shifter_key_number)<2):
        encryptionn_box.insert("1.0", empty_message)
    else:
        encryptionn_box.insert("1.0", mn.MainWindow.decryption(moving_text,moving_text,int(shifter_key_number)))
        decryptionn_box.delete("1.0", mn.tkinter.END)

#Clearing each box 
def clear_box():
    #Encryption Box Details
    empty_message_1 = ("Error! The Encryption box or shifter key box is empty")
    moving_text_1 =  encryptionn_box.get("1.0",mn.tkinter.END)
    
    #Decryption Box Details
    empty_message_2 = ("Error! The Decryption box or shifter key box is empty")
    moving_text_2 = decryptionn_box.get("1.0",mn.tkinter.END)

    if empty_message_1 in moving_text_1:
        encryptionn_box.delete("1.0",mn.tkinter.END)
    elif empty_message_2 in moving_text_2:
        decryptionn_box.delete("1.0",mn.tkinter.END)
    else:
        encryptionn_box.delete("1.0",mn.tkinter.END)
        decryptionn_box.delete("1.0",mn.tkinter.END)'''