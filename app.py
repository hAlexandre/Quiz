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

perguntas = []

# MODULO I

perguntas.append(Pergunta(0,
  '<h3>Introdução</h3>Este texto é um guia para conduzir com segurança trabalho no campo de jornalismo com drone. Ele leva em conta os regulamentos de drones atuais da América, a nossa compreensão da aceitação do público de drones, o estado das tecnologias de drones, e nossas próprias experiências.<br /><br /> O objetivo número um de qualquer operação de jornalismo drone é a segurança. Em nenhum momento esta deverá ser comprometida. Se houver qualquer dúvida, voltar o zumbido, também conhecido como um sistema aéreo não tripulado (UAS), para a zona de aterragem e encerrar o voo.<br /><br /> Jornalismo ético é jornalismo responsável, e que arvore um drone significa assumir a responsabilidade pela segurança das pessoas perto de você, na terra e no ar.<br /><br /> Os três papeis operacionais de voo definidos no Manual de Operações Lab jornalismo drone são piloto em comando (PIC), Observador, e jornalista. Um indivíduo pode encher todos os três papéis, que são definidos a seguir:<br /><br /> O piloto em comando: O PIC é responsável por todas as operações de voo. É o PIC que tem a autoridade máxima em qualquer voo. O PIC determina se a aeronave é de navegabilidade e capaz de conduzir as operações propostas. O PIC é responsável por determinar se o espaço aéreo permite a operação proposta. O PIC é responsável pelas operações dentro de todos os regulamentos da FAA e quaisquer restrições estabelecidas por uma concessão da isenção condução. O PIC é responsável por briefing os outros membros da tripulação de voo sobre qual é a missão, os seus papéis e responsabilidades são, e o que se espera deles antes, durante e após as operações de voo.<br /><br /> NOTA: O piloto em comando, segurando o FAA emitida Parte 107 certificado, é por regulamento a autoridade final sobre se a aeronave fls ou não. Se ocorrer um acidente, é titular certificado da Parte 107, que será responsabilizado. Como tal, os gerentes de notícias deve aceitar o piloto na decisão de comando final sobre a segurança do voo.<br /><br /> O observador: O observador é responsável por monitorar a área operacional para garantir que não há riscos que podem pôr em perigo o voo ou pessoas que não fazem parte da equipe de Introdução de voo dos UAS. O Observador é o único membro da equipe que pode falar com o PIC durante as operações de voo. O Observador deve alertar o PIC imediatamente se qualquer aeronave entrar na área, ou se qualquer pessoa ou veículo se aproxima da operação. The Observador deve permanecer dentro da distância de falar do PIC. Não use rádios para se comunicar.<br /><br /> O Jornalista: o jornalista é responsável por comunicar metas de FL para o PIC antes do voo e verificar os resultados após o desembarque. O jornalista determina o que é necessário para a história e comunica que a PIC. O PIC é responsável por determinar se os objetivos do jornalista são possíveis sob as condições apresentadas. Durante voo, o PIC pode pedir feedback do Jornalista, mas o jornalista só deve falar com o piloto, se perguntou, enquanto a aeronave estiver no ar. O jornalista pode atuar como observador.<br /><br /> Nos termos da Parte 107, as operações podem ocorrer com apenas um PIC. Se nenhum pessoal adicional está disponível para o voo, cuidado e consideração deve ser levado para a carga de trabalho adicional que o PIC vai assumir, incluindo ter que assistir a área de operação para os perigos, completando objetivos jornalísticos e garantindo a segurança do voo.<br /><br /> NOTA: Quanto maior o número de variáveis ambientais (espectadores, estruturas, árvores, vento, etc.) em um ambiente operacional, os mais substanciais as demandas estão na PIC.',
    0,1,1,1,1,0,0))


perguntas.append(Pergunta(1,'Tendo em mente o objetivo numero um do jornalismo com drone, o qual procedimento deve ser tomado, caso o mesmo seja quebrado?',
  'Prosseguir com a matéria, pois, mesmo que o tema tenha perdido seu interesse, o objetivo manda que a mesma seja finalizada, mesmo que não seja utilizada posteriormente.',
  '.Deve-se voltar o zumbido também conhecido por UAS para a zona de aterrissagem e finalizar o voo.',
  '(Caso esteja ao vivo) Manter-se firme, mesmo que a exclusividade seja quebrada, pois deve-se manter a fidelidade para com o telespectador que está acompanhando a matéria.',
  'Analisar e estudar, com antecedência, a situação com a qual deseja-se fazer a matéria, para que possa conduzir a reportagem com maior excelência.',
  2, 1, 0))
