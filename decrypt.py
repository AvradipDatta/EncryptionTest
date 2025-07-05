from cryptography.fernet import Fernet
import base64
# Load key
cipher = Fernet("79eH9tgYume-sf4v9srfXjrK4hKEnZ908xDaNlbhtd8=")    #replace 'key' with your actual key

# Read encoded text
with open('encrypted_file.txt', 'r') as f:
    encoded_text = f.read()

# Decode from base64
encrypted_data = base64.b64decode(encoded_text.encode())

# Decrypt
original_data = cipher.decrypt(encrypted_data)

# Save the original file
with open('restored_file.mp4', 'wb') as f:
    f.write(original_data)

print("File restored successfully.")
