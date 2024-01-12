import requests
import dotenv
import os

dotenv.load_dotenv()

def realizar_pesquisa(consulta):
    url = f'https://www.googleapis.com/customsearch/v1?q={consulta}&key={os.getenv("chave_de_api")}&cx={os.getenv("id_de_cse")}'
    resposta = requests.get(url)
    
    try:
        resposta.raise_for_status() 
        dados = resposta.json()

    #print para verificacao das informacoes que aparecem, pode comentar se preferir.
        print(dados)

        if 'items' in dados:
            for item in dados['items']:
                print(item.get('title'))
        else:
            print("Nenhum item encontrado na resposta.")
    except requests.exceptions.HTTPError as err:
        print(f"Falha na solicitação. Código de status: {resposta.status_code}")
        print(f"Detalhes do erro: {err}")
    except Exception as e:
        print(f"Erro desconhecido: {e}")

consulta = 'Empresa que deseja aqui'

realizar_pesquisa(consulta, os.getenv("chave_de_api"), os.getenv("id_de_cse"))
