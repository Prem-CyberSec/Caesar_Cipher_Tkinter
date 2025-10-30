# Caesar Cipher Tkinter

A Python-based graphical user interface (GUI) application for encrypting and decrypting text using the Caesar cipher and Vigenère cipher methods.

## Description

The Caesar cipher is a simple encryption method that shifts letters by a fixed number of positions in the alphabet. While it's easy to use, it's relatively insecure due to only 26 possible keys. This project also implements the Vigenère cipher, a more secure variant that uses a keyword to determine the shift for each letter.

## Features

- **User-Friendly GUI**: Built with Tkinter for an intuitive user experience
- **Caesar Cipher**: Classic encryption with customizable shift values
- **Vigenère Cipher**: Enhanced security with keyword-based encryption
- **Encryption & Decryption**: Support for both encoding and decoding messages
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Project Structure

```
Caesar_Cipher_Tkinter/
│
├── main.py          # Entry point of the application
├── app.py           # GUI implementation
├── logic.py         # Cipher logic and algorithms
└── README.md        # Project documentation
```

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Prem-CyberSec/Caesar_Cipher_Tkinter.git
```

2. Navigate to the project directory:
```bash
cd Caesar_Cipher_Tkinter
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Launch the application by running `main.py`
2. Enter the text you want to encrypt or decrypt
3. Choose your cipher method (Caesar or Vigenère)
4. For Caesar cipher: Enter the shift value
5. For Vigenère cipher: Enter the keyword
6. Click the appropriate button to encrypt or decrypt your message
7. View the results in the output field

## How It Works

### Caesar Cipher
The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

### Vigenère Cipher
The Vigenère cipher uses a keyword to determine different shift values for each letter. Each letter of the keyword corresponds to a shift value, making it more secure than the basic Caesar cipher.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Author

[Prem-CyberSec](https://github.com/Prem-CyberSec)

## Acknowledgments

- Classic cryptography techniques
- Python Tkinter documentation
- Cryptography enthusiasts community