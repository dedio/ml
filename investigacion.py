# -*- coding: utf-8 -*-
#  investigacion.py
#  
#  Copyright 2019 Juanmanuel
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Ejemplo
# investigacion.py -l 256189964

import argparse
import requests
import json

# Retorna un request tipo get de la API
# el parámetro flag es para cambiar la consulta entre user_id o category_id 
def consulta(object_id, flag = True):
    if flag:
        url = ROOT
    else:
        url = CAT
    return json.loads(requests.get((url + str(object_id) + TOKEN)).text)

if __name__ == "__main__":
    
    TOKEN = '&access_token='
    ROOT = 'https://api.mercadolibre.com/sites/MLA/search?seller_id='
    CAT = 'https://api.mercadolibre.com/categories/'

    # Configura los parámetros de la línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', nargs = '+')

    # Bucle principal
    for _, values in parser.parse_args()._get_kwargs():
        if values is not None:
            # Por cada user_id ingresado en la línea de comandos
            # genera un log con los datos solicitados
            for value in values:
                with open(('user_id_' + str(value) + '.log'), 'w+') as log:
                    # Recorre los items de la consulta
                    for item in consulta(str(value)):
                        # Obtiene el json con los datos de la categoría
                        cat = consulta(item["body"]["category_id"], False)
                        
                        log.writelines(item["body"]["id"] + ' ' + item["body"]["title"] + ' ' + item["body"]["category_id"] + ' ' + cat["name"] + ' ' + item["body"]["paging"]["total"])
                    log.close()