perguntas.append(Pergunta(2,'Tendo em mente os três papéis de operadores de voo, qual a responsabilidade do PIC?',
  'É de sua responsabilidade monitorar a área operacional para garantir que não há riscos que podem pôr em perigo o voo ou pessoas que não fazem parte da equipe de operações.',
  'É de sua responsabilidade comunicar metas de voo para o piloto antes do voo e verificar os resultados após o desembarque. O PIC determina o que é necessário para a história e comunica que ao jornalista.',
  '.É de sua responsabilidade todas as operações de voo. É o PIC que tem a autoridade máxima em qualquer voo. O PIC determina se a aeronave é de navegabilidade e capaz de conduzir as operações propostas.',
  'O PIC é responsável por permanecer dentro da distância de falar do jornalista para que não se utilize rádios para se comunicar.',
  3, 1, 0))
perguntas.append(Pergunta(3,'Quem pode pilotar um drone com fins jornalísticos?',
  'Apenas o jornalista em questão, pois, para que se tenha boas imagens referentes a matéria, é necessário possuir conhecimento sobre a mesma.',
  'O "câmera", pois, este possui conhecimentos sobre técnicas de filmagem desconhecidos pelo jornalista.',
  '.Apenas um piloto treinado e certificado para isto.',
  'Qualquer pessoa visto que atualmente até mesmo crianças possuem conhecimento',
  3, 1, 0))
perguntas.append(Pergunta(4,'Sobre o Código SPJ de Ética, é correto afirmar que:',
  'Não é necessário demonstrar compaixão por aqueles que podem ser afetados pela cobertura de notícias.',
  '.Equilíbrio necessidade do público por informações contra danos ou desconforto potencial. Buscar por uma notícia não é uma licença para a arrogância ou a intromissão indevida.',
  'Perceber que as pessoas públicas têm um maior direito de controlar informações sobre si mesmos do que figuras privadas e outros que buscam o poder, influência ou atenção.',
  'É permitido atrapalhar a reportagem de outros, se isso for lhe trazer maior vantagem.',
  2, 1, 0))
perguntas.append(Pergunta (5,
  'Considerando o Código Nacional Press Photographers Association de Ética, é incorreto afirmar que:',
  '.Não sabotar intencionalmente os esforços de outros jornalistas a menos que isso lhe traga vantagem maior.',
  'Ao cobrir uma notícia, juntamente com outras organizações de mídia de drones, evitar o uso de seu drone, obstruir ou derrubar outros drones.',
  'Enquanto fotografar assuntos não contribuir intencionalmente, alterar, ou tentar alterar ou em eventos fluêntes.',
  'Considere como o ruído gerado pelos seus UAS, e sua presença, influências eventos, pessoas e animais.',
  1, 1, 1))

  #MODULO II
perguntas.append(Pergunta (0,
  'Uma operação de sistema aéreo não tripulado (sigla em inglês UAS) profissional é aquele que envolve um planejamento cuidadoso e premeditação. Antes de embarcar em utilizar drones para fazer jornalismo, pilotos e as organizações devem tomar várias medidas. Em primeiro lugar, o piloto deve prática com o avião a ser utilizado. Seu primeiro vôo com o avião não deve ser para uma história. Familiarização com a plataforma é essencial. organizações de notícias que querem usar drones deve falar com a polícia e bombeiros locais bem antes quebras de notícias, alertando-os de futuras usando drones de coleta de notícias.<br /><br /> Os procedimentos operacionais gerais para voos de drones são divididos em seções: Pré-viagem, Pré-vôo, vôo, e pós-vôo. Os requisitos gerais de cada um são encapsulado em listas de verificação projetadas para ajudar a garantir que cada passo é realizado. As seções e o raciocínio por trás deles, são descritos aqui:<br /><br /><b>Pré-viagem</b><br /><br /> Antes de empreender qualquer operação voo, o piloto em comando deve reunir informações sobre a área de voo proposta para garantir a segurança das operações que cumprem com os Regulamentos Federal de Aviação.<br /><br /><b> Localização </b>Perguntas o PIC deve responder sobre o local são: <br /><br />-> O que é aquilo? Existem riscos para a aviação? <br /><br />-> O espaço aéreo está? <br /><br />-> Você precisa da permissão de controlo de tráfego aéreo (ATC)? <br /><br /><b>Instruções</b> O PIC é responsável pela instrução de todo o pessoal de operações em cada fase da voar. O PIC irá designar o observador e o jornalista, vai explicar a sua papéis e o que vai acontecer durante o vôo. Uma reunião PIC deve abranger, no mínimo:<br /><br /> -> Quem está cumprindo cada função em operações de voo.<br /><br /> -> As expectativas de cada membro da tripulação de voo.<br /><br /> -> Uma descrição geral da área de operações.<br /><br /> -> O tempo previsto para o local.<br /><br /> -> Quaisquer perigos conhecidos, incluindo ventos, obstáculos, áreas de alto tráfego conhecidas, nenhum os aeroportos mais próximos ou de tráfego aéreo esperado.<br /><br /> -> Os objetivos da missão específicas, incluindo fotos esperados, ângulos ou assuntos.<br /><br /> -> Qualquer privacidade conhecido ou questões éticas e as medidas paliativas.<br /> '
   ,1,1,1,1,1,0,0))

