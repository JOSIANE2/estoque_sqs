import os
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.environ.get("ESTOQUE_DB_HOST", "localhost"),
        user=os.environ.get("ESTOQUE_DB_USER", "root"),
        password=os.environ.get("ESTOQUE_DB_PASSWORD", ""),
        database=os.environ.get("ESTOQUE_DB_NAME", "estoque_db"),
    )
