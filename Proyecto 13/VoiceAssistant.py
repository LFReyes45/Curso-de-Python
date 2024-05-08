import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar el micro y devolver el audio como texto
def transformar_audio_a_texto():
    # Almacenar reconocedor en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8
        # Informar que comenzó la grabación
        print('Ya puedes hablar')
        # Guardar lo que se escuche como audio
        audio = r.listen(origen)
        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language='es-Mx')
            # Prueba de que pudo ingresar
            print('Dijiste: ' + pedido)
            # Devolver pedido
            return pedido

        # En caso de no comprender el audio
        except sr.UnknownValueError:
            # No comprendió el audio
            print('No entendí')
            return 'Espero'
        # En caso de no resolver el pedido
        except sr.RequestError:
            # No se pudo resolver el audio
            print('No resuelvo')
            return 'Espero'
        # Error inesperado
        except Exception as e:
            # Ocurrió un error inesperado
            print('Algo salió mal:', str(e))
            return 'Espero'


#Función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id)
    # Pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():
    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario nombres de día
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el dia de la semana
    hablar(f'Hoy es: {calendario[dia_semana]}')


# Informar qué hora es
def pedir_hora():
    #Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    # Decir la hora
    hablar(hora)


# Saludo inicial
def saludo_inicial():
    # Variables de datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas Noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen Día'
    else:
        momento = 'Buenas Tardes'

    # decir el saludo
    hablar(f'{momento}, soy Sabina, tu asistente personal. Por favor, dime qué necesitas')


# Funciones de pedidos del asistente
def pedir_cosas():
    # activar saludo
    saludo_inicial()
    # Variable de corte
    comenzar = True

    # loop central
    while comenzar:
        # Activar micro y guardar el pedido en un String
        pedido = transformar_audio_a_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, un momento')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Con gusto, espera un segundo')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Claro, espera un segundo')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Realizaré la busqueda y lo reproduciré')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue

        elif 'adiós' in pedido:
                hablar('Me voy a descansar, cualqueir cosa me ejecutas ☺')
                break


id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

pedir_cosas()
