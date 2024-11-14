import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import socketio
import os

# Configurações iniciais
server_url = "http://localhost:5000"
user_id = None

# Diretório onde os arquivos serão baixados
DOWNLOAD_DIR = 'downloads'
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Configuração do SocketIO
sio = socketio.Client()

class FileShareClient:
    def __init__(self, master):
        self.master = master
        master.title("P2P File Sharing Client")
        
        # ID do usuário
        self.user_id_label = tk.Label(master, text="User ID:")
        self.user_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.user_id_entry = tk.Entry(master)
        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Botão de Registro
        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Botão para Compartilhar Arquivo
        self.share_button = tk.Button(master, text="Share File", command=self.share_file)
        self.share_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        
        # Botão para Consultar Arquivos
        self.list_button = tk.Button(master, text="List Files", command=self.list_files)
        self.list_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        
        # Área de Exibição dos Arquivos
        self.files_listbox = tk.Listbox(master, width=50)
        self.files_listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        
        # Botão para Baixar Arquivo
        self.download_button = tk.Button(master, text="Download File", command=self.download_file)
        self.download_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        
    def register(self):
        global user_id
        user_id = self.user_id_entry.get()
        if not user_id:
            messagebox.showerror("Error", "Please enter a User ID.")
            return
        
        # Envia o ID para o servidor
        try:
            response = requests.post(f"{server_url}/register", json={"user_id": user_id, "address": "localhost"})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Registered successfully!")
            else:
                messagebox.showerror("Error", "Failed to register.")
        except requests.RequestException:
            messagebox.showerror("Error", "Could not connect to server.")
        
    def share_file(self):
        if not user_id:
            messagebox.showerror("Error", "Please register first.")
            return
        
        file_path = filedialog.askopenfilename()  # Corrigido: agora está dentro do método
        if file_path:
            file_name = os.path.basename(file_path)
            try:
                with open(file_path, 'rb') as file:
                    files = {'file': file}
                    data = {'user_id': user_id, 'file_name': file_name}
                    response = requests.post(f"{server_url}/share", files=files, data=data)
                    if response.status_code == 200:
                        messagebox.showinfo("Success", f"File '{file_name}' shared successfully!")
                    else:
                        messagebox.showerror("Error", "Failed to share file.")
            except requests.RequestException:
                messagebox.showerror("Error", "Could not connect to server.")

                
    def list_files(self):
        try:
            response = requests.get(f"{server_url}/files")
            if response.status_code == 200:
                files = response.json()
                self.files_listbox.delete(0, tk.END)
                for file, users in files.items():
                    self.files_listbox.insert(tk.END, f"{file} - shared by: {', '.join(users)}")
            else:
                messagebox.showerror("Error", "Failed to retrieve files.")
        except requests.RequestException:
            messagebox.showerror("Error", "Could not connect to server.")
    
    def download_file(self):
        selected_file = self.files_listbox.get(tk.ACTIVE)
        if selected_file:
            file_name = selected_file.split(" -")[0]
            try:
                response = requests.get(f"{server_url}/downloads/{file_name}")
                if response.status_code == 200:
                    file_path = os.path.join(DOWNLOAD_DIR, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    messagebox.showinfo("Success", f"File '{file_name}' downloaded successfully!")
                else:
                    messagebox.showerror("Error", "Failed to download file.")
            except requests.RequestException:
                messagebox.showerror("Error", "Could not connect to server.")

root = tk.Tk()
client = FileShareClient(root)
root.mainloop()
