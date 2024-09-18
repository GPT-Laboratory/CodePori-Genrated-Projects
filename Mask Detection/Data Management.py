class SecureDataHandler:
    def __init__(self, key, encryption_algo=Fernet):
        self.key = key
        self.encryption_algo = encryption_algo(key)

    def encrypt_and_save(self, filename: str):
        with open(filename, 'rb') as file:
            data = file.read()

        token = self.encryption_algo.encrypt(data)

        # Save the token in-memory and return it
        return token

    def save_encrypted(self, filename: str, data: bytes):
        # Save the encrypted token to file
        with open(filename, 'wb') as file:
            file.write(data)

    def backup(self, filename):
        shutil.copy(filename, filename + '.backup')

    def load_encrypted(self, data: bytes):
        # Decrypt the in-memory data
        decrypted_token = self.encryption_algo.decrypt(data)
        return decrypted_token

    def export(self, filename, decrypted=False):
        if decrypted:
            filename = self.load_encrypted(filename)

        return pd.read_csv(filename)
