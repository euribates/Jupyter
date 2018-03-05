Los sistemas de Lindenmayer, o Sistemas-L (L-systems), porporcionan una técnica
muy potente para la generación de fractales. Lindenmayer usó los sistemas-L
para describir el comportamiento de celulas vegetales y para modelar el proceso
de crecimiento de una planta.

Un sistema-L es un sistema de reescritura, y formalmente son un tipo 
de gramática. Consiste en un conjunto de **símbolos** o alfabeto
(que se pueden usar para generar cadenas de cadenas de texto), un
conjunto de **reglas de producción** que pueden expandir cada símbolo
en una cedena más larga de símbolos, un **axioma** o cadena de simbolos
inicial, y algún mecanismo para convertir las cadenas generadas en forma
de estructuras geométricas.

Para ver un ejemplo sencillo, veamos el sistema-L original que usó Lindenmayer
para modelar el crecimiento de un alga. En este sistema trabajamos con
solo dos símbolos, `A` y `B`. Las reglas son las siguientes:

- Cuando encontremos `A`, cambiarlo por `AB` (A -> AB)
- Cuando encontremos `B`, reemplazarlo con A (B -> A)

Empezamos con el símbolo 'A', asi que aplicando la primera regla generamos
`AB` y terminamos esta iteración. Empezamos ahora con `AB`. De nuevo,
sustituimos `A` por `AB`, pasamos al segundo caracter, `B`, y lo reemplazamos
por `A` siguiendo la segunda regla, con lo que el resultado final es
`ABA`. En la tercera iteración, se obtiene la cadena de texto `ABAAB`, en 
la cuarta `ABAABABA`, y así sucesivamente.

**Nota:** La longitud de cada una de estas cadenas consecutivas es 1, 2, 3, 5,
8... ¿Le recuerda algo? Pista: Añadir otro uno antes de la secuencia.

Podemos extender este sistema básico con algunas instrucciones, como por
ejemplo, `-` para indicar `gira hacia la izquierda en un determinado ángulo` 
y `+` para indicar giro a la derecha. `F` podría significar `Sigue adelante`.
Estas instrucciones pueden ser representadas de forma muy fácil usando
gráficos de tipo tortuga. Por ejemplo, la [Curva de Hilbert](https://es.wikipedia.org/wiki/Curva_de_Hilbert)
puede dibujarse mediante las siguientes reglas:

A -> − B F + A F A + F B −

B -> + A F − B F B − F A +




- Sistemas L: <https://en.wikipedia.org/wiki/L-system>
