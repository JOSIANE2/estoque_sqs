import tkinter as tk
from tkinter import ttk, messagebox
from produtos import *
from functools import wraps
from mysql.connector import Error as DatabaseError

def tratar_erros(funcao):
    @wraps(funcao)
    def executar(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except ValueError as erro:
            messagebox.showwarning("Dados inválidos", str(erro))
        except DatabaseError:
            messagebox.showerror("Banco de dados", "Não foi possível concluir a operação. Confira o MySQL e a configuração de conexão.")
    return executar


@tratar_erros
def carregar_produtos():
    tabela.delete(*tabela.get_children())
    for item in listar_produtos():
        alerta = ""
        if item[2] <= 5:
            alerta = "⚠ ESTOQUE BAIXO"
        tabela.insert("", "end", values=(item[0], item[1], item[2], item[3], alerta))

@tratar_erros
def adicionar():
    if not nome.get() or not quantidade.get() or not preco.get():
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    inserir_produto(nome.get(), quantidade.get(), preco.get())
    carregar_produtos()

@tratar_erros
def editar():
    selected = tabela.selection()
    if not selected:
        messagebox.showwarning("Atenção", "Selecione um produto.")
        return
    item = tabela.item(selected[0])["values"]
    editar_produto(item[0], nome.get(), quantidade.get(), preco.get())
    carregar_produtos()

@tratar_erros
def excluir():
    selected = tabela.selection()
    if not selected:
        messagebox.showwarning("Atenção", "Selecione um produto.")
        return
    item = tabela.item(selected[0])["values"]
    excluir_produto(item[0])
    carregar_produtos()

@tratar_erros
def entrada():
    selected = tabela.selection()
    if not selected:
        messagebox.showwarning("Atenção", "Selecione um produto.")
        return
    item = tabela.item(selected[0])["values"]
    qtd = qtd_mov.get()
    entrada_produto(item[0], qtd)
    carregar_produtos()

@tratar_erros
def saida():
    selected = tabela.selection()
    if not selected:
        messagebox.showwarning("Atenção", "Selecione um produto.")
        return
    item = tabela.item(selected[0])["values"]
    qtd = qtd_mov.get()

    if not saida_produto(item[0], qtd):
        messagebox.showerror("Erro", "Produto não encontrado ou quantidade insuficiente em estoque!")
    carregar_produtos()

app = tk.Tk()
app.title("Sistema de Estoque - Completo")
app.geometry("800x500")

tk.Label(app, text="Nome:").grid(row=0, column=0)
nome = tk.Entry(app)
nome.grid(row=0, column=1)

tk.Label(app, text="Quantidade:").grid(row=1, column=0)
quantidade = tk.Entry(app)
quantidade.grid(row=1, column=1)

tk.Label(app, text="Preço:").grid(row=2, column=0)
preco = tk.Entry(app)
preco.grid(row=2, column=1)

tk.Button(app, text="Adicionar", command=adicionar).grid(row=3, column=0)
tk.Button(app, text="Editar", command=editar).grid(row=3, column=1)
tk.Button(app, text="Excluir", command=excluir).grid(row=3, column=2)

tk.Label(app, text="Quantidade movimentada:").grid(row=4, column=0)
qtd_mov = tk.Entry(app)
qtd_mov.grid(row=4, column=1)

tk.Button(app, text="Entrada", command=entrada).grid(row=5, column=0)
tk.Button(app, text="Saída", command=saida).grid(row=5, column=1)

colunas = ("ID", "Nome", "Qtd", "Preço", "Alerta")
tabela = ttk.Treeview(app, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
tabela.grid(row=6, column=0, columnspan=5)

carregar_produtos()
app.mainloop()