perguntas.append(Pergunta(1,
  'Marque a alternativa incorreta:',
  'Uma operação de sistema aéreo não tripulado envolve um planejamento cuidadoso e premeditado.',
  'O piloto deve ter prática com drone a ser utilizado.',
  '.Usar um novo drone sem pratica.',
  'Organizar as notícias que desejar usar drones.',
  3,1,0))

perguntas.append(Pergunta(2,'Quais são procedimentos gerais para voo com drone?',
  'A) Pré-viagem, Decolar , vôo, pousar.',
  'B) Decolar , vôo, pousar.',
  'C) Pré-vôo, vôo, e pós-vôo.',
  '.D) Pré-viagem, pré-vôo, vôo, e pós-vôo.',
  4,1,0))

perguntas.append(Pergunta(3,'Em relação a pré-viagem no quesito localização qual alternativa é incorreta:',
  'Verificar quantidade de pessoas do local e o que esperar.',
  '.As condições climáticas do local não afeta voo.',
  'Você precisa da permissão de controlo de tráfego aéreo (ATC).',
  'Tem permissão para voo no espaço privado.',
  2,1,0))

perguntas.append(Pergunta(4,'Qual alternativa esta incorreta em relação à pré-viagem:',
  '.Fazer medidas contra falhas no drone.',
  'Fazer uma inspeção pré-viagem.',
  'Verificar local do voo e sua logistica.',
  'Definir as metas operacionais do drone.',
1,1,0))

perguntas.append(Pergunta(5, 'Em uma reunião de pré-viagem o PIC deve abortar alguns temas, mas qual não faz parte dela?',
  '.É permitido atrapalhar a reportagem de outros, se isso for lhe trazer maior vantagem.',
  'Qualquer privacidade conhecido ou questões éticas e as medidas paliativas.',
  'Uma descrição geral da área de operações.',
  'Os objetivos da missão específicas, incluindo fotos esperados, ângulos ou assuntos.',
  1,1,1
  ))

