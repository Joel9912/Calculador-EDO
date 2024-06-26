# Calculadora de Ecuaciones Diferenciales Ordinarias (EDO)

## Ingrese los parámetros de la EDO:

<form id="edo-form" onsubmit="return submitForm()">
    <label for="edo">Ecuación Diferencial:</label><br>
    <input type="text" id="edo" name="edo"><br><br>

    <label for="condiciones_iniciales">Condiciones Iniciales (x0, y0):</label><br>
    <input type="text" id="condiciones_iniciales" name="condiciones_iniciales"><br><br>

    <label for="posicion_final">Posición Final (xf):</label><br>
    <input type="number" id="posicion_final" name="posicion_final"><br><br>

    <label for="iteraciones">Número de Iteraciones (n):</label><br>
    <input type="number" id="iteraciones" name="iteraciones"><br><br>

    <input type="submit" value="Calcular">
</form>

<div id="graficas"></div>

