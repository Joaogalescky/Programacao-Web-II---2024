from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, MedicamentoViewSet, PrescricaoViewSet, RegistroViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'prescricoes', PrescricaoViewSet)
router.register(r'registros', RegistroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prescricoes/cadastrar_prescricao_com_medicamento/', PrescricaoViewSet.as_view({'post': 'cadastrar_prescricao_com_medicamento'})),
]