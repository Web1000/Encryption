import string

PLAIN = "abcdefghijklmnopqrstuvwxyz"
CYPHER = "/.,mnbvcxz';lkjhgfdsa][poi"

enc_map = {p: c for p , c in zip(PLAIN, CYPHER)}
dec_map = {c: p for p, c in zip(PLAIN,CYPHER)}

def translate(text, mapping):
    out = []
    for ch in text:
        if ch.isalpha():
            is_lower = ch.islower()
            base = ch.lower()
            mapped = mapping[ch.lower()]
            out.append(mapped if is_lower else mapped.upper())
        else:
            out.append(ch)
    return "".join(out)

def encrypt(text):
    return translate(text, enc_map)

def decrypt(text):
    return translate(text, dec_map)

if __name__ == "__main__":
    print("=== Simple Message Translator ===")
    print("This uses a substitution key:\n")
    print(f"Plain : {PLAIN}")
    print(f"Cipher: {CYPHER}")
    print("-" * 40)

while True:
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Q to quit): ").strip().lower()
    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == 'e':
        msg = input("Enter the message to encrypt: ")
        print("Encrypted:", encrypt(msg))
    elif choice == 'd':
        msg = input("Enter the message to decrypt: ")
        print("Decrypted:", decrypt(msg))
    else:
        print("Invalid choice! Please type E, D, or Q.")
        print("-" * 40)





