from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'criacao',
            'comentario',
            'avaliacao',
            'ativo'
        ]


class CursoSerializer(serializers.ModelSerializer):
    # As relaçoes entre tabelas podem ser mostradas de diferentes maneiras como se segue abaixo:

    # 1. Nested Relationship:(Este mostra todos os dados da tabela relacionada a esta)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2. Hyperlinked Related Fields(Este mostra um link que leva a tabela relacionada):
    '''avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='avaliacao-detail')'''

    # 3. Primary Key Related Fields(Este mostra a primary key da tabela relacionada):
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        ]
