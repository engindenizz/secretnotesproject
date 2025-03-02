import customtkinter as ctk
from PIL import Image
import os
import customtkinter



class Window():
    def __init__(self):
        self.screen = ctk.CTk()
        self.screen.geometry('450x700')
        self.screen.title('SecretNotes')
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_columnconfigure(1, weight=1)
        self.image_label()
        self.title_label()
        self.entry_label()
        self.master_key_label()

        self.encrypt_btn = ctk.CTkButton(self.screen, text='Save & Encrypt', command=None)
        self.encrypt_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.decrypt_btn = ctk.CTkButton(self.screen, text='Decrypt', command=None)
        self.decrypt_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10)



    def image_label(self):
        IMAGE_WITDH = 100
        IMAGE_HEIGHT = 100
        IMAGE_PATH = "image.png"
        secret_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WITDH, IMAGE_HEIGHT))
        label = customtkinter.CTkLabel(master=self.screen, image=secret_image, text='')
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    def title_label(self):
       title_label = ctk.CTkLabel(self.screen, text='Enter your Title')
       title_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
       self.title_enter = ctk.CTkEntry(self.screen)
       self.title_enter.grid(row=2, column=0,columnspan=2, padx=10, pady=10)
    def entry_label(self):
        enter_note_label = ctk.CTkLabel(self.screen, text='Enter you Secret')
        enter_note_label.grid(row=3, column=0, columnspan=2,padx=10, pady=10)
        self.enter_note = ctk.CTkTextbox(self.screen, padx=10, pady=10, height=150, width=240)
        self.enter_note.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
    def master_key_label(self):
        enter_master_key_label = ctk.CTkLabel(self.screen, text='Enter Master Key')
        enter_master_key_label.grid(row=5, column=0,columnspan=2, padx=10, pady=10)
        self.enter_master_key = ctk.CTkEntry(self.screen)
        self.enter_master_key.grid(row=6, column=0,columnspan=2, padx=10, pady=10)


    def encrypt_button(self, command):
        self.encrypt_btn.configure(command=command)

    def decrypt_button(self, command):
        self.decrypt_btn.configure(command=command)