#MÓDULO III
perguntas.append(Pergunta (0,
  '<b>Pré voo </b><br /><br />Operações pré-voo é feito imediatamente antes de qualquer trabalho de vôo é para ocorrer. O Lista de verificação pré-vôo repete algumas da lista de verificação pré-viagem, como inspecionar o aeronaves e algumas das superfícies de controlo. inspeções pré-viagem e pré-vôo ajudar assegurar a aeronavegabilidade e vai servir como um alerta tanto para a manutenção e questões de procurar problemas mecânicos que poderiam substancialmente afetar ou cancelar vôo.<br /><br /> As regras gerais de pré-vôo são:<br /><br /> -> O PIC toca as UAS. O PIC é responsável pela aeronave e todos Ao redor deles. Assim, o PIC vai realizar a inspeção pré-vôo, conectar as pilhas, etc.<br /><br /> -> Quando no local, o pessoal de operações deve delinear uma decolagem e pouso área de pelo menos 10 pés x 10 pés e garantir que ele está livre de detritos. <br /><br /> -> Quando no local, se não as operações de pessoas estão ao redor, o pessoal de operações pode ser necessária para garantir uma área a ser mantido livre de pessoas de modo a UEA pode operam sem voar sobre as pessoas. Esse lugar pode ser a decolagem e pouso zona. Esse espaço, para permanecer livre de pessoas, deve ser tão grande como o PIC acha que é prático. <br /><br /> -> O tempo pode ser muito localizadas. Quando você chegar, você deve verificar o seu clima local contra o relatório do tempo que você tem de um briefing de voo ou serviço de observação automatizada. tectos nuvem será mais difícil estimar no local, para ser razoável. Se as nuvens olhar baixo, fique baixa. Não voe se nevoeiro está presente. <br /><br /> -> As condições de vento também variam conforme a localidade. Um anemômetro é uma ferramenta valiosa para medição de vento no local, informando o PIC, se a velocidade do vento estão dentro limites operacionais e de como elas podem afetar as operações de voo.<br /><br /> -> Desligue a conectividade WiFi em qualquer UAS dispositivos montados, como câmeras. dispositivos WiFi ativos na UAS pode interferir com RC crítica 2,4 GHz e transmissões de vídeo. Porque a maioria dos sistemas UAS não militares usar 2.4GHz tanto para transmissão de vídeo RC ou, só permitem WiFi se você estiver certo lá haverá interferência com o seu hardware UAS.<br /><br /> -> Antes da decolagem, certifique-se a sua bússola não está a receber interferências de objetos metálicos nas proximidades, e que você tem conexões de satélite GPS suficientes.<br /><br /> <b>Voo</b> <br /><br />A lista de verificação de vôo não é realmente uma lista de verificação. É uma lista afazeres. É listado como um lembrete. operadores de UAV devem:<br /><br /> -> Constantemente analisando o tráfego por via aérea ou obstáculos. O observador deve comunicá-los imediatamente. <br /><br /> -> Constantemente analisando as pessoas no chão na área de vôo. O observador deve comunicá-los imediatamente. <br /><br /> -> Verificando constantemente os níveis de bateria e voltando antes de atingir 25 por cento da capacidade restante. <br /><br /> -> Constantemente verificando parâmetros de vôo, como altitude para garantir que eles permaneçam dentro de restrições e objetivos operacionais.Na troca de bateria, e as mudanças de bateria única, se o PIC, Observer e Jornalista discutir mudanças no plano operacional. Enquanto a UEA está em vôo, o PIC precisa se concentrar em voar, e o observador precisa de se concentrar sobre os perigos.'  ,
    1,1,1,1,1,0,0))

perguntas.append(Pergunta(1,
  'Quanto deve ser realizado operação de pré-vôo?',
  'Antes de pousar drone.',
  'Depois de decolar o drone.',
  '.Antes de levantar vôo.',
  'Depois de pousar drone.',
  3,1,0))

perguntas.append(Pergunta(2,
  '.Qual alternativa es correta sobre operação de pré-vôo?',
  'O Pré-vôo repete algumas da lista de verificação pré-viagem.',
  'O pré-vôo não verifica o drone.',
  'O PIC não é responsável pela pessoas ou aeronave.',
  'No pré-vôo não existe a necessidade de verificar há existência de problemas mecânicos.',
  1,1,0))

perguntas.append(Pergunta(3,'Qual alternativa esta incorreta na lista de vôo',
   'Constantemente analisando o tráfego por via aérea e obstáculos.',
   '.Constantemente verificando parâmetros de vôo, como altitude para garantir que eles permaneçam sempre o mais alto possível.',
   'Constantemente analisando as pessoas no chão na área de vôo.',
   'Verificando constantemente os níveis de bateria e voltando antes de atingir 25 por cento da capacidade restante.',
  2,1,0))

perguntas.append(Pergunta(4, 'Verificando constantemente os níveis de bateria e voltando antes de atingir _____ por cento da capacidade restante.',
    '90',
    '5',
    '.25',
    '0',
  3,1,0))

perguntas.append(Pergunta(5, 'Antes da decolagem, certifique-se a sua _________ não está a receber interferências de objetos metálicos nas proximidades, e que você tem conexões de satélite GPS suficientes.',
    '.Bússola',
    'Wi-fi',
    'Bluetooth',
    'Controle',
  1,1,1
  ))

