from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'slug', 'descricao']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset = Categoria.objects.all(),
        source = 'categoria',
        write_only = True
    )

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'slug', 'descricao', 'preco',
            'estoque', 'disponivel', 'categoria', 'categoria_id',
            'imagem', 'criado_em', 'atualizado_em'
        ]