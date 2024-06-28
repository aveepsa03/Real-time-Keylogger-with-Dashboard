from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Commonly used public exponent
    key_size=2048,          # Key size in bits; 2048 bits is a good balance of security and performance
)

# Generate public key
public_key = private_key.public_key()  # Derive the public key from the private key

# Save the private key to a file
with open("private_key.pem", "wb") as private_key_file:  # Open a file in write-binary mode to save the private key
    private_key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,            # Encode the key in PEM format
        format=serialization.PrivateFormat.TraditionalOpenSSL,  # Use the traditional OpenSSL format for the private key
        encryption_algorithm=serialization.NoEncryption()  # No encryption for the private key file
    ))

# Save the public key to a file
with open("public_key.pem", "wb") as public_key_file:  # Open a file in write-binary mode to save the public key
    public_key_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,            # Encode the key in PEM format
        format=serialization.PublicFormat.SubjectPublicKeyInfo  # Use the SubjectPublicKeyInfo format for the public key
    ))

print("Public and private keys generated and saved to 'public_key.pem' and 'private_key.pem'")  # Confirmation message
