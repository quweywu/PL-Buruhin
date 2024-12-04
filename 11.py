import requests
import json
import tkinter as tk
from tkinter import messagebox
#spark
def get_repo_info(repo_name):
    link = f'https://api.github.com/repos/apache/{repo_name}'
    response = requests.get(link)
    if response.status_code == 200:
        repo_data = response.json()
        repo_info = {
            'company': None,
            'created at': repo_data.get('created_at'),
            'email': None,
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': repo_data.get('html_url') 
        }
        return repo_info
    else:
        messagebox.showerror('Ошибка', 'Репозиторий не обнаружен')
def button_click():
    repo_name = entry.get()
    if repo_name:
        repo_info = get_repo_info(repo_name)
        if repo_info:
            with open(f'{repo_name}_info.json', 'w') as json_file:
                json.dump(repo_info, json_file, indent=4)
            messagebox.showinfo("Отлично", f"В файл сохранена информация о репозитории '{repo_name}_info.json'")
    else:
         messagebox.showwarning("Предупреждение", "Введите имя репозитория.")
root = tk.Tk()
root.title('repo info')
tk.Label(root, text='Введите имя репозитория:', ).pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Вывести информацию", command=button_click)
button.pack(pady=20)
root.mainloop()