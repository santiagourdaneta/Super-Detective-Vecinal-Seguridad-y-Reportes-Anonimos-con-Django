import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib # Para guardar y cargar las "memorias" del robot

# --- Primero, el robot aprende a hablar español y a clasificar mensajes ---

# Intentamos cargar el "idioma español" para spaCy. Si no lo encuentra, te avisará.
try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    print("\n¡Advertencia! No se encontró el modelo de spaCy 'es_core_news_sm'.")
    print("Para que el cerebro mágico funcione bien, ejecuta en tu terminal:")
    print("python -m spacy download es_core_news_sm")
    print("Y luego vuelve a iniciar el robot.")
    # Aunque no salga el programa, el procesamiento de IA no funcionará sin esto.
    # Podrías considerar salir aquí con exit() si la IA es crítica.
    nlp = None # Marcamos que no se pudo cargar

# Simulamos algunos ejemplos de mensajes para que el robot aprenda.
# En la vida real, tendríamos MUCHOS más ejemplos.
ejemplos_mensajes = [
    "Vi un coche sospechoso merodeando por la calle Los Sauces.",
    "Una persona extraña observaba las casas en la esquina de la Calle Real.",
    "Mucho ruido en el parque, parece una fiesta de vecinos.",
    "Me siento inseguro por la noche en esta zona cerca de la plaza.",
    "Unos chicos estaban jugando ruidosamente en el parque, nada grave.",
    "Necesitamos más luz en la calle principal, está muy oscuro.",
    "Robaron una bicicleta cerca de mi casa, en la calle del Sol."
]

# Le decimos al robot si el ejemplo es de "seguridad" (1) o "no seguridad" (0)
etiquetas_seguridad = [1, 1, 0, 1, 0, 0, 1]

# Creamos una herramienta para convertir texto en números (así el robot los entiende)
vectorizador = TfidfVectorizer(max_features=1000)
X = vectorizador.fit_transform(ejemplos_mensajes)

# Entrenamos a un "detector de incidentes de seguridad"
modelo_seguridad = LogisticRegression()
modelo_seguridad.fit(X, etiquetas_seguridad)

# Guardamos estas "memorias" para que el robot no olvide cómo clasificar
joblib.dump(vectorizador, 'vectorizador.pkl')
joblib.dump(modelo_seguridad, 'modelo_seguridad.pkl')

# --- Funciones que el robot usará cuando reciba un mensaje ---

# Esta función predice si un mensaje es de seguridad o no
def predecir_tipo_mensaje(texto):
    if nlp is None: # Si el modelo de spaCy no cargó, no podemos predecir bien
        return 0 # Por seguridad, asumimos que no es de seguridad para no alarmar

    # Convierte el mensaje nuevo en números para que el modelo lo entienda
    texto_vectorizado = vectorizador.transform([texto])
    # El robot predice si es de seguridad (1) o no (0)
    return modelo_seguridad.predict(texto_vectorizado)[0]

# Esta función hace el mensaje anónimo y, si es de seguridad, lo enfatiza
def procesar_mensaje_ia(mensaje_original):
    if nlp is None: # Si spaCy no está, solo anonimizamos lo básico
        return f"Mensaje anónimo (sin IA avanzada): {mensaje_original.replace('calle', '[calle]').replace('plaza', '[plaza]')}"

    # Usamos spaCy para encontrar nombres de personas, lugares, organizaciones y los ocultamos
    doc = nlp(mensaje_original)
    mensaje_anonimo = mensaje_original
    for ent in doc.ents:
        # Reemplaza entidades conocidas como PERSONAS, LUGARES, ORGANIZACIONES por [OMITIDO]
        if ent.label_ in ["PERSON", "LOC", "ORG", "GPE"]: # GPE también es lugar/país/ciudad
            mensaje_anonimo = mensaje_anonimo.replace(ent.text, "[OMITIDO]")

    # Si el robot predice que es un mensaje de seguridad, lo marca como ALERTA
    if predecir_tipo_mensaje(mensaje_original) == 1:
        return f"ALERTA (por Super Detective Robot): Mensaje de seguridad anónimo: {mensaje_anonimo}"
    else:
        return f"Mensaje anónimo del robot: {mensaje_anonimo}"