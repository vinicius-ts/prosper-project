# Descrição da Aplicação

Esta é uma aplicação web desenvolvida com FastAPI que gerencia produtos. A aplicação permite listar, criar, atualizar e deletar produtos em um banco de dados PostgreSQL. A estrutura do projeto inclui módulos para modelos, roteadores e configuração do banco de dados.

## Estrutura do Projeto

- core: Contém a configuração do banco de dados.
- models: Contém os modelos de dados.
- routers: Contém os roteadores da API.
- main.py: Ponto de entrada da aplicação.

## Requisitos

- Docker
- Docker Compose

## Subindo a Aplicação

1. Crie um arquivo .env

 na raiz do projeto com as seguintes variáveis de ambiente:

```env
DB_USER=root
DB_PASSWORD=root
DB_HOST=prosper_db
DB_PORT=5432
DB_NAME=prosperdb
```

2. Construa e inicie os containers Docker:

```sh
docker-compose up --build
```

3. Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

## Endpoints

- `GET /products/`: Lista todos os produtos.
- `GET /products/{product_id}`: Obtém um produto pelo ID.
- `POST /products/`: Cria um novo produto.
- `PUT /products/{product_id}`: Atualiza um produto existente.
- `DELETE /products/{product_id}`: Deleta um produto pelo ID.

## Tecnologias Utilizadas

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

## Comandos Úteis

- Para parar os containers:

```sh
docker-compose down
```

- Para reconstruir os containers:

```sh
docker-compose up --build
```

- Para visualizar os logs:

```sh
docker-compose logs -f
```

## Hospedagem

A API está hospedada em: [API](https://prosper-project-docker.onrender.com/docs)