#imports
import main as mn
#logical functions
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
        decryptionn_box.delete("1.0",mn.tkinter.END)

#GuI stuff
#Create a title
placeholder_label = mn.tkinter.Label(text = "\t\t", font = ("times",20))
placeholder_label.grid(row=0, column=0)

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times",20))
title_label.grid(row=0, column=1)

placeholder_label = mn.tkinter.Label(text = "\t\t", font = ("times",20))
placeholder_label.grid(row=0, column=2)

#Encryption Part
#Encryption_message
encryptionn_message = mn.tkinter.Label(text = "Encrypt", font = ("times", 16), pady = 20, bg = "light blue")
encryptionn_message.grid(row = 1, column = 0, sticky = mn.tkinter.N)

#Encryption_box
encryptionn_box = mn.tkinter.Text(height = 6, width = 20, font = ("times", 16))
encryptionn_box.grid(row = 2, column = 0, sticky = mn.tkinter.W)

#Encryption_button
encryptionn_button = mn.tkinter.Button(text = "ENCRYPT", font = ("times", 12), pady = 10, command = move_text_to_decryption_box)
encryptionn_button.grid(row = 3, column = 0, sticky = mn.tkinter.N)


#Decryption Part
#Decryption_message
decryptionn_message = mn.tkinter.Label(text = "Decrypt", font = ("times", 16), pady = 20, bg = "light blue")
decryptionn_message.grid(row = 1, column = 2, sticky = mn.tkinter.N)

#Decryption_Box
decryptionn_box = mn.tkinter.Text(height = 6, width = 20, font = ("times", 16))
decryptionn_box.grid(row = 2, column = 2, sticky = mn.tkinter.E)

#Decryption_button
decryption_button = mn.tkinter.Button(text = "DECRYPT", font = ("times", 12), pady = 10, command = move_text_to_encryption_box)
decryption_button.grid(row = 3, column = 2, sticky = mn.tkinter.N)

#Shifter Key Part
#Shifter key title
shifter_key = mn.tkinter.Label(text = "Shifter Key / Keyword", font  = ("times", 15), bg = "light blue")
shifter_key.grid(row = 1, column = 1, sticky= mn.tkinter.N)

#Shifter Key Box
shifter_key_box = mn.tkinter.Text(height = 2, width = 8, font = ("times", 15))
shifter_key_box.grid(row = 2, column = 1,sticky= mn.tkinter.N)

#Clear Button
clear_button = mn.tkinter.Button(text = "Clear", font = ("times", 15), pady = 10, command = clear_box)
clear_button.grid(row = 4, column = 1, sticky = mn.tkinter.N)


#Looping the program
if __name__ == "__main__":
    mn.root_window.mainloop()
