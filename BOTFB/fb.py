# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:09:03 2023

@author: franm

CODIGO API FACEBOOK
"""

import facebook

def publicar_en_grupo(token, id_grupo, mensaje):
    graph = facebook.GraphAPI(access_token=token)
    graph.put_object(parent_object=id_grupo, connection_name='feed', message=mensaje)

# Llama a la función para publicar en un grupo específico
publicar_en_grupo('TU_TOKEN_DE_ACCESO', 144727261910648, 'Este es un mensaje de prueba')