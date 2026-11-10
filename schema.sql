-- Instalação inicial de demonstração. Não altera tabelas existentes.
CREATE DATABASE IF NOT EXISTS estoque_db CHARACTER SET utf8mb4;
USE estoque_db;
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(12,2) NOT NULL,
    CHECK (quantidade >= 0),
    CHECK (preco >= 0)
);
