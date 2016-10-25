import os
import sys
from flask import Flask, session, render_template, url_for, redirect, request, flash, jsonify


app = Flask(__name__, static_url_path='/static')

app.secret_key = app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'



# tipo: 0 para texto 1 para pergunta
class Pergunta:
  def __init__(self,num, enunciado, opcao1, opcao2, opcao3, opcao4, resposta, tipo, final):
    self.num = num
    self.enunciado = enunciado
    self.opcao1 = opcao1
    self.opcao2 = opcao2
    self.opcao3 = opcao3
    self.opcao4 = opcao4
    self.resposta = resposta
    self.tipo = tipo
    self.final = final




informacoes = []
informacoes.append('equQWEASDUhAWEdwasdXCZX aqui fala sobre drones naanananananaanaannananananana')

perguntas = []

# MODULO I

perguntas.append(Pergunta(0,'Uma operação de sistema aéreo não tripulado (sigla em inglês UAS) profissional é aquele que envolve um planejamento cuidadoso e premeditação. Antes de embarcar em utilizar drones para fazer jornalismo, pilotos e as organizações devem tomar várias medidas. Em primeiro lugar, o piloto deve prática com o avião a ser utilizado. Seu primeiro vôo com o avião não deve ser para uma história. Familiarização com a plataforma é essencial. organizações de notícias que querem usar drones deve falar com a polícia e bombeiros locais bem antes quebras de notícias, alertando-os de futuras usando drones de coleta de notícias. Os procedimentos operacionais gerais para voos de drones são divididos em seções: Pré-viagem, Pré-vôo, vôo, e pós-vôo. Os requisitos gerais de cada um são encapsulado em listas de verificação projetadas para ajudar a garantir que cada passo é realizado. As seções e o raciocínio por trás deles, são descritos aqui:',
  0,1,1,1,1,0,0))


perguntas.append(Pergunta(1,'Tendo em mente o objetivo numero um do jornalismo com drone, o qual procedimento deve ser tomado, caso o mesmo seja quebrado?',
  'Prosseguir com a matéria, pois, mesmo que o tema tenha perdido seu interesse, o objetivo manda que a mesma seja finalizada, mesmo que não seja utilizada posteriormente.',
  'Deve-se voltar o zumbido também conhecido por UAS para a zona de aterrissagem e finalizar o voo.',
  '(Caso esteja ao vivo) Manter-se firme, mesmo que a exclusividade seja quebrada, pois deve-se manter a fidelidade para com o telespectador que está acompanhando a matéria.',
  'Analisar e estudar, com antecedência, a situação com a qual deseja-se fazer a matéria, para que possa conduzir a reportagem com maior excelência.',
  2, 1, 0))
perguntas.append(Pergunta(2,'Tendo em mente os três papéis de operadores de voo, qual a responsabilidade do PIC?',
  'É de sua responsabilidade monitorar a área operacional para garantir que não há riscos que podem pôr em perigo o voo ou pessoas que não fazem parte da equipe de operações.',
  'É de sua responsabilidade comunicar metas de voo para o piloto antes do voo e verificar os resultados após o desembarque. O PIC determina o que é necessário para a história e comunica que ao jornalista.',
  'É de sua responsabilidade todas as operações de voo. É o PIC que tem a autoridade máxima em qualquer voo. O PIC determina se a aeronave é de navegabilidade e capaz de conduzir as operações propostas.',
  'O PIC é responsável por permanecer dentro da distância de falar do jornalista para que não se utilize rádios para se comunicar.',
  3, 1, 0))
perguntas.append(Pergunta(3,'Quem pode pilotar um drone com fins jornalísticos?',
  'Apenas o jornalista em questão, pois, para que se tenha boas imagens referentes a matéria, é necessário possuir conhecimento sobre a mesma.',
  'O "câmera", pois, este possui conhecimentos sobre técnicas de filmagem desconhecidos pelo jornalista.',
  'Apenas um piloto treinado e certificado para isto.',
  'Qualquer pessoa visto que atualmente até mesmo crianças possuem conhecimento',
  3, 1, 0))
perguntas.append(Pergunta(4,'Sobre o Código SPJ de Ética, é correto afirmar que:',
  'Não é necessário demonstrar compaixão por aqueles que podem ser afetados pela cobertura de notícias.',
  'Equilíbrio necessidade do público por informações contra danos ou desconforto potencial. Buscar por uma notícia não é uma licença para a arrogância ou a intromissão indevida.',
  'Perceber que as pessoas públicas têm um maior direito de controlar informações sobre si mesmos do que figuras privadas e outros que buscam o poder, influência ou atenção.',
  'É permitido atrapalhar a reportagem de outros, se isso for lhe trazer maior vantagem.',
  2, 1, 0))
