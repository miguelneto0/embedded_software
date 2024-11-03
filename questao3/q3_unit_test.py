import unittest
from q3_algoritmoAES import aes_decrypt

class TestAESDecrypt(unittest.TestCase):

    def test_decrypt_valid_message(self):
        """Testa se a mensagem é descriptografada corretamente."""
        ciphertext = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        key = "thisisasecretkey"
        expected_message = "Sistemas Embarcados"
        decrypted_message = aes_decrypt(ciphertext, key)
        self.assertEqual(decrypted_message, expected_message)

    def test_decrypt_with_wrong_key(self):
        """Testa se uma chave incorreta não retorna a mensagem correta."""
        ciphertext = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        wrong_key = "wrongsecretkey!!"
        decrypted_message = aes_decrypt(ciphertext, wrong_key)
        self.assertNotEqual(decrypted_message, "Sistemas Embarcados")

    def test_decrypt_with_invalid_ciphertext(self):
        """Testa se um texto cifrado inválido gera um erro de descriptografia."""
        invalid_ciphertext = "1234abcd"
        key = "thisisasecretkey"
        with self.assertRaises(ValueError):
            aes_decrypt(invalid_ciphertext, key)

    def test_decrypt_with_invalid_key_length(self):
        """Testa se uma chave com comprimento incorreto gera um erro."""
        ciphertext = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        short_key = "shortkey"
        with self.assertRaises(ValueError):
            aes_decrypt(ciphertext, short_key)

# Executa os testes
if __name__ == "__main__":
    unittest.main()
