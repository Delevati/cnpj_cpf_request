# Ferramentas de Validação e Verificação

Este projeto oferece uma coleção de ferramentas para validação e verificação, incluindo precauções contra ataques de negação de serviço (DDoS).

## Cuidado com DDoS

O sistema possui medidas de proteção contra ataques de DDoS para garantir a integridade do serviço.

## Verificação em 2 Etapas de CNPJ de Empresas

Para a verificação em duas etapas de CNPJ de empresas, foi implementado um sistema de automação que realiza procedimentos específicos.

## Validador de CPF

O módulo `CPF_Validator` realiza a validação do número de CPF, garantindo a conformidade com o formato e critérios de validação.

## Validador de CNPJ

Para a validação de CNPJ, há diversas ferramentas implementadas:

- **run_google_research:** Utiliza o CX (CSE) e a API custom search do Google para realizar pesquisas específicas.

- **run_validate_cnpjnome_google.py:** Realiza a pesquisa do CNPJ, obtém o mesmo CNPJ nos resultados e, em seguida, refaz a pesquisa para encontrar o nome da empresa. Isso serve como uma segunda verificação na automação.

- **run_validate_gov2.py:** Pesquisa até 3 empresas e realiza a validação com a API do governo. (Atenção: apenas 3 requests por minuto à API).

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

1. Configure o ambiente:

   ```bash
   pip install -r requirements.txt

1. Execute o Script de sua necessidade:

   ```bash
    python CPF_Validator.py
    python run_google_research.py
    python run_validate_cnpjnome_google.py
    python run_validate_gov2.py
