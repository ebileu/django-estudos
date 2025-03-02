from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.pacientes, name="pacientes_home"),
    path('<int:id>', views.paciente_view, name="paciente_view"),
    path('atualizar_paciente/<int:id>', views.atualizar_paciente, name="atualizar_paciente"),
    path('excluir_consulta/<int:id>', views.excluir_consulta, name="excluir_consulta")
]