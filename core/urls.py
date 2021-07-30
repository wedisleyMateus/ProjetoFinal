from django.urls import include, path, re_path 
from .views import (home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos, 
    lista_mensalistas,
    lista_mov_mensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensal_novo,
    pessoa_update,
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensal_update,
    pessoa_delete,
    veiculo_delete,
    movrotativos_delete,
    mensalista_delete,
    movmensal_delete,
)


urlpatterns = [
    path(r'/', home, name='core_home'),
    path(r'pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path(r'pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'pessoa_update/(?P<id>\d+)/', pessoa_update, name='core_pessoa_update'),
    re_path(r'pessoa_delete/(?P<id>\d+)/', pessoa_delete, name='core_pessoa_delete'),

    path(r'veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path(r'veiculo_novo/', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'veiculo_update/(?P<id>\d+)/', veiculo_update, name='core_veiculo_update'),
    re_path(r'veiculo_delete/(?P<id>\d+)/', veiculo_delete, name='core_veiculo_delete'),

    path(r'mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path(r'mov-rot_novo/', movrotativos_novo, name='core_movrotativos_novo'),
    re_path(r'mov-rot_update/(?P<id>\d+)/', movrotativos_update, name='core_movrotativos_update'),
    re_path(r'mov-rot_delete/(?P<id>\d+)/', movrotativos_delete, name='core_movrotativos_delete'),

    path(r'mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path(r'mensalista_novo/', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'mensalista_update/(?P<id>\d+)/', mensalista_update, name='core_mensalista_update'),
    re_path(r'mensalista_delet/(?P<id>\d+)/', mensalista_delete, name='core_mensalista_delete'),
    
    path(r'mov-mensal/', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    path(r'mov-mensal_novo/', movmensal_novo, name='core_movmensal_novo'),
    re_path(r'mov-mensal_update/(?P<id>\d+)/', movmensal_update, name='core_movmensal_update'),
    re_path(r'mov-mensal_delete/(?P<id>\d+)/', movmensal_delete, name='core_movmensal_delete'),
]
