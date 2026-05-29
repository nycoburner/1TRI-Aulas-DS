import tkinter as tk
from conta import Conta
import json
def Cadastrar():

    conta = Conta(input_titular.get(), input_agencia.get() input_cpf.get()) 
    with open("clientes.json", "r") as clientes_arq
        clientes = json.load(clientes_arq)
    
    clientes_append({
        "titular": conta.titular,
        "agencia": conta.agencia,
        "numero": conta.numero
        "cpf":conta.cpf,
        "saldo":conta.saldom,
        "senha":conta.senha,
        "chavepix":conta.chavepix
    })
    with open("clientes.json", "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)
    label_resposta.configure(
        text=f"Conta: {conta.numero} Titular: {conta.titular} cadastrado com sucesso!",
        fg="green")

    app = tk.Tk()
    app.title("Banco Red Dessert")
    app.geometry("400x300")

    label_agencia = tk.Label(app,text="Agencia:")
    label_agencia.pack(pady=5)
    input_agencia = tk.Entry(app)
    input_agencia.pack()

    label_senha = tk.Label(app,text="Senha:")
    label_senha.pack(pady=5)
    input_senha = tk.Entry(app, show="*")
    input_senha.pack()

    label_cpf = tk.Label(app,text="CPF:")
    label_cpf.pack(pady=5)
    input_cpf = tk.Entry(app)
    input_cpf.pack()

    botao = tk.Button(app, text="Enviar", command=login)
    botao.pack(pady=10)

app.mainloop()