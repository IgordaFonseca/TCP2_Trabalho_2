"""Gera os 33 históricos de atendimento SINTÉTICOS do corpus (dados/corpus_txt/historico_sint_XX.txt).

Cada diálogo foi escrito a partir de um atendimento real do SAAE São Carlos e preserva o assunto e as informações de procedimento do atendimento
original (documentos exigidos, prazos, custos, encaminhamentos), mas é reescrito
com outras palavras e sem nenhum dado pessoal: nomes, endereços, CDC, CPF,
e-mails e protocolos viram marcadores ([NOME], [ENDERECO], [CDC]...).
"""
from pathlib import Path
import json, sys

C, A, B = "Cliente", "Atendente", "Bot"

MSG_2VIA = ("Para obter a fatura, acesse a Agência Virtual no site do SAAE. Não conseguiu? Informe: "
            "CDC-DV; nome completo; CPF ou CNPJ; e, se quiser receber por e-mail, o endereço de e-mail.")
MSG_TITULARIDADE = ("Para alteração de titularidade, use a atualização cadastral no site do SAAE. Não conseguiu? Envie: "
                    "documento que vincule ao imóvel (contrato de compra e venda, escritura, matrícula ou contrato de "
                    "locação com firma reconhecida; não aceitamos IPTU) ou o Termo de Responsabilidade (arquivo anexo) "
                    "preenchido à mão; documento pessoal frente e verso; e o CDC-DV. Se for terceiro, é necessária "
                    "procuração com firma reconhecida.")
MSG_ANTERIORES = ("Importante: contas de anos anteriores só podem ser enviadas agrupadas, com vencimento para hoje, "
                  "e por isso já incluem juros e multa. Desagrupar ou alterar o vencimento só é possível presencialmente. "
                  "Deseja continuar ou prefere somente as contas deste ano?")
MSG_CONFERIR = "Confira o CDC-DV e o endereço antes de pagar. Posso ajudar em algo mais?"
MSG_VAZ_MENU = ("Onde é o vazamento? 1. Rua 2. Calçada 3. Cavalete 4. Esgoto entupido 5. Esgoto vazando "
                "6. Mau cheiro de esgoto 7. Troca de registro do cavalete 8. Limpeza de fossa séptica")
MSG_VAZ_DADOS = "Informe o nome completo do solicitante e o CDC-DV ou o endereço do local. Se puder, envie fotos."
MSG_VAZ_PERGUNTAS = ("Por favor, responda: o vazamento é no asfalto ou na calçada? Qual o endereço completo? "
                     "É água limpa ou esgoto? É de pequena, média ou grande proporção? Há algum ponto de referência?")
MSG_REVISAO = ("Para revisão por vazamento, informe o CDC-DV e quais contas deseja revisar, e envie: laudo/declaração "
               "de conserto do vazamento assinado à mão (modelo anexo); fotos do conserto; documento que vincule ao "
               "imóvel, caso a conta não esteja em seu nome (não aceitamos IPTU); e documento pessoal frente e verso. "
               "Se o vazamento foi na boia da caixa d'água ou da caixa acoplada, a nota fiscal da compra e a foto da "
               "boia são obrigatórias.")
MSG_EXCLUSAO = ("Para exclusão de usuário, envie: documento pessoal frente e verso e o Termo de Exclusão de Usuário "
                "(anexo) preenchido à mão. Sem impressora, o termo pode ser escrito todo à mão seguindo o modelo. "
                "A data no fim do termo deve ser a data em que você deixou de ser responsável pelo imóvel.")
MSG_ANALISE = ("Vamos encaminhar os documentos para análise do setor responsável e entraremos em contato com o "
               "número da ordem de serviço.")
MSG_HIDRO_MENU = ("Hidrômetro: 1. Aferição 2. Furtado 3. Danificado 4. Parado ou embaçado 5. Vazando 6. Lacrar hidrômetro")

