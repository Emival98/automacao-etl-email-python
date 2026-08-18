# 📊 Automação de ETL e Disparo Diário de Relatórios

Sistema automatizado desenvolvido em Python para extração de dados do SQL Server, geração de relatórios tabulares em Excel e distribuição corporativa por e-mail via protocolo SMTP.

## 🚀 Tecnologias Utilizadas
- **Python 3.13**
- **Pandas / OpenPyXL** (Processamento de dados e exportação de planilhas)
- **SQL Server / pyodbc** (Extração de banco de dados)
- **SMTP / Email MIME** (Envio automatizado de e-mails)
- **python-dotenv** (Gestão de variáveis de ambiente e segurança)

## 🛠️ Arquitetura do Fluxo
1. **Extração:** Conexão com o banco de dados SQL Server para consulta do movimento diário.
2. **Transformação e Carga:** Exportação dos dados para arquivo `.xlsx` estruturado na pasta de destino.
3. **Distribuição:** Conexão com servidor SMTP e envio individual para lista de destinatários com cópias e anexo.

## ⚙️ Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
