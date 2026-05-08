# 📚 FlashPy_CLI

Una aplicación de línea de comandos (CLI) ligera y eficiente, escrita en Python, diseñada para crear, gestionar y estudiar flashcards. Desarrollada utilizando los principios de **Programación Orientada a Objetos (POO)** y almacenamiento persistente mediante **JSON**.

## ✨ Características Principales

*   **Creación Ágil:** Añade rápidamente el concepto (anverso) y la definición (reverso) de tus tarjetas de estudio.
*   **Persistencia de Datos:** Todas las flashcards se guardan automáticamente en un archivo `mis_flashcards.json`. Si el archivo no existe, el programa lo crea por ti.
*   **Modo Estudio Interactivo:** Repasa tus tarjetas directamente desde la terminal, revelando las respuestas a tu propio ritmo.
*   **Arquitectura Limpia:** Construido con POO, dividiendo la lógica en clases bien definidas para facilitar la escalabilidad y el mantenimiento.
*   **Soporte UTF-8:** Manejo seguro de caracteres especiales, tildes y eñes (ideal para estudiar en español u otros idiomas).

## 🏗️ Estructura del Código (POO)

El proyecto está modularizado en tres clases principales:
1.  `Flashcard`: Representa la entidad de la tarjeta individual y su capacidad para serializarse a diccionarios.
2.  `GestorFlashcards`: Maneja la lógica de negocio, la colección en memoria y las operaciones de lectura/escritura del archivo JSON.
3.  `AppConsola`: Controla la interfaz de usuario, los menús y la interacción por teclado.

## 🚀 Requisitos e Instalación

Este proyecto utiliza únicamente la biblioteca estándar de Python, por lo que **no necesitas instalar dependencias externas** (ni `pip install`).

**Requisito:** Python 3.6 o superior.

**Pasos para ejecutar:**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/NeoByteMX/FlashPy_CLI.git](https://github.com/NeoByteMX/FlashPy_CLI.git)
2. Navega al directorio del proyecto:
   ```bash
   cd FlashPy_CLI
3. Ejecuta el script principa:
   ```bash
   python main.py