#MÓDULOIV
perguntas.append(Pergunta (0,
  '<b>Pós voo </b><br /><br />A lista de verificação pós-voo de é dividida em três partes: Desligar o zumbido, que é feito pelo PIC; inspecionar a aeronave; e preencher os registros. Registrar é uma parte importante da segurança da aviação e servirá como um documento importante na manutenção do seu UAS.<br /><br /> <b> Registro </b><br /><br />Operações UAS pode ser dividida em três registos separados, em grande parte transportados ao longo da aviação tripulada. Eles são um registro de manutenção, um log da bateria, e um registro de vôo.<br /><br /><b> Registro de manutenção</b><br /><br /> Um registo de manutenção é uma simples lista de questões a ser marcado ou fixado entre voos. PICs devem observar qualquer questão que deve ser verificado, a partir de uma oscilação estranha, som incomum, um motor excepcionalmente quente no pouso, a falha de um componente completo. O registro deve incluir a data, UAS Make & Model, UAS número de registo, o número de identificação da bateria usada quando o problema ocorreu, o problema, que relataram que, a data reparado, que consertou e notas.<br /><br /><b> Registro de bateria </b><br /><br />Um log da bateria serve como um aviso para quando a bateria está ficando desgastada e poderá falhar. baterias UAS degradará, dando progressivamente menos tempo de voo. baterias que vão não utilizados e não são descarregadas mais de uma semana também pode levar a células de bateria danificados totalmente carregada. Um log da bateria irá destacar falhando baterias, e dar o PIC um guia de quanto tempo a bateria vai dar em voo. Um log da bateria deve anotar a data, UAS marca e modelo, número de registo UAS, o número de cargas anteriores, a percentagem de carga restante da bateria durante o desligamento, o tempo total de vôo, taxa de esgotamento da bateria, quaisquer sinais de puffing (um indicador de que a bateria é danificado), e condições de uso. Por exemplo, se você colocou um DJI Inspire com um equipamento de câmera de vídeo de 360 contendo seis câmeras GoPros, e voou sobre uma F 100 °, você faria nota das condições de operação.<br /><br /><b>Registro de voo</b><br /><br /> Um registro de vôo irá destacar os eventos importantes que ocorrem a partir do momento que um UAS decola ao tempo que aterrou e foi desligado pelo PIC. Cada UAS terá seu próprio log. Ele deve anotar a data, a bateria utilizada durante o voo, e o tempo total de vôo. Cada entrada também deve ter espaço para anotações importantes e relevantes sobre o voo, que pode incluir uma visão geral da missão, condições de voo, distância de voo, possui, take-off locais e aterragem, um pouso forçado, etc.',
    1,1,1,1,1,0,0))

perguntas.append(Pergunta(1,
  'Sabendo das três partes que constituem a lista de operações pós-voo, é correto afirmar que:',
  'Deve-se desligar o zumbido, que é feito pelo PIC; inspecionar a aeronave; remover as baterias',
  '.Registrar é uma parte importante da segurança da aviação e servirá como um documento importante na manutenção do seu UAS',
  'Deve-se desligar o drone, que é feito pelo PIC; inspecionar a aeronave; remover as baterias',
  'Não é necessário manter registros após o voo, registros são necessários apenas no pré-voo',  
  2,1,0))

perguntas.append(Pergunta(2,
  'Operações de drone podem ser divididas em quais partes?',
  'Registro de manutenção e um log da bateria.',
  'Log da bateria e um registro de voo.',
  '.Registro de manutenção, um log da bateria, e um registro de vôo.  ',
  'Registro de manutenção, um log da bateria, um registro de voo, e um registro da matéria.',
  3,1,0))

perguntas.append(Pergunta(3,

  'é uma simples lista de questões a ser marcado ou fixado entre voos. PICs devem observar qualquer questão que deve ser verificado, a partir de uma oscilação estranha, som incomum, um motor excepcionalmente quente no pouso, a falha de um componente completo:',    
  'Log da bateria.',
  '.Registro da matéria.',
  'Registro de manutenção.',
  'Registro de voo.' ,
  2,1,0))

perguntas.append(Pergunta(4, 
  'Um log da _________________ deve anotar a data, UAS marca e modelo, número de registo UAS, o número de cargas anteriores, a percentagem de carga restante da bateria durante o desligamento, o tempo total de vôo, taxa de esgotamento da bateria, quaisquer sinais de puffing (um indicador de que a bateria é danificado), e condições de uso',
  'da matéria.',
  '.da bateria.',
  'de manutenção.',
  'de voo.',
  2,1,0))

