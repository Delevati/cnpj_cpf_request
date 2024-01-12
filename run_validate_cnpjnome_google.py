import time
import random
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from validate_docbr import CNPJ
import re

# Função para extrair o CNPJ a partir de um texto
def extrair_cnpj(texto):
    padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b')
    cnpjs_encontrados = re.findall(padrao_cnpj, texto)
    return cnpjs_encontrados[0] if cnpjs_encontrados else None

# Função para remover caracteres especiais do CNPJ para pesquisa na API
def limpar_cnpj(cnpj):
    return re.sub(r'\D', '', cnpj)

# Configura as opções globais
query = 'CNPJ DA EMPRESA TOTVS SA'

# Cria um objeto CNPJ para validação
validador_cnpj = CNPJ()

# Número de requisições a serem feitas
num_requisicoes = 50

# Tempo de espera entre as requisições (em segundos)
tempo_espera = 3

# Contado de requisições
contador_requisicoes = 0

# Medir o tempo total de execução
total_start_time = time.time()

# Cria um objeto UserAgent fake
user_agent = UserAgent()

# Iterar sobre o número desejado de requisições
while contador_requisicoes < num_requisicoes:
    result = None  
    try:
        # Escolher um resultado de pesquisa aleatório
        search_results = list(search(query, num_results=5))
        if not search_results:
            print("Nenhum resultado encontrado. Encerrando.")
            break

        result = random.choice(search_results)

        # Extrair texto da descrição dos resultados
        headers = {'User-Agent': user_agent.random}
        page = requests.get(result, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        description_tag = soup.find('meta', attrs={'name': 'description'})

        if description_tag:
            # Extrair o CNPJ do texto da descrição
            description_text = description_tag.get('content', '')
            cnpj_encontrado = extrair_cnpj(description_text)

            if cnpj_encontrado:
                # Validar o CNPJ
                if validador_cnpj.validate(cnpj_encontrado):
                    # Limpar o CNPJ removendo caracteres especiais
                    cnpj_limpo = limpar_cnpj(cnpj_encontrado)

                    # Extrair o nome da empresa diretamente do texto da descrição
                    match = re.search(r'empresa\s*([\w\s]+(?:\s+\w+){0,10})', description_text)
                    nome_empresa = match.group(1).strip() if match else 'Nome não encontrado'

                    # Imprimir as informações
                    print(f"\nCNPJ: {cnpj_limpo}")
                    print(f"Validado: Válido")
                    print(f"Nome da Empresa: {nome_empresa}\n")

                    # Atualizar o contador de requisições
                    contador_requisicoes += 1

                    # Aguardar um intervalo de tempo entre as requisições
                    time.sleep(tempo_espera)
                else:
                    print(f"\nCNPJ: {cnpj_encontrado}")
                    print(f"Validado: Inválido\n")

    except requests.RequestException as e:
        print(f"Erro na requisição HTTP para {result}: {e}")
    except Exception as e:
        print(f"Erro ao processar {result}: {e}")

# Medir o tempo total de execução
total_end_time = time.time()
total_time = total_end_time - total_start_time
print(f"Tempo total do processo: {total_time:.4f} segundos")
