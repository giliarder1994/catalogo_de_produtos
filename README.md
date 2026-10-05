# Catálogo de Produtos - API REST com Django

API REST para gerenciamento de catálogo de produtos desenvolvida com **Django** e **Django REST Framework**.

## Funcionalidades

- CRUD completo de **Produtos** e **Categorias**
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
- django-filter
- Pillow (upload de imagens)
- SQLite (banco padrão)

## Endpoints

| Método | Endpoint                    | Descrição                  |
|--------|-----------------------------|----------------------------|
| GET    | `/api/produtos/`            | Lista todos os produtos    |
| POST   | `/api/produtos/`            | Cria um novo produto       |
| GET    | `/api/produtos/{slug}/`     | Detalhe de um produto      |
| PUT    | `/api/produtos/{slug}/`     | Atualiza um produto        |
| PATCH  | `/api/produtos/{slug}/`     | Atualização parcial        |
| DELETE | `/api/produtos/{slug}/`     | Remove um produto          |
| GET    | `/api/categorias/`          | Lista todas as categorias  |
| POST   | `/api/categorias/`          | Cria uma nova categoria    |

### Exemplos de filtros

```
GET /api/produtos/?search=notebook
GET /api/produtos/?categoria=1
GET /api/produtos/?disponivel=true
GET /api/produtos/?ordering=-preco
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
pip install django djangorestframework django-filter pillow
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
├── produtos/              # App principal
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
└── requirements.txt
```

## Autor

Desenvolvido por **Giliarde**
```
