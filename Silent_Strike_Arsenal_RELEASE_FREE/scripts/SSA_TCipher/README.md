# T-Cipher: C.I Toolkit Module
The T-Cipher module is part of the Creative and Innovative Toolkit (Silent Strike Arsenal). It provides text encryption and decryption functionalities using the AES encryption algorithm.
## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
  - [Encryption](#encryption)
  - [Decryption](#decryption)
- [Security Considerations](#security-considerations)


## Overview
The T-Cipher module allows users to perform text encryption and decryption using the AES encryption algorithm. AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm known for its security and efficiency. This module provides a simple command-line interface for users to encrypt and decrypt messages.

## Usage
To use the T-Cipher module, follow these steps:

### Encryption
1. Run the script: `python t_cipher.py`
2. Choose the `encrypt` mode.
3. Enter the message you want to encrypt.
4. The script will display the generated AES key and the encrypted message.
5. Securely store the generated AES key as it's required for decryption.

### Decryption
1. Run the script: `python t_cipher.py`
2. Choose the `decrypt` mode.
3. Enter the AES key used for encryption.
4. Enter the ciphertext you want to decrypt.
5. The script will attempt to decrypt the ciphertext and display the decrypted result.

## Security Considerations
- **Key Security**: Ensure the generated AES key is securely stored and shared only with trusted parties. Without the key, decryption is not possible.
- **Secure Transmission**: When sharing encrypted text and keys, ensure secure transmission channels to prevent interception.
- **Safe Storage**: Protect decrypted messages from unauthorized access. Delete them securely once they are no longer needed.

