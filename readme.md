# Dino Runner

Un emocionante juego de escritorio en Python con Pygame, inspirado en el famoso juego del dinosaurio de Google.

## Descripción

"Dino Runner" es un juego en el que controlas a un dinosaurio que corre automáticamente, evitando obstáculos como cactus y aves. El objetivo es sobrevivir el mayor tiempo posible y acumular la mayor cantidad de puntos.

## Características Principales

- **Movimientos Básicos:**
  - Salta con la flecha hacia arriba.
  - Agáchate con la flecha hacia abajo.

- **Vidas:**
  - Comienzas con tres vidas.
  - Pierdes una vida al tocar un cactus o ave.
  - Al perder todas las vidas, el juego termina.

- **Velocidad y Puntaje:**
  - La velocidad de los obstáculos aumenta con el puntaje.
  - El juego avanza automáticamente.

- **Power Ups:**
  - **Martillo:** Destruye obstáculos en un rango de tiempo de 2 a 9 segundos.
  - **Escudo:** Proporciona inmunidad durante un tiempo determinado.
  - **Corazón:** Otorga una vida extra acumulable.

## Imágenes de Power Ups

A continuación, se muestran imágenes de cada power-up:

### Martillo

![Martillo](/dino_runner/assets/Other/imageWithHammer.png)
![Martillo](/dino_runner/assets/Other/useHammer.png)

### Escudo

![Escudo](/dino_runner/assets/Other/imageWithShield.png)
![Escudo](/dino_runner/assets/Other/useShield.png)

### Corazón

![Corazón](/dino_runner/assets/Other/useHeart.png)

## Instalación
![Alt text](image.png)
1. Clona el repositorio:

    ```bash
    git clone https://github.com/Daniel-Acosta-Perez/JDAP-Dino-Runner.git
    ```

2. Instala los requerimientos:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta el juego:

    ```bash
    python main.py
    ```



## Contacto

Para cualquier pregunta o comentario, contáctame en [juan.acostaperez2@gmail.com](mailto:juan.acostaperez2@gmail.com).


## Historial de Cambios

### Versión 1.0.0 (Nov 2023)

- Archivo Readme

## FAQ

### ¿Cómo puedo destruir obstáculos con el martillo?

Se destruirá automáticamente cuando toques un obstáculo y tengas el efecto del power up.
