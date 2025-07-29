def gerar_html():
    # Inputs
    valor = input("Digite o valor da transação (ex: 150,00): ")
    dia_semana = input("Digite o dia da semana (ex: Segunda-feira): ")
    dia_mes = input("Digite o dia do mês (ex: 15): ")
    mes = input("Digite o mês (ex: 10): ")
    ano = input("Digite o ano (ex: 2024): ")
    hora = input("Digite a hora (ex: 14): ")
    minuto = input("Digite o minuto (ex: 30): ")
    cod_agencia = input("Digite o código da agência (4 dígitos): ")
    nome_recebedor = input("Digite o nome de quem recebeu: ")
    cpf_recebedor = input("Digite o CPF de quem recebeu (formato ***.nnn.nnn-**): ")
    instituicao_recebedor = input("Digite a instituição de quem recebeu: ")
    nome_pagador = input("Digite o nome do pagador: ")
    cpf_pagador = input("Digite o CPF do pagador (formato ***.nnn.nnn-**): ")

    # Nome do arquivo de saída
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: comprovante.html): ")
    if not nome_arquivo.endswith(".html"):
        nome_arquivo += ".html"

    # Template HTML
    html = f"""
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comprovante Inter</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .container {{
                margin: 20px; text-align: center;
            }}
            .linha-pontilhada {{
                border-top: 1px dotted #000;
                margin: 20px 0;
            }}
            .lado {{
                display: flex;
                justify-content: space-between;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://brandlogos.net/wp-content/uploads/2023/12/banco_inter-logo_brandlogos.net_qybid-300x78.png" alt="Imagem no topo" style="height:22px; width: 92px;">
            <h1>Pix enviado</h1>
            <h1>R$ {valor}</h1>
        </div>
        <div class="lado">
            <h3>Data do pagamento</h3>
            <div>
                <h2>{dia_semana}, {dia_mes}/{mes}/{ano}</h2>
            </div>
        </div>
        <div class="lado">
            <h3>Horário</h3>
            <div>
                <h2>{hora}h{minuto}</h2>
            </div>
        </div>
        <div class="lado">
            <h3>Identificador</h3>
            <h2>"SAN{ano}{mes}{dia_mes}2054{cod_agencia}7"</h2>
        </div>
        <h2>ID da transação</h2>
        <h2>"E00416968{ano}{mes}{dia_mes}2055CO3LkQHRnl"</h2>
        <div class="linha-pontilhada"></div>
        <div class="lado">
            <h2>Quem recebeu</h2>
        </div>
        <div>
            <h3>Nome</h3>
            <h3>{nome_recebedor}</h3>
        </div>
        <div class="lado">
            <h3>CPF/CNPJ</h3>
            <h2>{cpf_recebedor}</h2>
        </div>
        <div class="lado">
            <h3>Instituição</h3>
            <h2>{instituicao_recebedor}</h2>
        </div>
        <div class="linha-pontilhada"></div>
        <div class="lado">
            <h2>Quem pagou</h2>
        </div>
        <div class="lado">
            <h3>Nome</h3>
        </div>
        <div>
            <h3>{nome_pagador}</h3>
        </div>
        <div class="lado">
            <h3>CPF/CNPJ</h3>
            <h2>{cpf_pagador}</h2>
        </div>
        <div class="lado">
            <h3>Instituição</h3>
            <h2>Banco Inter S.A.</h2>
        </div>
    </body>
    </html>
    """

    # Salvar o HTML em um arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Comprovante gerado com sucesso no arquivo: {nome_arquivo}")

# Chamar a função
gerar_html()
