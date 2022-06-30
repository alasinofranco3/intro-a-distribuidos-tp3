# TP3 - Introducción a los sistemas distribuidos - FIUBA

[Link al informe](https://es.overleaf.com/project/62ba10333057de5bc123a840)

## Comando útiles

1. Correr controlador utilizando POX

```
./pox/pox.py --verbose controller
```

2. Correr Mininet

```
sudo mn --custom myTopo.py --topo linear,<switches_amount> --mac --arp --switch ovsk --controller remote
```

3. Una vez dentro de mininet, utilizando el comando que se detalla a continuación, vamos a abrir dos terminales de xterm para poder visualizar un servidor y un cliente y hacer diversas pruebas usando iperf

```
>mininet xterm h1 h2
```

4. Levantar un servidor escuchando en el puerto 5000 TCP (ejecutar en la consola H1 abierta en el punto 3)

```
iperf -s -p 5000
```

5. Levantar un cliente enviando paquetes TCP al puerto 5000 de host 1 (ejecutar en la consola H2 abierta en el punto 3)

```
iperf -c "10.0.0.1" -p 5000
```

6. Levantar un servidor en el puerto 5000 UDP (ejecutar en la consola H1 abierta en el punto 3)

```
iperf -s -p 5000 -u
```

7. Levantar un cliente enviando paquetes UDP al puerto 5000 de host 1 (ejecutar en la consola H2 abierta en el punto 3)

```
iperf -c "10.0.0.1" -p 5000 -u
```

## [Visualizador de topología](http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet)

## Archivo de configuración

En el archivo de configuración que se encuentra en /pox/ext/config.py se pueden configurar distintas variables para afectar las reglas del controlador.

## Simulaciones

Utilizando los comandos anteriormente descriptos, en el informe linkeado se pueden observar capturas de las distintas pruebas realizadas para comprobar el correcto funcionamiento del Firewall.
