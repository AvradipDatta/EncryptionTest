from cryptography.fernet import Fernet
import base64

# Generate a key (do this once and save securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a file
with open('input_file.mp4', 'rb') as f:
    data = f.read()

encrypted_data = cipher.encrypt(data)

# Save encrypted data
with open('encrypted_file.enc', 'wb') as f:
    f.write(encrypted_data)

print(f"Encryption done. Key: {key.decode()}")


# Encode to base64
encoded_text = base64.b64encode(encrypted_data).decode()

# Save as a text file
with open('encrypted_file.txt', 'w') as f:
    f.write(encoded_text)

print("Encoded text file ready for GitHub push.")
