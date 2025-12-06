from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, RelatorioSQL, dashboard_view, lista_alunos_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
        title="API de Gestão Acadêmica",
        default_version='v1',
        description="Documentação da API para o sistema de gestão acadêmica.",
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/relatorio_sql/', RelatorioSQL.as_view(), name='relatorio_sql'),
    path('', dashboard_view, name='dashboard'), 
    path('alunos/', lista_alunos_view, name='lista_alunos'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]