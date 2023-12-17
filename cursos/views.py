from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .permissions import IsSuperUser
# Create your views here.

# O token é criado dessa maneira:
# from django.contri.auth.models import User // importa-se a tabela user do django
# from rest_framework.authtoken.models import Token // importa-se o objeto token de rest_framework
#
# lucas = User.objects.get(id=1) // seleciona-se o usuario
# token = Token.objects.create(user=lucas) // e cria-se o token a partir do usuario
# o token criado ficará dessa maneira:
# Token: a9ebfe556bd3620d71769fbc521d536a36f27117 // a9ebfe556bd3620d71769fbc521d536a36f27117

# Como essa viewset apresenta permissões locais estas se sobrepõe as permissões globais


class CursoViewset(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # permisões locais (modelo 1):
    # permission_classes = (permissions.DjangoModelPermissions,)

    # Este segundo modelo de permissoes locais abrange pontos mais especificos para a permissibilidade
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Este é um exemplo de paginação local
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


'''ViewSet Padrao
class AvaliacaoViewset(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''
# ViewSet Customizada

# Já esta viewset por não apresentar permissões locais esta relegada apenas as permissões globais


class AvaliacaoViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