H = [
# 01 · inclusão de usuário com termo de responsabilidade
("Ordem de serviço", [
 (C,"Bom dia"),(B,MSG_TITULARIDADE),(C,"Mandei o RG e o termo de inclusão assinado. O CDC é [CDC]"),
 (A,"Bom dia! O endereço é [ENDERECO]?"),(C,"Isso"),
 (A,"O RG enviado tem mais de 10 anos. Pode mandar um documento atualizado? A CNH também serve. E informe um e-mail para contato, por favor."),
 (C,"Vou mandar a CNH. E-mail: [EMAIL]"),
 (A,"Lembrando: para ser cadastrada como PROPRIETÁRIA, precisamos de todas as páginas da matrícula do imóvel. Com o Termo de Responsabilidade, o cadastro é feito apenas como USUÁRIA."),
 (C,"Pode ser como usuária mesmo"),(A,MSG_ANALISE),(C,"Só isso, obrigada")]),
# 02 · 2ª via de parcelas; imóvel com poço; como conferir CDC-DV
("2ª via de conta", [
 (C,"Bom dia, preciso da segunda via"),(B,MSG_2VIA),(C,"[NOME], CPF [CPF]"),
 (A,"Bom dia! Confirme o endereço completo, por favor."),(C,"[ENDERECO]"),
 (A,"Seguem em anexo as parcelas de 2025 e 2026. "+MSG_CONFERIR),
 (C,"Lá a gente não recebe conta do SAAE, usamos poço artesiano. Como confiro o CDC-DV?"),
 (A,"Basta verificar se o endereço impresso na conta está correto."),(C,"Beleza"),
 (A,"Qualquer dúvida, pode nos chamar novamente.")]),
# 03 · 2ª via simples
("2ª via de conta", [
 (C,"Oi, quero a conta"),(B,MSG_2VIA),(C,"CDC [CDC], CPF [CPF], nome [NOME]"),
 (A,"Bom dia! Com quem eu falo?"),(C,"[NOME]"),(A,"Segue a fatura em anexo. "+MSG_CONFERIR),(C,"Só isso, obrigado")]),
# 04 · 2ª via de contas de anos anteriores (agrupadas, juros e multa)
("2ª via de conta", [
 (C,"Oi"),(B,MSG_2VIA),(A,"Boa tarde! Informe o CDC-DV e o nome completo, por favor."),(C,"[CDC], [NOME]"),
 (A,MSG_ANTERIORES),(C,"Quero as anteriores. As deste ano eu já paguei pelo site."),
 (A,"Seguem a conta agrupada e a taxa de resíduos sólidos em anexo. "+MSG_CONFERIR),(C,"Obrigado pelo atendimento")]),
# 05 · 2ª via de parcela de parcelamento em atraso
("2ª via de conta", [
 (C,"Oi"),(B,"Parcelamento: 1. Solicitar parcelamento 2. 2ª via do parcelamento"),(C,"2"),(B,MSG_2VIA),
 (C,"[CDC], [NOME]"),(A,"Boa tarde!"),(C,"Quero a segunda via da parcela do mês 9 do meu parcelamento"),
 (A,"Consta que há parcelas em atraso desde julho."),(C,"Pode mandar mesmo assim, por favor"),
 (A,"Segue o carnê em anexo. "+MSG_CONFERIR),(C,"Só isso, obrigada")]),
# 06 · esgoto vazando na calçada — munícipe de outra cidade
("Ordem de serviço", [
 (C,"Bom dia!"),(B,MSG_VAZ_MENU),(C,"5"),(B,MSG_VAZ_DADOS),
 (C,"[NOME], [ENDERECO]. O vazamento é na calçada: saiu esgoto com pressão de uma fissura ao lado do cano. Moro aqui há muitos anos e nunca teve problema de esgoto na rua. Acho que tem a ver com uma troca de manilha que fizeram no começo da rua há poucos dias."),
 (A,"Bom dia! Esse endereço fica em São Carlos-SP?"),
 (C,"Não, é em outra cidade. Me passaram este número como se fosse de lá, desculpe o incômodo."),
 (A,"Sem problemas! Este é o canal digital do SAAE de São Carlos-SP e não temos informações sobre outras cidades. Procure o serviço de água e esgoto do seu município.")]),
# 07 · débitos: só sabe o CPF — exigência da LGPD
("2ª via de conta", [
 (C,"Oi"),(B,MSG_2VIA),(A,"Boa tarde! Informe o CDC-DV, o nome completo e o CPF ou CNPJ, por favor."),
 (C,"Eu só sei o CPF"),
 (A,"Em cumprimento à LGPD (Lei Geral de Proteção de Dados), para informar débitos precisamos confirmar os dados do responsável pela conta. Sem o CDC-DV ou o nome completo do titular, não conseguimos liberar as informações.")]),
# 08 · erro no site ao fazer cadastro; envio de documentos pelo WhatsApp
("Ordem de serviço", [
 (C,"Olá"),(B,MSG_TITULARIDADE),(C,"Mandei a CNH e o termo assinado"),
 (A,"Boa tarde! Com quem eu falo?"),
 (C,"Sou o titular. Tentei fazer o cadastro pelo site, mas aparece 'Falha ao enviar solicitação, verifique os campos'. Já revisei tudo e não consigo enviar."),
 (A,"Qual o CDC da conta?"),(C,"[CDC]"),(A,"Confirme o endereço, por favor."),(C,"[ENDERECO]"),
 (A,"Para dar continuidade, informe um e-mail para contato."),(C,"[EMAIL]"),(A,MSG_ANALISE),
 (C,"Qual o prazo para a verificação? Onde posso acompanhar?"),
 (A,"É conforme a demanda do setor. Você pode acompanhar por aqui ou pelo 0800.")]),
# 09 · 2ª via; conta retida para revisão; próxima em leitura
("2ª via de conta", [
 (C,"Oi"),(B,MSG_2VIA),(C,"[CDC], [NOME]"),(A,"Boa tarde!"),
 (A,"Seguem a fatura e a taxa de resíduos sólidos em anexo. "+MSG_CONFERIR),(C,"Só consta essa?"),
 (A,"Em nome do titular, sim. A conta com vencimento em abril está retida para revisão, e a de maio ainda está em processo de leitura."),
 (C,"Tá bom, obrigada")]),
# 10 · inclusão de proprietária com escritura
("Ordem de serviço", [
 (C,"Boa tarde"),(B,MSG_TITULARIDADE),(C,"Enviei a escritura do apartamento. CDC [CDC]"),
 (A,"Boa tarde! Envie também o documento pessoal frente e verso e um e-mail para contato."),
 (C,"Segue a CNH. E-mail: [EMAIL]"),(A,"O endereço é [ENDERECO]?"),(C,"Correto"),(A,MSG_ANALISE),
 (C,"Só isso, obrigada")]),
# 11 · revisão de conta por conserto de vazamento (torneira); vínculo por certidão de casamento
("Revisão de conta", [
 (C,"Oi"),(B,"Motivo da revisão: 1. Vazamento 2. Aferição de hidrômetro 3. Falta de água 4. Erro de leitura 5. Categoria residencial/comercial"),
 (C,"1"),(B,MSG_REVISAO),(C,"CDC [CDC]. Quero revisar a conta de outubro, vencimento dia 20."),
 (A,"Bom dia! Aguardo o envio do laudo, das fotos do conserto e dos documentos."),
 (C,"O vazamento foi na torneira, já substituí. Segue minha CNH."),
 (A,"Qual o seu vínculo com o imóvel?"),(C,"Sou a dona, esposa do titular da conta."),
 (A,"Como a senhora é a solicitante, precisamos da sua documentação pessoal e da certidão de casamento. E um e-mail para contato, por favor."),
 (C,"Ok. [EMAIL]"),(A,"O endereço é [ENDERECO]? Deseja revisar apenas o vencimento de outubro?"),(C,"Sim"),
 (A,MSG_ANALISE),(C,"Muito obrigada")]),
# 12 · alteração de titularidade (filha → pai); prazo conforme demanda
("Ordem de serviço", [
 (C,"Boa tarde"),(B,MSG_TITULARIDADE),
 (C,"Quero alterar a titularidade da conta [CDC]. Está no nome da minha filha, mas sou eu quem paga."),
 (A,"Boa tarde! Envie o documento que vincule ao imóvel ou o termo preenchido à mão, e o documento pessoal frente e verso."),
 (C,"Tentei pelo site, mas no 0800 me orientaram a fazer por aqui porque o site está instável. Segue o termo de inclusão preenchido."),
 (A,"Envie também a documentação pessoal, por favor."),(C,"Segue a CNH"),
 (A,"O endereço é [ENDERECO] e o e-mail para contato é [EMAIL]?"),(C,"Exato"),(A,MSG_ANALISE),
 (C,"Em quanto tempo fica pronto?"),
 (A,"O procedimento é feito conforme a demanda, sem prazo exato. Por este canal fazemos a análise dos documentos e a abertura da ordem de serviço; a execução é feita por outro setor. O senhor pode nos contatar nos próximos dias para verificar."),
 (C,"Vocês mandam o número da ordem de serviço por aqui? Esse é o protocolo da solicitação?"),
 (A,"Esse é o protocolo do atendimento. A ordem de serviço será enviada por aqui ou por e-mail."),(C,"Ok, obrigado")]),
# 13 · 2ª via enviada por e-mail
("2ª via de conta", [
 (C,"Bom dia"),(B,MSG_2VIA),(C,"[NOME], CPF [CPF], e-mail [EMAIL]"),
 (A,"Bom dia! Com quem eu falo?"),(C,"Com a titular"),(A,"Confirme o endereço, por favor."),(C,"[ENDERECO]"),
 (A,"A segunda via foi enviada para o e-mail informado e chega em até 15 minutos. Posso ajudar em algo mais?"),
 (C,"Só isso, obrigada")]),
# 14 · 2ª via simples
("2ª via de conta", [
 (C,"Bom dia"),(B,MSG_2VIA),(C,"[CDC] [NOME]"),(A,"Bom dia! Segue a fatura. "+MSG_CONFERIR),
 (C,"Não, só isso mesmo. Obrigada")]),
# 15 · vazamento de água limpa na calçada → OS
("Ordem de serviço", [
 (C,"Bom dia! Gostaria de solicitar o conserto de um vazamento na frente de casa."),(B,MSG_VAZ_MENU),(C,"2"),
 (B,MSG_VAZ_DADOS),(C,"[NOME], CDC [CDC]"),(A,"Bom dia! "+MSG_VAZ_PERGUNTAS),
 (C,"Calçada. [ENDERECO]. Água limpa, média proporção. Fica dentro do condomínio."),
 (A,"Gerada a ordem de serviço [PROTOCOLO]. A equipe irá ao local conforme a demanda. Posso ajudar em algo mais?"),
 (C,"Ok, obrigada")]),
# 16 · 2ª via simples
("2ª via de conta", [
 (C,"bom dia"),(B,MSG_2VIA),(C,"[CDC] [NOME]"),(A,"Bom dia! Segue a fatura em anexo. "+MSG_CONFERIR),(C,"obrigada")]),
# 17 · 2ª via com contas antigas agrupadas
("2ª via de conta", [
 (C,"Oi, preciso da segunda via da conta"),(B,MSG_2VIA),(C,"[NOME], CPF [CPF], [ENDERECO]"),
 (A,"Bom dia! "+MSG_ANTERIORES),(C,"Sim, pode mandar"),
 (A,"Seguem a conta agrupada, a conta do mês e a taxa de resíduos sólidos. "+MSG_CONFERIR),(C,"Obrigada")]),
# 18 · 2ª via com taxa de resíduos
("2ª via de conta", [
 (C,"Bom dia"),(B,MSG_2VIA),(C,"[CDC], [NOME], CPF [CPF]"),
 (A,"Bom dia! Seguem a fatura de água e a taxa de resíduos sólidos. "+MSG_CONFERIR),(C,"Obrigado")]),
# 19 · exclusão de usuário concluída
("Exclusão de usuário", [
 (C,"Olá, quero tirar meu nome da conta, não moro mais no imóvel"),(B,MSG_EXCLUSAO),
 (C,"Enviei o documento e o termo preenchido"),(A,"Boa tarde! Exclusão concluída. Protocolo [PROTOCOLO]. Posso ajudar em algo mais?"),
 (C,"Era isso mesmo, obrigado")]),
# 20 · 2ª via simples
("2ª via de conta", [
 (C,"Bom dia"),(B,MSG_2VIA),(C,"CDC [CDC], [NOME], CPF [CPF]"),(A,"Bom dia! Segue a fatura. "+MSG_CONFERIR),(C,"Ok, obrigada")]),
# 21 · lacre do hidrômetro rompido em obra; custos de serviço
("Ordem de serviço", [
 (C,"Boa tarde"),(B,MSG_HIDRO_MENU),(C,"3"),
 (B,"Informe o CDC-DV e o nome completo do solicitante e envie fotos do dano. Constatada a avaria, abriremos uma ordem de serviço e será cobrado R$ 155,03 na próxima conta."),
 (C,"Na verdade é outra coisa"),(B,MSG_HIDRO_MENU),(C,"6"),
 (B,"Informe o CDC-DV e o nome completo. Há um custo de R$ 21,86 para lacrar o hidrômetro, cobrado na próxima fatura."),
 (C,"[NOME], CDC [CDC]. Fiz uma obra no portão e o lacre do medidor quebrou."),
 (A,"Boa tarde! O lacre é da caixa padrão?"),(C,"Sim"),(A,"Prefere que a equipe vá de manhã ou à tarde?"),(C,"Manhã"),
 (A,"Gerada a ordem de serviço [PROTOCOLO]. A equipe irá conforme a demanda. Lembrando que o custo de R$ 21,86 será cobrado na próxima fatura."),
 (C,"Não, obrigado")]),
# 22 · vazamento no hidrômetro → OS
("Ordem de serviço", [
 (C,"Bom dia!"),(B,MSG_HIDRO_MENU),(C,"5"),
 (B,"Informe o CDC-DV e o nome completo do solicitante. Se possível, envie fotos e detalhes. Qual o volume do vazamento?"),
 (C,"[NOME]. Vazamento médio de água no hidrômetro."),
 (A,"Bom dia! O vazamento é no hidrômetro ou no pé do cavalete? É de pequena, média ou grande proporção? Há ponto de referência?"),
 (C,"É no hidrômetro, média proporção, perto da pista."),
 (A,"Gerada a ordem de serviço [PROTOCOLO]. A equipe irá conforme a demanda."),(C,"Só isso, muito obrigada")]),
# 23 · 2ª via com agrupamento de contas antigas
("2ª via de conta", [
 (C,"Boa tarde"),(B,MSG_2VIA),(C,"[CDC]"),(A,"Boa tarde! Confirme o nome completo do titular da conta."),(C,"[NOME]"),
 (A,MSG_ANTERIORES),(C,"Pode continuar"),(A,"Seguem a conta do mês e o agrupamento das anteriores. "+MSG_CONFERIR),
 (C,"Obrigada")]),
# 24 · exclusão de usuário; última conta de responsabilidade
("Exclusão de usuário", [
 (C,"Boa tarde"),(B,MSG_EXCLUSAO),(C,"Segue a CNH e o termo de exclusão preenchido. Falei com vocês há pouco."),
 (A,"Boa tarde! O endereço é [ENDERECO]?"),(C,"Isso"),
 (A,"Exclusão realizada. Chamado [PROTOCOLO]. Posso ajudar em algo mais?"),
 (C,"Então está feito? Pago a fatura atual e não vai ter outra para pagar, certo?"),
 (A,"Correto. A última conta de sua responsabilidade é a referência de junho, com vencimento em julho."),
 (C,"Essa já paguei, obrigado")]),
# 25 · exclusão de locatário pelo proprietário
("Exclusão de usuário", [
 (C,"Olá, sou o proprietário e o inquilino saiu do imóvel"),
 (B,"Para excluir o locatário, informe: nome completo do proprietário; nome completo do locatário; CPF e RG do locatário; telefone e e-mail do locatário; período da locação; CDC-DV; e endereço."),
 (C,"Proprietário: [NOME]. Locatário: [NOME], CPF [CPF]. Período da locação: dezembro de 2023 a junho de 2026. CDC [CDC]. Endereço [ENDERECO]."),
 (A,"Boa tarde! Exclusão realizada. Chamado [PROTOCOLO]. Posso ajudar em algo mais?")]),
# 26 · vazamento grande na calçada de imóvel abandonado (terceiro)
("Ordem de serviço", [
 (C,"Oi"),(B,MSG_VAZ_MENU),(C,"2"),(B,MSG_VAZ_DADOS),(C,"Não é na minha casa, é na rua"),
 (A,"Boa tarde! "+MSG_VAZ_PERGUNTAS),
 (C,"Na calçada, água limpa, vazamento grande. Fica numa esquina perto de uma escola."),
 (A,"Qual o número do imóvel?"),(C,"É um imóvel abandonado, a casa da esquina, [ENDERECO]"),
 (A,"Gerada a ordem de serviço [PROTOCOLO]. A equipe irá conforme a demanda.")]),
# 27 · ligação nova: vistoria aprovada, prazo de 30 dias úteis
("Ligação nova", [
 (C,"Boa tarde"),(B,"Tipo de vistoria: 1. Vistoria da caixa padrão 2. Vistoria para mudar categoria (comercial/residencial) 3. Vistoria de mudança de cavalete"),
 (C,"1"),(B,"Informe o nome completo do solicitante e o CDC-DV ou o endereço do local."),(C,"[NOME], [ENDERECO]"),
 (A,"Boa tarde! Com quem eu falo?"),(C,"[NOME]. Quero saber da minha solicitação de ligação nova."),
 (A,"Localizei a ordem de serviço [PROTOCOLO]. A vistoria da caixa padrão foi aprovada. O prazo para executar a ligação é de até 30 dias úteis após a aprovação da vistoria."),
 (C,"Certo, então é só aguardar o prazo. Obrigada")]),
# 28 · inclusão de inquilino com contrato de locação
("Ordem de serviço", [
 (C,"Bom dia"),(B,MSG_TITULARIDADE),(C,"Mandei o contrato de locação, a CNH e o termo. CDC [CDC]"),
 (A,"Bom dia! O endereço é [ENDERECO]?"),(C,"Isso"),
 (A,"Para continuar, informe um e-mail para contato."),(C,"[EMAIL]"),(A,MSG_ANALISE),(C,"Por enquanto é só, agradeço")]),
# 29 · consulta de débitos: nada em aberto; conta do mês em leitura
("2ª via de conta", [
 (C,"Bom dia. Quero ver se tenho conta em aberto"),(B,MSG_2VIA),(C,"[CDC], [NOME]"),
 (A,"Bom dia! No momento não há contas de água em atraso ou em aberto. A conta de novembro ainda está em processo de leitura e deve ser disponibilizada nos próximos dias."),
 (C,"Não, obrigado")]),
# 30 · 2ª via com taxa de resíduos
("2ª via de conta", [
 (C,"Olá"),(B,MSG_2VIA),(C,"[CDC], [NOME]"),(A,"Boa tarde! Seguem a fatura e a taxa de resíduos sólidos. "+MSG_CONFERIR),(C,"Ok, obrigado")]),
# 31 · buraco aberto pelo SAAE e tampa da caixa padrão quebrada
("Ordem de serviço", [
 (C,"Oi"),(B,MSG_VAZ_MENU),(C,"2"),(B,MSG_VAZ_DADOS),(C,"[NOME], CDC [CDC], [ENDERECO]"),(A,"Boa tarde!"),
 (C,"A equipe consertou um vazamento aqui e ficou de voltar no dia seguinte para fechar o buraco, mas não voltou. Amarraram a fita de sinalização na tampa do cavalete e o vento arrancou a tampa. Preciso que venham fechar o buraco e trocar a tampa. Ainda tenho ordem de serviço em aberto."),
 (A,"Foi o SAAE que abriu o buraco? Ainda há vazamento aparente?"),
 (C,"Foi o SAAE, sim. Não há mais vazamento: uma pedra tinha cortado a mangueira. Liguei no 0800 e me pediram para mandar as fotos por aqui."),
 (A,"Vou encaminhar ao setor responsável e pedir que compareçam o quanto antes. Sobre a tampa da caixa padrão: o SAAE não faz a troca, a responsabilidade é do consumidor, pois a caixa é comprada em lojas de material de construção."),
 (C,"Mas quebrou por causa da fita que colocaram. E o lacre, como fica? Vou ter que pagar?"),
 (A,"Vamos encaminhar ao setor para verificar e, se houver posicionamento, retorno por aqui mesmo."),
 (C,"Agradeço, aguardo então")]),
# 32 · revisão de contas altas por vazamento na caixa d'água; medo de corte
("Revisão de conta", [
 (C,"Desculpa a demora"),(B,"Motivo da revisão: 1. Vazamento 2. Aferição de hidrômetro 3. Falta de água 4. Erro de leitura 5. Categoria residencial/comercial"),
 (C,"1"),(B,MSG_REVISAO),
 (C,"CDC [CDC]. Contas de julho, agosto e setembro. Pedi revisão há dias e não tive resposta. Estou preocupada porque tenho 3 contas em aberto e tenho medo de cortarem a água. As contas vieram acima de 200 reais por causa de um vazamento; eu sempre paguei por volta de 60."),
 (A,"Boa tarde! Por favor, encaminhe toda a documentação."),
 (C,"Seguem os documentos e vídeos que comprovam a troca da caixa d'água que estava vazando. Já tinha mandado tudo para a unidade de atendimento e não tive retorno."),
 (A,"O endereço é [ENDERECO]? Envie também o documento pessoal frente e verso, uma foto ou a 2ª via das contas a revisar e um e-mail para contato."),
 (C,"[EMAIL]. Não estou com as contas, mas os vencimentos são agosto, setembro e outubro. Consegui baixar a segunda via pelo site, seguem as 3 no mesmo arquivo."),
 (A,MSG_ANALISE),(C,"Eu que agradeço")]),
# 33 · 2ª via simples com confirmação de endereço
("2ª via de conta", [
 (C,"Oi"),(B,MSG_2VIA),(C,"[NOME], CPF [CPF]"),(A,"Boa tarde! Com quem eu falo? Confirme o endereço, por favor."),
 (C,"Com a titular. [ENDERECO]"),(A,"Segue a fatura. "+MSG_CONFERIR),(C,"Só isso, obrigada")]),
]

def renderizar(assunto, msgs):
    linhas = [f"Assunto: {assunto}", ""]
    h, m = (14, 10) if "tarde" in msgs[0][1].lower() else (9, 5)
    for quem, texto in msgs:
        linhas += [f"{quem} {h:02d}:{m:02d}", texto, ""]
        m += 2
        if m >= 60: h, m = h + 1, m - 60
    return "\n".join(linhas).strip() + "\n"

if __name__ == "__main__":
    destino = Path(sys.argv[1]); destino.mkdir(parents=True, exist_ok=True)
    assert len(H) == 33
    for i, (assunto, msgs) in enumerate(H, 1):
        assert msgs[0][0] == C, f"histórico {i} deve começar pelo Cliente"
        (destino / f"historico_sint_{i:02d}.txt").write_text(renderizar(assunto, msgs), encoding="utf-8")
    print("ok", len(H))
