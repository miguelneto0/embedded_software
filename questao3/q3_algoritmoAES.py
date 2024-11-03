from Crypto.Cipher import AES
import binascii

def pkcs7_unpad(data: bytes) -> bytes:
    """Remove o padding PKCS7."""
    padding_len = data[-1]
    return data[:-padding_len]

def aes_decrypt(ciphertext_hex: str, key: str) -> str: 
    key_bytes = key.encode('utf-8')                                    # Converte a chave e o texto cifrado em bytes
    ciphertext_bytes = binascii.unhexlify(ciphertext_hex)
    
    cipher = AES.new(key_bytes, AES.MODE_ECB)                          # Cria o objeto AES no modo ECB
    
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)                 # Decifra a mensagem e remove o padding
    # decrypted_text = decrypted_bytes.decode('utf-8').rstrip("\x00")  # Remove padding de NULL bytes
    unpadded_bytes = pkcs7_unpad(decrypted_bytes)
    decrypted_text = unpadded_bytes.decode('utf-8')
    
    return decrypted_text

# Entrada da questao 3
ciphertext = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
key = "thisisasecretkey"

# Execução
decrypted_message = aes_decrypt(ciphertext, key)
print("Mensagem decifrada:", decrypted_message)