perguntas.append(Pergunta(5, 
  'De acordo com os textos apresentados, o que é um registro de matéria?',
  'Um registro que deve ser feito pelo jornalista antes de cada operação de voo, contendo todos os dados que devem ser coletados pelo drone durante o voo. Utilizado para auxiliar o PIC.',
  'Um registro que deve ser feito pelo PIC depois de cada operação de voo, contendo todos os dados pertinentes que foram coletados pelo drone durante o voo. Utilizado para relatar ao jornalista o sucesso da missão.',
  'Um registro que deve ser feito pelo jornalista depois de cada operação de voo, a partir dos dados que foram coletados pelo drone durante o voo. Utilizado para verificar o sucesso da missão.',
  '.Nenhuma das anteriores.',
  4,1,1
  ))

#MODULOV
perguntas.append(Pergunta (0,
  '<h3>Procedimentos de Emergência</h3><br /><br /><b>Perda de Sinal/Missão Procedimento</b><br /><br /> Diretrizes Operacionais Gerais: O Sinal RC é para o PIC para controlar diretamente a aeronave. Se o PIC permite que os UAS para operar de forma autônoma e automatizada funcionalidade vôo está perdido, o drone irá reverter para o controle RC e o PIC tomará controle, devolvê-lo para a zona de aterragem e de terras. Se a UEA começa a mostrar qualquer assinatura de não seguir a trajetória de voo automático, e o comando manual não acontecer automaticamente, o PIC deve tomar as medidas necessárias para o manual ao controle. Consulte o manual do UAS para saber como substituir manualmente autónoma operação. Se a ligação é perdida RC, muitos sistemas comerciais são baseados UAS configurada com um retorno automático ao procedimento de casa built-in para o voo de UAS controlador para impedir a dispersão fora da área de operação.<br /><br /><b> Suposição de controle emergência</b><br /><br /> Durante todo o vôo automatizado, se há alguma preocupação de que a UEA não está voando a missão planejada ou que controlam características são anormais, o PIC vai demorar controle manual dos UAS com controle RC, devolvê-lo para a zona de desembarque, se possível, e pousa-lo. Pode haver problemas menores que não requerem pressuposto de emergência de controle. Nestes casos, a comunicação pode GCS dirigir o UAS de desembarque ou o PIC pode pousar manualmente a UEA.<br /><br /><b> Perda da Visão</b><br /><br /> Os regulamentos exigem que os UAS permanecer dentro Visual Line of Sight (VLOS) em tudo casos. Se, que VLOS está quebrado, o PIC deve retornar ao VLOS imediatamente se possível. Se PIC não pode retornar UAS para VLOS, usando o GCS, o PIC deve executar um percurso de voo pré-programado para retornar à zona de pouso.<br /><br /><b> Outros voos Emergências</b><br /><br /> Na maioria das situações de emergência, o protocolo geral é a terra o mais rápido e seguramente prático. Em muitas situações de emergência, o desembarque no patamar pré-determinado zona não será possível. O objetivo é um ambiente controlado, aterragem segura.    <br /><br /> ',
  1,1,1,1,1,0,0))

perguntas.append(Pergunta(1,
  'Qual procedimento PIC deve fazer quando drone esta no automático e mostra qualquer assinatura de não seguir a trajetória de voo automático?',
  'Deixar drone continuar voo automático.',
  'Esperar o drone recuperar trajetória do voo.',
  'Ficar observando.',
  '.Recuperar controle manual do drone.',
  4,1,0))

perguntas.append(Pergunta(2,
  'Q2 – Caso encontre características anormais durante o voo, qual procedimento a ser feito?',
  'Tirar voo automático e continuar no voo manual.',
  'Colocar no voo automático.',
  'Continuar o voo.',
  '.Devolve-lo a zona de desembarque e pousa-lo',
  4,1,0))

perguntas.append(Pergunta(3,
  'Quando houver perda da visão, qual procedimento PIC realiza?',
  'Continuar voo como se não tivesse perdido de vista.',
  '.Executar percurso pré-programado para retornar zona de pouso.',
  'Parar o drone e continuar o voo programado.',
  'Continuar o voo programado mesmo sem visão.',
  2,1,0))

