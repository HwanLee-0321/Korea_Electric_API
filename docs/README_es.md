# Guía de Utilización de la API de Korea Electric Power Corporation (KEPCO)

Este proyecto proporciona un backend Python orientado a objetos para recopilar datos de la API de datos públicos de Korea Electric Power Corporation (KEPCO) y un frontend basado en Electron para interactuar con él.

## Idiomas Disponibles

*   [Inglés](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## Características Clave

*   **Backend Python Orientado a Objetos:** Recopila varios datos relacionados con la energía proporcionados por KEPCO a través de su API, estructurados en las clases `KepcoApiClient` y `DataCollector` para una mejor mantenibilidad y extensibilidad.
*   **Frontend Electron:** Una aplicación de escritorio construida con Electron, que proporciona una interfaz gráfica de usuario para activar la recopilación de datos y mostrar los resultados.
*   **Configuración de Clave API:** Fácil configuración de la clave API a través de un archivo `config.py`.
*   **Salida de Datos:** Los datos recopilados se envían a la salida estándar (stdout) mediante el script de Python, que luego es capturado y mostrado por la aplicación Electron.

## Requisitos

*   **Python 3.11+**
    *   Librería `requests`
*   **Node.js (se recomienda LTS)**
    *   `npm` (Node Package Manager)
    *   `electron`

## Instalación y Configuración

1.  **Clonar el Repositorio:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Instalar Dependencias de Python:**

    ```bash
    pip install requests
    ```

3.  **Instalar Dependencias de Node.js:**

    ```bash
    npm install
    ```

4.  **Configuración de la Clave API:**

    *   Visita el Portal de Datos Públicos de KEPCO ([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/)), regístrate, solicita el uso de la API y obtén una clave de autenticación (API Key).
    *   Abre `config.py` en el directorio raíz del proyecto e introduce tu clave API obtenida como se muestra a continuación.

    ```python
    # config.py
    API_KEY = "INTRODUCE_TU_CLAVE_API_AQUI"
    ```

    **Importante:** El archivo `config.py` contiene información sensible, por lo que se recomienda añadirlo a tu archivo `.gitignore` para evitar que se incluya en tu repositorio Git.

## Uso

### Ejecutar la Aplicación Electron

Para iniciar la aplicación de escritorio:

```bash
npm start
```

Haz clic en el botón "Fetch KEPCO Data" (Obtener Datos de KEPCO) en la aplicación para iniciar la recopilación de datos. Los datos recopilados se mostrarán dentro de la ventana de la aplicación.

### Ejecutar el Backend Python (Independiente)

También puedes ejecutar el script de Python directamente desde la terminal. Los datos recopilados se imprimirán en la salida estándar.

```bash
python main.py
```

## Estructura del Proyecto

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # Cliente API de KEPCO para realizar solicitudes
│   └── collector.py    # Orquesta la recopilación de datos
├── src/
│   ├── main/
│   │   ├── main.js         # Proceso principal de Electron
│   │   └── preload.js      # Script de precarga de Electron
│   └── renderer/
│       ├── index.html      # HTML del proceso de renderizado
│       ├── renderer.js     # JavaScript del proceso de renderizado
│       └── style.css       # Estilos del proceso de renderizado
├── config.py           # Clave API y configuración
├── main.py             # Punto de entrada para el backend Python
├── kepco_codes.json    # (Generado) Almacena códigos regionales y de datos
├── package.json        # Configuración del proyecto Node.js
├── package-lock.json   # Archivo de bloqueo de dependencias de Node.js
├── README.md           # Descripción del proyecto (Inglés)
├── README_ko.md        # Descripción del proyecto (Coreano)
├── README_zh.md        # Descripción del proyecto (Chino)
├── README_ja.md        # Descripción del proyecto (Japonés)
├── README_es.md        # Descripción del proyecto (Español)
├── README_de.md        # Descripción del proyecto (Alemán)
├── README_fr.md        # Descripción del proyecto (Francés)
├── README_ar.md        # Descripción del proyecto (Árabe)
├── LICENSE             # Información de la licencia del proyecto
└── ... (otros archivos como .git, node_modules, etc.)
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

-----

**Descargo de responsabilidad:** Este proyecto no es proporcionado oficialmente por Korea Electric Power Corporation y está destinado a ser un ejemplo de referencia para ayudar con la utilización de la API.