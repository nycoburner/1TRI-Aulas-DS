import tkinter as tk

def login():
    if input_email.get() == "Nycobendy":
        if input_senha.get() == "#Hope123":
            print("Login realizado!")
        else:
            print("login falhado")
    else:
        print("Login falhado...")

app = tk.Tk()
app.title("Login Page")
app.geometry("400x300")

label_email = tk.Label(app,text="Email:")
label_email.pack(pady=5)
input_email = tk.Entry(app)
input_email.pack()

label_senha = tk.Label(app,text="Senha:")
label_senha.pack(pady=5)
input_senha = tk.Entry(app, show="*")
input_senha.pack()



botao = tk.Button(app, text="Enviar", command=login)
botao.pack(pady=10)

app.mainloop()