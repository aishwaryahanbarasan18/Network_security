
import os
import argparse
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_DIR = Path("keys")
KEY_DIR.mkdir(exist_ok=True)


# Generate RSA public and private keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    (KEY_DIR / "private_key.pem").write_bytes(private_pem)
    (KEY_DIR / "public_key.pem").write_bytes(public_pem)

    print("RSA Keys Generated Successfully!")


# Encrypt file using AES and RSA
def encrypt_file(input_file, output_file):
    public_key = serialization.load_pem_public_key(
        Path("keys/public_key.pem").read_bytes()
    )

    aes_key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)

    plaintext = Path(input_file).read_bytes()

    ciphertext = AESGCM(aes_key).encrypt(
        nonce, plaintext, None
    )

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    output = (
        len(encrypted_key).to_bytes(4, "big")
        + encrypted_key
        + nonce
        + ciphertext
    )

    Path(output_file).write_bytes(output)

    print("File Encrypted Successfully!")


# Decrypt received file
def decrypt_file(input_file, output_file):
    private_key = serialization.load_pem_private_key(
        Path("keys/private_key.pem").read_bytes(),
        password=None
    )

    data = Path(input_file).read_bytes()

    key_length = int.from_bytes(data[:4], "big")

    encrypted_key = data[4:4 + key_length]
    nonce = data[4 + key_length:16 + key_length]
    ciphertext = data[16 + key_length:]

    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    plaintext = AESGCM(aes_key).decrypt(
        nonce, ciphertext, None
    )

    Path(output_file).write_bytes(plaintext)

    print("File Decrypted Successfully!")


# Main program
def main():
    parser = argparse.ArgumentParser(
        description="Secure File Transfer Using Hybrid Cryptography"
    )

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("keygen")

    enc = sub.add_parser("encrypt")
    enc.add_argument("input")
    enc.add_argument("output")

    dec = sub.add_parser("decrypt")
    dec.add_argument("input")
    dec.add_argument("output")

    args = parser.parse_args()

    if args.command == "keygen":
        generate_keys()

    elif args.command == "encrypt":
        encrypt_file(args.input, args.output)

    elif args.command == "decrypt":
        decrypt_file(args.input, args.output)


if __name__ == "__main__":
    main()
