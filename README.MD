Documentation Consulting CNPJ (Receita Federal) 
- 
Esse código realiza a tarefa de Consultar e extrair para um .XLSX dados de uma lista de CNPJs (Sem caracteres especiais) na API Publica da Receita federal, como essa API suporta apenas o total de 3 consultas por minuto, o código realiza um timer de 1 minuto por consulta de 3.

Retorno/ Dados que podem ser extraidos:
-
_Retorno JSON_ :
{'abertura': '', 'situacao': '', 'tipo': '', 'nome': '', 'fantasia': '', 'porte': '', 'natureza_juridica': '', 'atividade_principal': [{'código': '', 'text': ''}], 'qsa': [{'nome': '', 'qual': ''}, {'nome': '', 'qual': ''}], 'logradouro': '', 'numero': '', ' complemento': '', 'município': '', 'bairro': '', 'uf': '', 'cep': '', 'telefone': '', 'data_situacao': '', 'cnpj ': '', 'ultima_atualizacao': '', 'status': '', 'email': '', 'efr': '' , 'motivo_situacao': '', 'situacao_especial': '', 'data_situacao_especial': '', 'atividades_secundarias': [{'code': '', 'text': ''}] , 'capital_social': '', 'simples': {'optante': , 'data_opcao': '', 'data_exclusao': Nenhum, 'ultima_atualizacao': ''} , 'simei': {'optante': Falso, 'data_opcao': Nenhum, 'data_exclusao': Nenhum, 'ultima_atualizacao': ''}, 'extra': {}, ' billing': {'free': True, 'database': True}} 

_Campos p/ Extração_ :
- abertura: Data de abertura da empresa.
- situacao: Situação atual da empresa (e.g., ATIVA, INATIVA).
- tipo: Tipo da empresa (e.g., MATRIZ, FILIAL).
- nome: Nome empresarial completo.
- fantasia: Nome fantasia da empresa (se houver).
- porte: Porte da empresa (e.g., MICRO EMPRESA, PEQUENA EMPRESA).
- natureza_juridica: Código e descrição da natureza jurídica da empresa.
- atividade_principal: Lista de atividades principais da empresa, com os seguintes subcampos:
- código: Código CNAE da atividade principal.
- text: Descrição da atividade principal.
- qsa (Quadro de Sócios e Administradores): Lista de sócios ou administradores, com os seguintes subcampos:
- nome: Nome do sócio ou administrador.
- qual: Qualificação do sócio ou administrador.
- logradouro: Nome da rua ou avenida onde a empresa está localizada.
- numero: Número do endereço.
- complemento: Complemento do endereço.
- municipio: Cidade onde a empresa está localizada.
- bairro: Bairro onde a empresa está localizada.
- uf: Unidade federativa (estado) onde a empresa está localizada.
- cep: CEP do endereço da empresa.
- telefone: Telefone da empresa.
- data_situacao: Data da última atualização da situação da empresa.
- cnpj: CNPJ da empresa.
- ultima_atualizacao: Data da última atualização no sistema.
- status: Status da empresa (e.g., OK).
- email: E-mail de contato da empresa.
- efr: Entidade Federativa Responsável (se houver).
- motivo_situacao: Motivo da situação da empresa (se houver).
- situacao_especial: Situação especial (se houver).
- data_situacao_especial: Data da situação especial (se houver).
- atividades_secundarias: Lista de atividades secundárias, com os seguintes subcampos:
- code: Código CNAE da atividade secundária.
- text: Descrição da atividade secundária.
- capital_social: Capital social da empresa.
- simples: Informações relacionadas ao Simples Nacional, com os seguintes subcampos:
- optante: Se a empresa é optante pelo Simples Nacional.
- data_opcao: Data da opção pelo Simples Nacional.
- data_exclusao: Data de exclusão do Simples Nacional (se houver).
- ultima_atualizacao: Data da última atualização dessas informações.
- simei: Informações relacionadas ao Simei, com os seguintes subcampos:
- optante: Se a empresa é optante pelo Simei.
- data_opcao: Data da opção pelo Simei (se houver).
- data_exclusao: Data de exclusão do Simei (se houver).
- ultima_atualizacao: Data da última atualização dessas informações.
- extra: Campo reservado para informações adicionais (pode estar vazio).
- billing: Informações de faturamento, com os seguintes subcampos:
- free: Indica se o uso da API é gratuito.
- database: Indica se a consulta foi feita no banco de dados.


