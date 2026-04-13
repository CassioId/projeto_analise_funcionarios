import sqlite3
import pandas as pd

# Função para classificar salários
def classificar_salario(salario):
    if salario < 3000:
        return "Baixo"
    elif salario <= 6000:
        return "Médio"
    else:
        return "Alto"


# Conectar ao banco de dados
conexao = sqlite3.connect("funcionarios.db")
cursor = conexao.cursor()

# Criar a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    salario REAL NOT NULL
)
""")

print("\n=== Sistema de Cadastro de Funcionários ===")

# Loop para cadastro de funcionários
while True:
    print("\nDigite os dados do funcionário:")

    nome = input("Nome: ").strip()
    if not nome:
        print("❌ O nome não pode ser vazio.")
        continue

    # Validação do salário
    try:
        salario = float(input("Salário: R$ ").replace(",", "."))
    except ValueError:
        print("❌ Salário inválido! Tente novamente.")
        continue

    # Inserir dados no banco
    cursor.execute(
        "INSERT INTO funcionarios (nome, salario) VALUES (?, ?)",
        (nome, salario)
    )
    conexao.commit()

    classificacao = classificar_salario(salario)
    print(f"✅ Funcionário cadastrado com sucesso! Classificação: {classificacao}")

    # Perguntar se deseja continuar
    continuar = input("\nDeseja cadastrar outro funcionário? (s/n): ").strip().lower()
    if continuar != 's':
        print("\nCadastro finalizado.")
        break

# Exibir os dados classificados
print("\n📋 Funcionários cadastrados:")
cursor.execute("""
SELECT 
    id,
    nome,
    salario,
    CASE
        WHEN salario < 3000 THEN 'Baixo'
        WHEN salario BETWEEN 3000 AND 6000 THEN 'Médio'
        ELSE 'Alto'
    END AS classificacao
FROM funcionarios
""")

dados = cursor.fetchall()

print("\nID | Nome | Salário | Classificação")
print("-" * 45)
for funcionario in dados:
    print(funcionario)

# Exportar para Excel com classificação
df = pd.read_sql_query("""
SELECT 
    id,
    nome,
    salario,
    CASE
        WHEN salario < 3000 THEN 'Baixo'
        WHEN salario BETWEEN 3000 AND 6000 THEN 'Médio'
        ELSE 'Alto'
    END AS classificacao
FROM funcionarios
""", conexao)

df.to_excel("relatorio_funcionarios.xlsx", index=False)

print("\n📊 Relatório exportado para 'relatorio_funcionarios.xlsx'.")

# Fechar conexão
conexao.close()
print("🔒 Conexão com o banco de dados encerrada.")