perguntas.append(Pergunta (5,
  'Considerando o Código Nacional Press Photographers Association de Ética, é incorreto afirmar que:',
  'Não sabotar intencionalmente os esforços de outros jornalistas a menos que isso lhe traga vantagem maior.',
  'Ao cobrir uma notícia, juntamente com outras organizações de mídia de drones, evitar o uso de seu drone, obstruir ou derrubar outros drones.',
  'Enquanto fotografar assuntos não contribuir intencionalmente, alterar, ou tentar alterar ou em eventos fluêntes.',
  'Considere como o ruído gerado pelos seus UAS, e sua presença, influências eventos, pessoas e animais.',
  1, 1, 1))

  #MODULO II
perguntas.append(Pergunta (0,
  'Uma operação de sistema aéreo não tripulado (sigla em inglês UAS) profissional é aquele que envolve um planejamento cuidadoso e premeditação. Antes de embarcar em utilizar drones para fazer jornalismo, pilotos e as organizações devem tomar várias medidas. Em primeiro lugar, o piloto deve prática com o avião a ser utilizado. Seu primeiro vôo com o avião não deve ser para uma história. Familiarização com a plataforma é essencial. organizações de notícias que querem usar drones deve falar com a polícia e bombeiros locais bem antes quebras de notícias, alertando-os de futuras usando drones de coleta de notícias. Os procedimentos operacionais gerais para voos de drones são divididos em seções: Pré-viagem, Pré-vôo, vôo, e pós-vôo. Os requisitos gerais de cada um são encapsulado em listas de verificação projetadas para ajudar a garantir que cada passo é realizado. As seções e o raciocínio por trás deles, são descritos aqui:Pré-viagem Antes de empreender qualquer operação voo, o piloto em comando deve reunir informações sobre a área de voo proposta para garantir a segurança das operações que cumprem com os Regulamentos Federal de Aviação. Localização Perguntas o PIC deve responder sobre o local são: * O que é aquilo? Existem riscos para a aviação? * O espaço aéreo está? * Você precisa da permissão de controlo de tráfego aéreo (ATC)?'
  ,1,1,1,1,1,0,0))

perguntas.append(Pergunta(1,
  'Marque a alternativa incorreta:',
  'Uma operação de sistema aéreo não tripulado envolve um planejamento cuidadoso e premeditado.',
  'O piloto deve ter prática com drone a ser utilizado.',
  'Usar um novo drone sem pratica.',
  'D) Organizar as notícias que desejar usar drones.',
  3,1,0))

perguntas.append(Pergunta(2,'Quais são procedimentos gerais para voo com drone?',
  'A) Pré-viagem, Decolar , vôo, pousar.',
  'B) Decolar , vôo, pousar.',
  'C) Pré-vôo, vôo, e pós-vôo.',
  'D) Pré-viagem, pré-vôo, vôo, e pós-vôo.',
  4,1,0))

perguntas.append(Pergunta(3,'Em relação a pré-viagem no quesito localização qual alternativa é incorreta:',
  'Verificar quantidade de pessoas do local e o que esperar.',
  'As condições climáticas do local não afeta voo.',
  'Você precisa da permissão de controlo de tráfego aéreo (ATC).',
  'Tem permissão para voo no espaço privado.',
  2,1,0))

perguntas.append(Pergunta(4,'Qual alternativa esta incorreta em relação à pré-viagem:',
  'Fazer medidas contra falhas no drone.',
  'Fazer uma inspeção pré-viagem.',
  'Verificar local do voo e sua logistica.',
  'Definir as metas operacionais do drone.',
1,1,0))

perguntas.append(Pergunta(5, 'Em uma reunião de pré-viagem o PIC deve abortar alguns temas, mas qual não faz parte dela?',
  'É permitido atrapalhar a reportagem de outros, se isso for lhe trazer maior vantagem.',
  'Qualquer privacidade conhecido ou questões éticas e as medidas paliativas.',
  'Uma descrição geral da área de operações.',
  'Os objetivos da missão específicas, incluindo fotos esperados, ângulos ou assuntos.',
  1,1,1
  ))




@app.route('/',methods=['GET','POST'])
def indexo():    
#  sys.stdout.write(str(len(perguntas))+"\n")
  return app.send_static_file('index.html')

