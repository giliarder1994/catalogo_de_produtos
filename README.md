# Catálogo de Produtos - API REST com Django

API REST para gerenciamento de catálogo de produtos com autenticação JWT, desenvolvida com **Django** e **Django REST Framework**.

## Funcionalidades

- CRUD completo de **Produtos** e **Categorias**
- Autenticação com **JWT** (login, registro e refresh token)
- Perfil do usuário logado
- Filtros por categoria e disponibilidade
- Busca por nome e descrição
- Ordenação por preço, nome e data
- Upload de imagem do produto
- Paginação automática
- Documentação interativa (Browsable API do DRF)
- Painel administrativo do Django

## Tecnologias

- Python 3
- Django
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- Pillow
- SQLite

## Endpoints

### Autenticação

| Método | Endpoint                  | Descrição                          | Autenticação |
|--------|---------------------------|------------------------------------|--------------|
| POST   | `/api/auth/register/`     | Criar nova conta                   | Não          |
| POST   | `/api/auth/login/`        | Login (retorna access + refresh)   | Não          |
| POST   | `/api/auth/refresh/`      | Renovar o access token             | Não          |
| GET    | `/api/auth/me/`           | Dados do usuário logado            | Sim          |

### Produtos

| Método | Endpoint                    | Descrição                  | Autenticação |
|--------|-----------------------------|----------------------------|--------------|
| GET    | `/api/produtos/`            | Lista todos os produtos    | Não          |
| POST   | `/api/produtos/`            | Cria um novo produto       | Sim          |
| GET    | `/api/produtos/{slug}/`     | Detalhe de um produto      | Não          |
| PUT    | `/api/produtos/{slug}/`     | Atualiza um produto        | Sim          |
| PATCH  | `/api/produtos/{slug}/`     | Atualização parcial        | Sim          |
| DELETE | `/api/produtos/{slug}/`     | Remove um produto          | Sim          |

### Categorias

| Método | Endpoint                    | Descrição                  | Autenticação |
|--------|-----------------------------|----------------------------|--------------|
| GET    | `/api/categorias/`          | Lista todas as categorias  | Não          |
| POST   | `/api/categorias/`          | Cria uma nova categoria    | Sim          |

### Exemplos de filtros

```
GET /api/produtos/?search=notebook
GET /api/produtos/?categoria=1
GET /api/produtos/?disponivel=true
GET /api/produtos/?ordering=-preco
```

## Como usar a autenticação

### 1. Registrar um usuário

```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "giliarde",
  "email": "teste@email.com",
  "password": "senha123",
  "password2": "senha123",
  "first_name": "Giliarde",
  "last_name": "Silva"
}
```

### 2. Fazer login

```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "name",
  "password": "senha123"
}
```

Resposta:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```

### 3. Usar o token

Nas requisições protegidas, envie o header:

```
Authorization: Bearer SEU_ACCESS_TOKEN
```

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/catalogo-de-produtos.git
cd catalogo-de-produtos
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django djangorestframework djangorestframework-simplejwt django-filter pillow
```

### 4. Aplique as migrations

```bash
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor

```bash
python manage.py runserver
```

Acesse:

- **API**: http://127.0.0.1:8000/api/
- **Admin**: http://127.0.0.1:8000/admin/

## Estrutura do projeto

```
catalogo_produtos/
├── catalogo_produtos/     # Configurações do projeto
├── produtos/              # App de produtos e categorias
├── usuarios/              # App de autenticação e usuários
├── manage.py
└── requirements.txt
```

## Autor

Desenvolvido por **Giliarde**
