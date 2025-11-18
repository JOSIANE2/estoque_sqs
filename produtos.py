from database import conectar

def inserir_produto(nome, quantidade, preco):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, quantidade, preco))
    db.commit()
    db.close()

def listar_produtos():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    db.close()
    return produtos

def editar_produto(id, nome, quantidade, preco):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE produtos SET nome=%s, quantidade=%s, preco=%s WHERE id=%s"
    cursor.execute(sql, (nome, quantidade, preco, id))
    db.commit()
    db.close()

def excluir_produto(id):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM produtos WHERE id=%s"
    cursor.execute(sql, (id,))
    db.commit()
    db.close()

def entrada_produto(id, qtd):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE produtos SET quantidade = quantidade + %s WHERE id=%s"
    cursor.execute(sql, (qtd, id))
    db.commit()
    db.close()

def saida_produto(id, qtd):
    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT quantidade FROM produtos WHERE id=%s", (id,))
    atual = cursor.fetchone()[0]

    if qtd > atual:
        db.close()
        return False 

    sql = "UPDATE produtos SET quantidade = quantidade - %s WHERE id=%s"
    cursor.execute(sql, (qtd, id))
    db.commit()
    db.close()
    return True
