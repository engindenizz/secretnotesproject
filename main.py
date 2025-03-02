import ui

import base64, hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from tkinter import messagebox


def generate_fernet_key(user_key: bytes) -> bytes:
    salt = hashlib.sha256(user_key).digest()

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     salt=salt,
                     length=32,
                     iterations=100000)
    fernet_key = base64.urlsafe_b64encode(kdf.derive(user_key))
    return fernet_key
def encrypted_message(user_key: str, data: str) -> bytes:
    fernet_key = generate_fernet_key(user_key.encode())
    key = Fernet(fernet_key)
    encrypted_data = key.encrypt(data.encode())
    return encrypted_data


def decrypt_message(user_key: str, encrypted_data: bytes) -> str:
    key = generate_fernet_key(user_key.encode())
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()


def try_encrypt():
    user_key = app.enter_master_key.get().strip()
    title = app.title_enter.get().strip()
    message = app.enter_note.get("1.0", "end").strip()

    if not user_key or not message or not title:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    encrypted = encrypted_message(user_key, message)
    print(encrypted)
    encrypted_text = encrypted.decode()
    print(encrypted_text)

    with open("secret_notes.txt", "a", encoding="utf-8") as file:
        file.write(f"Başlık: {title}\n")
        file.write(f"Şifrelenmiş Mesaj: {encrypted_text}\n")
        file.write("=" * 40 + "\n")

    messagebox.showinfo("Congrats", "Saved Successfully!")

    app.title_enter.delete(0, "end")
    app.enter_note.delete("1.0", "end")
    app.enter_master_key.delete(0, "end")

# 🔓 Butona basınca mesajı çözen fonksiyon
def try_decrypt():
    user_key = app.enter_master_key.get().strip()
    title = app.title_enter.get().strip()

    if not user_key or not title:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        with open("secret_notes.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "Title doesnt found! Please create a note first! 1. create a note first! 2. save it. 3. try again! 4. if you're sure, check your file path'")
        return

    found_title = False
    encrypted_data = None

    for i in range(len(lines)):
        if lines[i].strip() == f"Başlık: {title}":
            found_title = True
            encrypted_data = lines[i + 1].strip().replace("Şifrelenmiş Mesaj: ", "")
            break

    if not found_title or encrypted_data is None:
        messagebox.showerror("Error", "No message found for this title!")
        return

    try:
        decrypted_message = decrypt_message(user_key, encrypted_data.encode())
        app.enter_note.delete("1.0", "end")
        app.enter_note.insert("1.0", decrypted_message)
        messagebox.showinfo("Congrats", "Decrypted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Fail for encrypted message. ")


app = ui.Window()

app.encrypt_button(try_encrypt)
app.decrypt_button(try_decrypt)

app.screen.mainloop()


