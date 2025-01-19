#import "template.typ": project

#show: project.with(
  abstract: "Queremos ver una forma aproximada de determinar la complejidad de un laberinto y como generar laberintos de dicha complejidad."
)

= Determinación de la dificultad

En primer lugar, consideremos la definición de la dificultad de un laberinto.

Supongamos que el tablero puede ser representado como un grafo $G=(V,E)$, donde $|V|=n^2$ y estamos en un tablero de dimensiones $n times n$, en el cual cada nodo representa una casilla y cada arista representa la conexión (es decir, la ausencia de una pared) con otra casilla adyacente.

También tenemos un nodo etiquetado como $s$ para la entrada y otro nodo $t$ para la salida

A continuación veremos los factores determinantes.


== Factores determinantes

=== Número de bifurcaciones

Llamemos al número de bifurcaciones $cal(B)$, donde 

$ cal(B) = |{v in V | deg(v) > 2}| $

Decimos que el grado de cada nodo debe ser mayor que 2 ya que si $deg(v) = 2$ es parte del mismo camino entre bifurcaciones, y si $deg(v) = 1$ es un camino cerrado.

=== Caminos cerrados

Como notamos anteriormente, si $deg(v) = 1$ entonces tenemos un camino cerrado, notamos al conjunto de todos los caminos cerrados del laberinto $G$ como

$ cal(D) = |{v in V | deg(v) = 1}| $

=== Cantidad de ciclos

  $ cal(C) = |E|-|V|+1 $

=== Profundidad

$ cal(P) = max_(v in V) delta(s,v)  $

=== Densidad de $G$
Llamamos $rho$ a la densidad del grafo $G$ tal que

$ rho = (2|E|)/(|V|^2-|V|) $

=== Relación entre caminos cerrados y cantidad de nodos

$ d cal(R) v = cal(D)/(|V|) $

=== Relación entre bifurcaciones y caminos cerrados

$ b cal(R) d = cal(B)/cal(D) $

// == Factor de desviación

// == Complejidad media para cada camino

== Dificultad final
Llamamos a la dificultad del laberinto como $cal(W)$ y cada $w_i$ es el peso que tiene cada factor
$ cal(W) = w_1 cal(B) + w_2 cal(D) + w_3 cal(C) + w_4 cal(P) + w_5 cal(rho)+ w_6 d cal(R) v + w_7 b cal(R) d $

