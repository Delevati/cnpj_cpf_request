import time
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from validate_docbr import CNPJ

def extrair_cnpj(texto):
    padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b')
    cnpjs_encontrados = re.findall(padrao_cnpj, texto)
    return cnpjs_encontrados[0] if cnpjs_encontrados else None

def limpar_cnpj(cnpj):
    return re.sub(r'\D', '', cnpj)

# API do Gov (3 por min, apenas)
def consulta_cnpj(cnpj):
    try:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": cnpj, "plugin": "RF"}
        start_time = time.time()
        response = requests.get(url, params=querystring)
        end_time = time.time()
        resp = response.json()
        nome_empresa = resp.get('nome', 'N/A')
        return nome_empresa, end_time - start_time
    except Exception as e:
        print(f"Erro na consulta ao CNPJ {cnpj}: {e}")
        return 'Erro na consulta', 0

queries = ['Empresa1', 'Empresa2', 'Empresa3']

validador_cnpj = CNPJ()

total_start_time = time.time()

for query in queries:
    search_results = list(search(query))


    for result in search_results:
        try:

            page = requests.get(result)
            soup = BeautifulSoup(page.text, 'html.parser')
            description = soup.find('meta', attrs={'name': 'description'})
            if description:

                cnpj_encontrado = extrair_cnpj(description['content'])
                if cnpj_encontrado:

                    if validador_cnpj.validate(cnpj_encontrado):
                        cnpj_limpo = limpar_cnpj(cnpj_encontrado)
                        nome_empresa, api_time = consulta_cnpj(cnpj_limpo)

                        print(f"\nCNPJ: {cnpj_limpo}")
                        print(f"Validado: Válido")
                        print(f"Nome da Empresa: {nome_empresa} Tempo: {api_time:.4f} segundos\n")

                        break
                    else:
                        print(f"\nCNPJ: {cnpj_encontrado}")
                        print(f"Validado: Inválido\n")

        except Exception as e:
            print(f"Erro ao processar {result}: {e}")

total_end_time = time.time()
total_time = total_end_time - total_start_time
print(f"Tempo total do processo: {total_time:.4f} segundos")
