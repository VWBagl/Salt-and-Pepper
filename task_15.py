class BlockTranspositionCipher:
    def __init__(self, text: str, key: str, decrypt: bool = False):
        self.text = text
        self.key = key
        self.decrypt = decrypt
        self._validate_key()
        self.block_size = len(self.key)
        self.numeric_key = self._key_to_numeric()
        self.permutation = self._get_permutation()

    def _validate_key(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key_lower = self.key.lower()

        for char in key_lower:
            if char not in alphabet:
                raise ValueError("Ключ должен состоять только из букв английского алфавита.")
    
        if len(key_lower) != len(set(key_lower)):
            raise ValueError("Все символы ключа должны быть уникальными (регистр не учитывается).")

    def _key_to_numeric(self):
        return [ord(let.lower()) - ord('a') for let in self.key]

    def _get_permutation(self):
        return self.numeric_key

    def __iter__(self):
        return self._process_blocks()

    def _process_blocks(self):
        block_size = self.block_size
        padded_text = self.text
        if len(padded_text) % block_size != 0:
            pad_len = block_size - (len(padded_text) % block_size)
            padded_text += ' ' * pad_len

        blocks = []
        for i in range(0, len(padded_text), block_size):
            block = padded_text[i:i + block_size]
            blocks.append(block)

        for block in blocks:
            if self.decrypt:
                decrypted_block = [''] * block_size
                for enc_pos in range(block_size):
                    orig_pos = self.permutation[enc_pos]
                    if orig_pos < block_size:
                        decrypted_block[orig_pos] = block[enc_pos]
                yield ''.join(decrypted_block)
            else:
                encrypted_block = ''.join(block[i] for i in self.permutation if i < block_size)
                yield encrypted_block