perguntas.append(Pergunta(4, 
  'O que deve ser feito em caso de emergência?',
  '.Fazer pouso num local livre.',
  'Estabelecer controle do drone.',
  'Colocar num programa pré-programado.',
  'Continuar o voo programado.',
  1,1,0))

perguntas.append(Pergunta(5, 
  'Em caso de perda de potência ou falha no motor, não é dever do PIC:',
  '.Alertar outras pessoas sobre a situação de emergência',
  'Registrar detalhes do voô para colocar no relatório',
  'Alertar o pessoal de operações sobre a situação de emergência',
  'Tentar controlar o UAS para realizar um pouso de emergência em alguma área livre',
  1,1,1
  ))




@app.route('/',methods=['GET','POST'])
def indexo():      
  return app.send_static_file('index.html')

@app.route('/videos', methods=['GET', 'POST'])
def videos():
  return app.send_static_file('videos.html')

@app.route('/teste/verifica<modulo>', methods=['POST', 'GET'])
def verificacao(modulo):
  k = int(session['mod1']) + int(session['mod2']) + int(session['mod3']) + int(session['mod4']) + int(session['mod5'])
  sys.stdout.write(str(k)+"\n")
  if(int(modulo) == 1):    
    if(k >= 6):     
      if int((session['certas1'])>=4):         
        return app.send_static_file('jaAprovado.html')     
            
  if(int(modulo)==2):    
    if(k < 5 ):      
      return app.send_static_file('erroModulo.html')
    if (k >= 12 ):
      if(int(session['certas2']) >=4):
        return app.send_static_file('jaAprovado.html')

  if(int(modulo)==3):     
    if(int(k) < 12):
      return app.send_static_file('erroModulo.html')
    if(int(k)  >= 18):
      if(int(session['certas3']) >= 4):
        return app.send_static_file('jaAprovado.html')

  if(int(modulo)==4):     
    if(int(k) < 18):
      return app.send_static_file('erroModulo.html')
    if(int(k)  >= 24):
      if(int(session['certas3']) >= 4):
        return app.send_static_file('jaAprovado.html')

  if(int(modulo)==5):
    if(int(k)<24):
      return app.send_static_file('erroModulo.html')

  


  return redirect('http://localhost:5000/teste')


@app.route('/teste/correcao<questao>', methods=['POST'])
def correcao(questao):    
  i = int(questao)

  if(perguntas[i].tipo == 0 ):    
    if(i<=5):
      session['mod1'] += 1
    else:
      if(i<=12):
        session['mod2'] += 1
      else:
        if(i<=18):
          session['mod3'] += 1
        else:
          if(i<=24):
            session['mod4'] += 1
          else:
            session['mod5'] += 1

        
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
    if(i<=12):
      session['mod2'] += 1
      if(str(respUsuario)==str(respCorreta)):
        session['certas2'] +=1
      session['respondidas2'] +=1    
    else: #Modulo 3
      if(i<=18):
        session['mod3'] += 1
        if(str(respUsuario) == str(respCorreta)):
          session['certas3'] += 1
        session['respondidas3'] +=1
      else:
        if(i<=24):
          session['mod4'] +=1
          if(str(respUsuario) == str(respCorreta)):
            session['certas4'] +=1 
          session['respondidas4'] += 1
        else:
          session['mod5'] += 1
          if(str(respUsuario) == str(respCorreta)):
            session['certas5'] += 1
          session['respondidas5'] +=1




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

  session.pop('mod3', None)
  session.pop('certas3', None)
  session.pop('respondidas3', None)

  session.pop('mod4', None)
  session.pop('certas4', None)
  session.pop('respondidas4', None)

  session.pop('mod5', None)
  session.pop('certas5', None)
  session.pop('respondidas5', None)

  return app.send_static_file('index.html')


