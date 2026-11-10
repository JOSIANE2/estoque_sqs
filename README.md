# Controle de estoque

Aplicação de estudo em Python com interface Tkinter e banco MySQL. Cadastra, edita e exclui produtos, movimenta quantidades e sinaliza estoque baixo (até 5 unidades).

## Preparar ambiente
1. Instale Python 3, Tkinter e MySQL.
2. Crie um ambiente virtual: python -m venv .venv e ative-o.
3. Instale as dependências: python -m pip install -r requirements.txt.
4. Em um MySQL de demonstração, execute schema.sql pelo cliente de sua preferência. Não execute sobre banco de produção.
5. Configure as variáveis ESTOQUE_DB_HOST, ESTOQUE_DB_USER, ESTOQUE_DB_PASSWORD e ESTOQUE_DB_NAME no ambiente. Prefira usuário dedicado ao banco; não coloque senha no código. Os padrões locais mantêm compatibilidade com o projeto original.
6. Execute python app.py.

## Validações
Quantidade de cadastro inteira e não negativa; movimentação inteira e maior que zero; nome obrigatório; preço finito, não negativo e com até duas casas decimais.

## Limitações
Projeto de demonstração sem autenticação, histórico de movimentações ou suporte seguro a movimentações concorrentes. A rotina de saída ainda faz leitura e atualização separadas. O script SQL é uma instalação inicial, não uma migração de banco existente. Integração com MySQL e interface gráfica precisam de teste no ambiente de uso.

## Créditos
Repositório mantido por JOSIANE2. A revisão do código e da documentação contou com assistência de IA.
