from django.urls import path
from .views import (
    UsuarioView, UsuarioReadUpdateDeleteView, 
    MedicamentoView, MedicamentoReadUpdateDeleteView,
    PrescricaoCreateWithMedicamentoView
)

urlpatterns = [
    # Endpoints para usuário
    path('usuarios/', UsuarioView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:id>/', UsuarioReadUpdateDeleteView.as_view(), name='usuario-detail'),

    # Endpoints para medicamentos
    path('medicamentos/', MedicamentoView.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:id>/', MedicamentoReadUpdateDeleteView.as_view(), name='medicamento-detail'),

    # Endpoints para prescrição com cadastro de medicamento
    path('prescricoes/cadastrar_prescricao_com_medicamento/', PrescricaoCreateWithMedicamentoView.as_view(), name='prescricao-medicamento-create'),
]