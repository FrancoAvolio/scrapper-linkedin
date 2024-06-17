# LinkedIn Connection Bot

## Descripción

Este proyecto es un bot automatizado que utiliza Selenium para enviar solicitudes de conexión en LinkedIn de manera eficiente. El bot navega a través de las páginas de resultados de búsqueda en LinkedIn y envía solicitudes de conexión a las personas que coincidan con los criterios especificados.

## Características

- **Automatización de solicitudes de conexión:** El bot identifica y hace clic en los botones de "Conectar" en las páginas de resultados de búsqueda.
- **Manejo de errores:** El bot maneja posibles errores al intentar enviar solicitudes de conexión.
- **Configuración a través de variables de entorno:** Las credenciales de LinkedIn se cargan desde un archivo `.env` para mayor seguridad.

## Requisitos

- Python 3.x
- Selenium
- ChromeDriver
- Google Chrome

## Instalación

1. **Clona este repositorio:**

    ```bash
    git clone https://github.com/FrancoAvolio/scrapper-linkedin.git
    ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install selenium
    dotenv
    ```

4. **Configura el archivo `.env`:**

    Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

    ```plaintext
    LINKEDIN_EMAIL=tu_correo_de_linkedin@example.com
    LINKEDIN_PASSWORD=tu_contraseña_de_linkedin
    ```

5. **Descarga ChromeDriver:**

    Descarga la versión correcta de ChromeDriver desde [aquí](https://sites.google.com/a/chromium.org/chromedriver/downloads) y asegúrate de que la ruta en tu sistema sea correcta.

## Uso

1. **Ejecuta el script:**

    ```bash
    python bot.py
    ```

    Asegúrate de que Google Chrome está instalado en la ruta especificada en el script y que ChromeDriver se encuentra en el lugar correcto.

## Contribución

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de [LinkedIn](https://www.linkedin.com/in/franco-avolio).
