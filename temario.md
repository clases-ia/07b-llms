Este es el temario de la clase que voy a hacer:

- del Transformer al Chatbot
- cómo elegir LLM
- buenas prácticas
- intro a openrouter/-conexión desde el código
- editando texto a escala a través de API

Te explico un poco. La primera parte explica en una o dos slides cómo pasamos de un transformer
que solo predice la siguiente palabra a un chatbot que está optimizado para responder preguntas
de forma adecuada (podemos mencionar tanto la parte de aprendizaje supervisado como RLHF).

En cómo elegir LLM la idea es hablar de LMArena y el Intelligence index de Artificial Analysis, los
que permiten hacerse una idea de balance costo/inteligencia y qué modelos son más inteligentes para qué tareas.

En buenas prácticas, la idea es mencionar desde manejo de contexto a temas de protección de datos (somos una institución
pública, no podemos mandar datos privados a la nube, si es que existe en otro país)

En la intro a openrouter la idea es explicar rápido qué es (luego de una explicación breve puedes dejar un link a la
página, que yo mostraré en vivo) y luego pasar a ejemplos de código cómo setearlo, cerrando con una llamada a algún
modelo.

En la última sección la idea es hacer un ejemplo más aterrizado. Pensaba un dataframe de unas cinco filas, con una
columna de texto con problemas de ortografía y gramaticales y pedirle a la LLM que genere una versión corregida del
texto.

La idea es que crees un primer .qmd con esta clase.

Notas:

Puedes dejar placeholders para imágenes, que yo luego puedo generar.

En @apoyo/index.qmd tienes un ejemplo de la clase anterior. La idea es que esta clase sea considerablemente menos
intensa en términos teóricos eso sí, pero puede servirte como referencia. Luego de sufrir el álgebra,
la idea es que esta tenga un foco más pragmático. Por lo tanto, para la parte inicial sobre el paso de
Transformer a chatbot basta con dar la intuición de los conceptos, no es necesario entrar en el álgebra.

Si no tienes claridad respecto a alguno de estos temas, puedes buscar referencias en internet, para mayor
claridad.