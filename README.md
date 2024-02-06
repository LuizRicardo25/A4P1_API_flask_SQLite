# Projeto Aula Flask com SQLite

Este projeto é uma introdução prática à criação de aplicações web com Flask e ao uso do SQLite como sistema de gerenciamento de banco de dados. Aqui, você aprenderá a configurar um projeto Flask, a interagir com um banco de dados e a versionar seu código usando o Git e o GitHub.

## Como começar

Siga os passos abaixo para configurar seu ambiente de desenvolvimento e começar a trabalhar no seu projeto Flask.

### Passo 1: Criar um Repositório no GitHub

1. Faça login na sua conta do GitHub.
2. Clique no ícone `+` no canto superior direito e selecione _New repository_.
3. Dê um nome ao seu repositório e adicione uma breve descrição.
4. Selecione se você deseja um repositório público ou privado.
5. Inicialize o repositório com um arquivo README, se desejar.
6. Clique em _Create repository_.

### Passo 2: Clonar o Repositório

Abra o terminal ou prompt de comando e execute:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
Substitua https://github.com/seu-usuario/seu-repositorio.git pelo URL do repositório que você acabou de criar.

### Passo 3: Configurar o Ambiente Virtual
Dentro do diretório do projeto, execute:

```bash
python -m venv venv
```
Isso criará um novo ambiente virtual dentro do diretório venv.

### Passo 4: Ativar o Ambiente Virtual
No Windows, use:

```cmd
venv\Scripts\activate
```

No macOS ou Linux, use:

```bash
source venv/bin/activate
```

### Passo 5: Instalar Dependências
Com o ambiente virtual ativado, instale o Flask e outras dependências necessárias:

```bash
pip install flask flask_sqlalchemy
```

### Passo 6: Estrutura do Projeto
Sua estrutura de projeto deve ser semelhante a esta:

```
eu-projeto/
│
├── venv/
│ ├── include/
│ ├── lib/
│ └── scripts/
├── app.py
├── models.py
├── create_db.py
└── README.md
```

### Passo 7: Executar a Aplicação
Para executar a aplicação, use:

```bash
python app.py
```

A aplicação deve estar acessível através do navegador em http://localhost:5000.

### Passo 8: Versionamento com Git
Para adicionar suas alterações ao Git, use os seguintes comandos:

```bash
git add .
git commit -m "Primeiro commit com o projeto Flask"
git push
```

Contribuição
Para contribuir com o projeto, faça um fork do repositório, faça suas alterações e crie um Pull Request.