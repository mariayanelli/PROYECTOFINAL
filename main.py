from nltk.chat.util import Chat, reflections
pares = [
    [
        r"mi nombre es(.*)",
        ["Hola %1, como estas ?",]
    ],

    [
        r"bien y tu ?",
        ["Bien tambien, es aqui por el sitio web que hicieron mis creadoras cierto?",]
    ],

    [
        r"Si|Como lo supo|Asi es",
        ["Ya lo sabia, ahora dime en que puedo ayudarte?",]
    ],

     [
        r"Cual es tu nombre ?",
        ["Mi nombre es MM",]
    ],

    [
        r"Porque MM ?",
        ["Mis creadoras se llaman Maria y Montserrat",]
    ],

    [
        r"Que interesante ?",
        ["Si lo es","Por supuesto","Verdad que si?",]
    ],

    [
        r"Que haces MM ?",
        ["Platicando contigo",]
    ],

     [
        r"Como va tu dia ?",
        ["Excelente y el tuyo","Muy bien gracias y el tuyo",]
    ],

     [
        r"Tambien|Igual gracias |Perfecto gracias",
        ["Excelente y el tuyo","Muy bien gracias y el tuyo",]
    ],

    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],

    [
        r"hola|hey|buenas tardes|buenas noches|buenos dias|Hola que tal",
        ["Hola", "Que tal",]
    ],

    [
        r"puedo preguntarte lo que sea ?",
        ["Me gustaria que fueran las preguntas que estan en el READMEOK ",]
        
    ],

    [
        r"OK|Me parece bien|Esta bien|Perfecto ",
        ["Pues comencemos...",]
    ],

    [
        r"(.*) creado ?",
        ["Fui creado hoy jejeje",]
    ],

    [
        r"adios|bye",
        ["Chao","Fue bueno hablar contigo","adios,cuidate",]
],

[
        r"La inteligencia de una máquina puede ser igual o superior a la de un humano ?",
        ["El propósito principal de esta tecnología es ejecutar tareas del nivel de complejidad de los humanos. Es decir, reemplazar una función operativa que, se supone, las personas podemos hacer. Mirándolo así, es muy difícil que una máquina pueda tener una inteligencia superior a la de un humano. Una de las distinciones de la Inteligencia Artificial es el machine learning: la capacidad de ir aprendiendo a medida que va recibiendo datos para así tomar mejores decisiones.",]
    ],

[
        r"Qué trabajos están en riesgo de extinción por la IA ?",
        ["La Inteligencia Artificial nos conducirá hacia una sociedad en la que se irán automatizando aquellas tareas que requieran muy poco tiempo para pensar en cómo hacerlas. Se irán automatizando paulatinamente por algoritmos de IA. Un estudio reciente realizado en la Universidad de Oxford clasificó los empleos más difíciles de sustituir en 3 categorías: empleos que requieren el uso de las manos (dentistas, bomberos...), empleos que requieren creatividad (coreógrafos, directores de arte...) y empleos que requieren percepción social (sacerdotes, enfermeros...).",]
    ],

[
        r"Puede la IA crear ?",
        ["Una IA aprende a partir de datos y de la propia experiencia, como es el caso de AlphaGO, la IA que creó la empresa Google Deep Mind para jugar al Go y que ganó al campeón del mundo Lee Shedol, realizando jugadas que fueran catalogadas como creativas y lejos de los movimientos de piezas que suelen hacer los jugadores humanos en similares posiciones. La IA puede crear. Ya hay diseño de IAs con experimentos para escribir pequeños artículos sobre noticias locales, hay IAs que imitan un estilo de pintura, hay IAs que crean música, y veremos IAs que escribirán libros. Cada vez habrá más.",]
    ],

