# 📊 Sistema de Análise de Funcionários

## 📌 Descrição

O **Sistema de Análise de Funcionários** é um projeto desenvolvido em Python com o objetivo de coletar, armazenar e analisar dados de colaboradores. A aplicação utiliza banco de dados SQLite para persistência das informações e gera relatórios em Excel para apoio à tomada de decisões.

Este projeto integra conceitos de programação, análise de dados e manipulação de bancos de dados, sendo ideal para fins acadêmicos e profissionais.

---

## 🚀 Tecnologias Utilizadas

- **Python** – Linguagem principal do projeto
- **SQLite** – Banco de dados leve e integrado
- **Pandas** – Manipulação e análise de dados
- **OpenPyXL** – Geração de relatórios em Excel
- **Microsoft Excel** – Visualização e análise dos resultados

---

## 📁 Estrutura do Projeto


projeto_analise_funcionarios/
│── script.py
│── funcionarios.db
│── relatorio_funcionarios.xlsx
│── README.md
│── requirements.txt


| Arquivo                          | Descrição                                               |
|----------------------------------|---------------------------------------------------------|
| **script.py**                    | Script principal do sistema                             |
| **funcionarios.db**              | Banco de dados SQLite com os registros dos funcionários |
| **relatorio_funcionarios.xlsx**  | Relatório gerado automaticamente em Excel               |
| **README.md**                    | Documentação do projeto                                 |
| **requirements.txt**             | Dependências do projeto                                 |

---

## 📊 Funcionalidades

- ✔️ Cadastro de funcionários
- ✔️ Armazenamento em banco de dados SQLite
- ✔️ Consulta e visualização de informações
- ✔️ Classificação automática de salários
- ✔️ Análise de dados com Pandas
- ✔️ Exportação de relatórios para Excel

---

## 💰 Classificação Salarial

| Faixa Salarial            | Classificação |
|---------------------------|---------------|
| Menor que R$ 3.000        |     Baixo     |
| Entre R$ 3.000 e R$ 6.000 |     Médio     |
| Acima de R$ 6.000         |     Alto      |

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.11 ou superior
- Pip (gerenciador de pacotes do Python)

Verifique a instalação com:

```bash
python --version
pip --version

▶️ Como Executar
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/projeto_analise_funcionarios.git
cd projeto_analise_funcionarios
2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado)

🔹 Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate

🔹 Linux/Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Instale as dependências
pip install -r requirements.txt

Caso o arquivo ainda não exista:

pip install pandas openpyxl
📈 Exemplo de Saída

Após a execução do programa, serão gerados:

📄 funcionarios.db – Banco de dados com os registros cadastrados
📊 relatorio_funcionarios.xlsx – Relatório em Excel com a análise dos dados
📦 Arquivo requirements.txt

Crie um arquivo chamado requirements.txt na raiz do projeto com o seguinte conteúdo:
- pandas
- openpyxl

🎯 Objetivos do Projeto
- Aplicar conceitos de programação em Python
- Integrar Python com banco de dados SQLite
- Desenvolver habilidades em análise de dados com Pandas
- Gerar relatórios automatizados em Excel
- Consolidar conhecimentos em Ciência e Análise de Dados

Autor
👨‍💻 Cássio Idelân Costa dos Santos
📍 Curitiba – PR, Brasil
🎓 Estudante de Engenharia de Software
🏢 Fundador da Tech Idel Group

📄 Licença

Projeto
- Este projeto é destinado a fins educacionais e acadêmicos.

⭐ Contribuição

Se este projeto foi útil para você, considere deixar uma estrela no repositório!
- git add .
- git commit -m "Adiciona documentação do projeto"
- git push origin main

🔗 Contato
📧 Email: cassioidelan@gmail.com
💼 LinkedIn: https://www.linkedin.com/
🐙 GitHub: https://github.com/seu-usuario

---