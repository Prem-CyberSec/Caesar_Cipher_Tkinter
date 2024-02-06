#Imports
import tkinter


#Main Class
class MainWindow(tkinter.Tk):
    """This is the main window, a child class of tkinter."""
    def __init__(self):
        super().__init__()
        '''The main window properties'''
        #Main window title
        self.title("Cryptographic Cipher")
        #Main Window Geometry 
        self.geometry("714x400")
        #Main Window Color
        self.configure(background="LightBlue")
    
    def encryption(self,message,shifter_key):
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
    
    def decryption(self,message,shifter_key):
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

root_window = MainWindow()
if __name__ == "__main__":
    root_window.mainloop()