[
        r"Sustituirán las máquinas a los médicos ?",
        ["No, esta es una profesión donde la IA les ayudará a ser supermédicos, con sistemas inteligentes de ayuda a la toma de decisiones que les aportará información de gran calidad en tiempo real a partir de los datos de los pacientes. A la inteligencia artificial se le da muy bien reunir datos y analizarlos para ofrecer información más completa sobre síntomas, diagnósticos y tratamientos. Pero no puede atender a los pacientes como hacen los humanos. Es esa combinación de capacidades la que puede revolucionar la medicina.",]
    ],

[
        r"Si la IA puede sustituir a los humanos, por qué lo hacemos ?",
        ["La IA no puede sustituir a los humanos. Una premisa básica propuesta por los expertos en ética en los campos de la IA y la robótica es que la creación de IAs debería llevarse a cabo siempre con la visión de que están ayudándonos a tener una vida mejor, promoviendo el bienestar de la especie humana. La IA permitirá investigaciones más rápidas sobre enfermedades graves y sus curas, reducir el número de accidentes de tráfico con los coches autónomos, estimulará el crecimiento económico... Yun largo etcétera.",]
    ],

[
        r"Dejaremos de conducir ?",
        ["Sí, a medio plazo los coches autónomos no tendrán volante y bastará con darles la dirección a la que queremos ir. Esto, aunque pueda parecer otra cosa, está más cerca de lo que se puede pensar. Lo tenemos a la vuelta de la esquina.",]
    ],

[
        r"Quien es considerado el padre de la IA ?",
        ["Jonh McCarthy, una leyenda para programadores y hackers",]
    ],


[
        r"Cómo podemos aplicar la inteligencia artificial ?",
        ["Cómo podemos aplicar la IA en nuestra vida cotidiana, es una de las preguntas clave del mundo de hoy. Al igual que con las otras tecnologías de la cuarta revolución industrial, cómo antes mencionamos no es necesario ser un desarrollador de la IA o trabajar en las grandes empresas tecnológicas. Cada uno de nosotros debería pensar cómo podemos aplicar la Inteligencia Artificial en las diferentes áreas de nuestras vidas personales y profesionales.",]
    ],

[
        r"Que es un chatbot ?",
        ["Un chatbot es un programa informático con el que es posible mantener una conversación, tanto si queremos pedirle algún tipo de información o que lleve a cabo una acción.",]
    ],

[
        r"Como funciona un chatbot ?",
        ["Los chatbots incorporan sistemas de inteligencia artificial. Por tanto, tienen la posibilidad de aprender sobre nuestros gustos y preferencias con el paso del tiempo. Siri o Cortana, por ejemplo, funcionan a gracias a este sistema (aunque todavía presentan un gran margen de mejora). Otros lugares en los que han estado en funcionamiento en los últimos años ha sido en chats como Facebook Messenger o en aplicaciones de mensajería instantánea como Telegram o Slack. En estas últimas los chatbots estaban incorporados como si fueran un contacto más.",]
    ],

[
        r"Menciona algun robot famoso de la historia ?",
        ["R2-D2", "HK-47", "Tachikomas", "Johnny 5", "Robbie", "Astro Boy","K-9", "Terminator", "Hal 9000", "Cylons", "Data Bender", "Wall-E","Roy Batty" ,]
    ],

[
        r"Pelicula que pueda relacionarse con la IA ?",
        ["Matrix","Matrix Reloaded","Blade Runner","Ex Machina", "Her",]
    ],

[
        r"Gracias (.*)",
        ["Fue un placer","No es nada","Gracias a ti",]
    ],

[
        r"Que pregunta planteaba Alan Turing en 1950 ?",
        ["Se cuestionaba el que si las maquinas podian pensar",]
    ],
    
[
r"None ?",
["Lo siento pregunta o contesta de nuevo no logro entender",]
 ],


]

def chatear():
    print("HOLA SOY UN BOT , ¿cual es tu nombre?") 
    chat = Chat(pares, reflections)
    chat.converse()
if __name__ == "__main__":
    chatear()