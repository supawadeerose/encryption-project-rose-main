from Crypto.Cipher import AES
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY").encode()  # 32-byte Key
IV = os.getenv("IV").encode()  # 16-byte IV

print(f"🔑 Key Length: {len(SECRET_KEY)} bytes")
print(f"🔹 IV Length: {len(IV)} bytes")

def encrypt_image(input_file, output_file):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_file, "rb") as f:
        file_data = f.read()

    padding = 16 - (len(file_data) % 16)
    file_data += bytes([padding]) * padding

    encrypted_data = cipher.encrypt(file_data)

    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"🔐 รูปภาพถูกเข้ารหัสแล้ว: {output_file}")

def decrypt_image(input_file, output_file):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    padding = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding]

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"🔓 รูปภาพถูกถอดรหัสแล้ว: {output_file}")

if __name__ == "__main__":
    input_file = "rosetest.png"
    encrypted_file = "rosetes_encrypted.bin"
    decrypted_file = "rosetes_decoded.jpg"

    encrypt_image(input_file, encrypted_file)
    decrypt_image(encrypted_file, decrypted_file)