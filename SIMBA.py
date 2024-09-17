import requests
import pandas as pd
import time

# Lista de CNPJs para consultar
list_cnpj = []
def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": cnpj, "plugin": "RF"}
    try:
        response = requests.get(url, params=querystring)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

        if response.status_code == 200:
            try:
                resp = response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Erro ao decodificar JSON para CNPJ {cnpj}")
                resp = {}
        else:
            print(f"Erro na resposta para CNPJ {cnpj}: {response.status_code}")
            resp = {}

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação para CNPJ {cnpj}: {e}")
        resp = {}

    atividade_principal = resp.get("atividade_principal", [{}])[0]

    # Extraindo os campos desejados
    dados_filtrados = {
        "cnpj": cnpj,
        "abertura": resp.get("abertura"),
        "situacao": resp.get("situacao"),
        "nome": resp.get("nome"),
        "fantasia": resp.get("fantasia"),
        "porte": resp.get("porte"),
        "uf": resp.get("uf"),
        "cep": resp.get("cep"),
        "municipio": resp.get("municipio"),
        "atividade_principal_code": atividade_principal.get("code"),
        "atividade_principal_text": atividade_principal.get("text")
    }

    return dados_filtrados


def consultar_cnpjs(cnpjs, output_file):
    resultados = []
    consultas = 0

    for index, cnpj in enumerate(cnpjs):
        dados = consulta_cnpj(cnpj)
        resultados.append(dados)
        print(f"Consultado: {cnpj}")

        consultas += 1

        # Pausar por 1 minuto a cada 3 consultas
        if consultas % 3 == 0:
            print("Aguardando 1 minuto para cumprir o limite de consultas...")
            time.sleep(60)

    df = pd.DataFrame(resultados)
    df.to_excel(output_file, index=False)


# Nome do arquivo Excel de saída
arquivo_excel = '.xlsx'
consultar_cnpjs(list_cnpj, arquivo_excel)