@app.route('/teste/verifica<modulo>', methods=['POST', 'GET'])
def verificacao(modulo):
  k = int(session['mod1']) + int(session['mod2'])
  sys.stdout.write(str(k)+"\n")
  if(int(modulo) == 1):    
    if(k >= 6):
      return app.send_static_file('jaAprovado.html')
  if(int(modulo)==2):  
    if(k < 6 ):      
      return app.send_static_file('erroModulo.html')
    if (k >= 12 ):
      return app.send_static_file('jaAprovado.html')

  return redirect('http://localhost:5000/teste')


@app.route('/teste/correcao<questao>', methods=['POST'])
def correcao(questao):    
  i = int(questao)
  if(perguntas[i].tipo == 0 ):    
    if(i<=5):
      session['mod1'] += 1
    else:
      session['mod2'] += 1
      #sys.stdout.write(str(session['mod1'])+"\n")
    return redirect('http://localhost:5000/teste')

  respCorreta = perguntas[i].resposta  
  respUsuario = request.form['optionsRadios']


#MODULO 1
  if(i<=5):
    session['mod1'] += 1
    if(str(respUsuario)==str(respCorreta)):
      session['certas1'] +=1
    session['respondidas1'] +=1    
#Modulo 2
  else:
    session['mod2'] += 1
    if(str(respUsuario)==str(respCorreta)):
      session['certas2'] +=1
    session['respondidas2'] +=1    




  return render_template("quizCorrecao.html",
    indice = int(questao), 
    num = int(perguntas[i].num),
    enunciado = perguntas[i].enunciado, 
    opcao1 = perguntas[i].opcao1, 
    opcao2 = perguntas[i].opcao2,
    opcao3 = perguntas[i].opcao3, 
    opcao4 = perguntas[i].opcao4, 
    resposta = (respCorreta),
    respostaUsuario = (respUsuario), aux1 = str(1), aux2 = str(2), aux3 = str(3), aux4 = str(4)
  )


#Reiniciar sessão
@app.route('/kkk/')
def kk():
  session.pop('mod1', None)
  session.pop('certas1', None)
  session.pop('respondidas1', None)
  session.pop('mod2', None)
  session.pop('certas2', None)
  session.pop('respondidas2', None)

  return app.send_static_file('index.html')


@app.route('/progresso/')
def progresso():  
  respondidas1 = int(session['respondidas1']),
  certas1 = int(session['certas1']),   
  total1 = 5
  if(respondidas1[0] == 0 ):
    pct12 = 0
  else:    
    pct12 = 100 * float(certas1[0]/respondidas1[0])
  pct11 = 100 * respondidas1[0]/total1
  return render_template("progresso.html",
      respondidas1 = respondidas1[0],
      certas1 = certas1[0],
      total1 = total1,
      pct11 =  float("{0:.2f}".format(pct11)),
      pct12 = float("{0:.2f}".format(pct12)) 
      )




@app.route('/teste/', methods=['POST', 'GET'])
def ind():      
  #i = int(questao)  
  try:
    session['mod1'] += 1
    session['mod1'] -= 1
    session['respondidas1'] += 1
    session['respondidas1'] -= 1
    session['certas1'] += 1
    session['certas1'] -= 1

    session['mod2'] += 1
    session['mod2'] -= 1
    session['respondidas2'] += 1
    session['respondidas2'] -= 1
    session['certas2'] += 1
    session['certas2'] -= 1
  except KeyError:
    session['mod1'] = 0
    session['respondidas1'] = 0
    session['certas1'] = 0

    session['mod2'] = 0
    session['respondidas2'] = 0
    session['certas2'] = 0

  i = int((session["mod1"]) ) + int((session["mod2"]) ) 
  sys.stdout.write(str(i)+"\n")

  
  if (i>=int(len(perguntas))):
    return("Perguntas finalizadas!")

  if(perguntas[i].tipo == 0):
    return render_template("texto.html",
      indice = int(i),
      enunciado = perguntas[i].enunciado)

  return render_template("quiz.html",
    indice = int(i), 
    enunciado = perguntas[i].enunciado, 
    opcao1 = perguntas[i].opcao1, 
    opcao2 = perguntas[i].opcao2,
    opcao3 = perguntas[i].opcao3, 
    opcao4 = perguntas[i].opcao4, 
    resposta = perguntas[i].resposta,
    num = perguntas[i].num
    )


  








if __name__ == '__main__':   
	app.run( 

  )