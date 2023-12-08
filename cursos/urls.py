from django.urls import path
from .views import AvaliacaoViewset, CursoViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewset)
router.register('avaliacoes', AvaliacaoViewset)