@app.route('/progresso/')
def progresso():  
  respondidas1 = int(session['respondidas1'])
  certas1 = int(session['certas1'])
  respondidas2 = int(session['respondidas2'])
  certas2 = int(session['certas2'])
  respondidas3 = int(session['respondidas3'])
  certas3 = int(session['certas3'])
  respondidas4 = int(session['respondidas4'])
  certas4 = int(session['certas4'])
  respondidas5 = int(session['respondidas5'])
  certas5 = int(session['certas5'])

  total1 = 5
  total2 = 5
  total3 = 5
  total4 = 5
  total5 = 5

  if(respondidas1 == 0 ):
    pct12 = 0    
  else:    
    pct12 = 100 * float(certas1/respondidas1)

  if(respondidas2 == 0 ):
    pct22 = 0
  else:
    pct22 = 100 * float(certas2/respondidas2) 

  if(respondidas3 == 0 ):
    pct32 = 0
  else:
    pct32 = 100 * float(certas3/respondidas3)

  if(respondidas4 == 0 ):
    pct42 = 0
  else:
    pct42 = 100 * float(certas4/respondidas4)

  if(respondidas5 == 0):
    pct52 = 0
  else:
    pct52 = 100 * float(certas5/respondidas5)


  pct11 = 100 * respondidas1/total1
  pct21 = 100 * respondidas2/total2
  pct31 = 100 * respondidas3/total3
  pct41 = 100 * respondidas4/total4
  pct51 = 100 * respondidas5/total5

  return render_template("progresso.html",
      respondidas1 = respondidas1,
      certas1 = certas1,
      total1 = total1,
      pct11 =  float("{0:.2f}".format(pct11)),
      pct12 = float("{0:.2f}".format(pct12)) ,
      
      respondidas2 = respondidas2,
      certas2 = certas2, 
      total2 = total2,
      pct21 =  float("{0:.2f}".format(pct21)),
      pct22 = float("{0:.2f}".format(pct22)) ,

      respondidas3 = respondidas3,
      certas3 = certas3, 
      total3 = total3,
      pct31 =  float("{0:.2f}".format(pct31)),
      pct32 = float("{0:.2f}".format(pct32)),

      respondidas4 = respondidas4,
      certas4 = certas4, 
      total4 = total4,      
      pct41 =  float("{0:.2f}".format(pct41)),
      pct42 = float("{0:.2f}".format(pct42)),

      respondidas5 = respondidas5,
      certas5 = certas5, 
      total5 = total5,      
      pct51 =  float("{0:.2f}".format(pct51)),
      pct52 = float("{0:.2f}".format(pct52))
      
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

    session['mod3'] += 1
    session['mod3'] -= 1
    session['respondidas3'] += 1
    session['respondidas3'] -= 1
    session['certas3'] += 1
    session['certas3'] -= 1


    session['mod4'] += 1
    session['mod4'] -= 1
    session['respondidas4'] += 1
    session['respondidas4'] -= 1
    session['certas4'] += 1
    session['certas4'] -= 1

    session['mod5'] += 1
    session['mod5'] -= 1
    session['respondidas5'] += 1
    session['respondidas5'] -= 1
    session['certas5'] += 1
    session['certas5'] -= 1

  except KeyError:
    session['mod1'] = 0
    session['respondidas1'] = 0
    session['certas1'] = 0

    session['mod2'] = 0
    session['respondidas2'] = 0
    session['certas2'] = 0

    session['mod3'] = 0
    session['respondidas3'] = 0
    session['certas3'] = 0

    session['mod4'] = 0
    session['respondidas4'] = 0
    session['certas4'] = 0

    session['mod5'] = 0
    session['respondidas5'] = 0
    session['certas5'] = 0

  i = int((session["mod1"]) ) + int((session["mod2"]) ) + int((session["mod3"]) ) + int((session["mod4"])) + int((session["mod5"]))
  #sys.stdout.write(str(i)+"\n")

  
  
    

  if(i == 6):
    if(int(session['certas1'] < 4)):
      session['mod1'] = 0 
      session['certas1'] = 0
      session['respondidas1'] = 0
      return render_template('refazerModulo.html')

  if(i == 12):
    if(int(session['certas2'] < 4)):
      session['mod2'] = 0 
      session['certas2'] = 0
      session['respondidas2'] = 0
      return render_template('refazerModulo.html')

  if(i == 18):
    if(int(session['certas3'] < 4)):
      session['mod3'] = 0 
      session['certas3'] = 0
      session['respondidas3'] = 0
      return render_template('refazerModulo.html')

  if( i == 24):
    if(int(session['certas4']) < 4):
      session['mod4'] = 0
      session['certas4'] = 0
      session['respondidas4'] = 0
      return render_template('refazerModulo.html')
  
  if (i == 30):
    if(int(session['certas5']) < 4):
      session['mod5'] = 0
      session['certas5'] = 0
      session['respondidas5'] = 0
      return render_template('reafazerModulo.html')


  if (i>=int(len(perguntas))):
    return app.send_static_file('fim.html')
    

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