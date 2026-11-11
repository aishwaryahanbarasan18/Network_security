# 🔐 Secure File Transfer Using Hybrid Cryptography

## 📌 Project Overview
Secure File Transfer Using Hybrid Cryptography is a Network Security mini project developed using Python. It provides a secure way to encrypt and decrypt files using a combination of AES and RSA algorithms.

AES is used to encrypt the file, while RSA is used to securely encrypt the AES secret key.

## 🎯 Objectives
- To provide secure file transfer.
- To protect files from unauthorized access.
- To implement AES and RSA encryption algorithms.
- To maintain data confidentiality and integrity.

## 🛠️ Technologies Used
- Python
- AES-256-GCM
- RSA-2048
- Cryptography Library
- Visual Studio Code

## 🔑 Algorithms Used

### 1. AES (Advanced Encryption Standard)
AES is a symmetric encryption algorithm used to encrypt the original file.

### 2. RSA (Rivest–Shamir–Adleman)
RSA is an asymmetric encryption algorithm used to protect the AES secret key.

## ⚙️ Working Process
1. Generate RSA public and private keys.
2. Select the file to be transferred.
3. Encrypt the file using AES.
4. Encrypt the AES key using the RSA public key.
5. Store the encrypted file.
6. Decrypt the AES key using the RSA private key.
7. Decrypt the file and recover the original content.

## 📂 Project Structure

```text
Secure-File-Transfer/
│
├── app.py
├── README.md
├── requirements.txt
├── keys/
│   ├── public_key.pem
│   └── private_key.pem
├── message.txt
└── message.enc
```

## 💻 Installation

Install Python 3 and run:

```bash
pip install cryptography
```

## ▶️ Execution

**Step 1: Generate RSA Keys**

```bash
python app.py keygen
```

**Step 2: Encrypt the File**

```bash
python app.py encrypt message.txt message.enc
```

**Step 3: Decrypt the File**

```bash
python app.py decrypt message.enc received.txt
```

## ✅ Advantages
- Provides data confidentiality.
- Uses strong encryption algorithms.
- Protects the AES key using RSA.
- AES-GCM provides integrity verification.
- Supports different file types.

## 🏁 Conclusion

This project demonstrates secure file encryption and decryption using hybrid cryptography. By combining AES and RSA algorithms, it provides a practical example of protecting files and maintaining data security during transfer.

## 👨‍💻 Project Details

**Project Title:** Secure File Transfer Using Hybrid Cryptography

**Subject:** Network Security

**Programming Language:** Python

**Project Type:** Mini Project
