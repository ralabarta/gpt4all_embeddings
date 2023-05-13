Proyecto de Aprendizaje de Documentos y Recuperación de Información con Llama Embeddings

Este proyecto consta de dos programas principales: doc_learn.py y chat.py. Ambos scripts están escritos en Python y utilizan el módulo langchain para cargar y procesar documentos, crear embeddings de texto con el modelo Llama y realizar consultas de recuperación de información.
Dependencias

El proyecto depende de las siguientes bibliotecas de Python:

    dotenv: para cargar variables de entorno desde un archivo .env
    langchain: para cargar documentos, dividir texto, crear y almacenar embeddings, y realizar consultas de recuperación de información
    os: para interactuar con el sistema de archivos del sistema operativo

Configuración

El proyecto requiere que las siguientes variables de entorno estén definidas en un archivo .env:

    LLAMA_EMBEDDINGS_MODEL: La ruta al modelo de embeddings de Llama
    PERSIST_DIRECTORY: El directorio en el que se almacenará la base de datos de Chroma
    MODEL_N_CTX: Parámetro del modelo Llama
    MODEL_PATH: Ruta al modelo de lenguaje (para chat.py)

doc_learn.py

Este script carga documentos de texto, PDF y CSV desde el directorio source_documents, los divide en fragmentos, crea embeddings para cada fragmento utilizando el modelo Llama, y almacena los embeddings en una base de datos Chroma.

La base de datos de Chroma se guarda en el directorio especificado por la variable de entorno PERSIST_DIRECTORY.
Uso

Para ejecutar doc_learn.py, simplemente ejecute el script con Python:

bash

python doc_learn.py

chat.py

Este script utiliza la base de datos Chroma creada por doc_learn.py para realizar consultas de recuperación de información.

El usuario puede introducir una consulta y el programa buscará en la base de datos Chroma los fragmentos de texto más relevantes, los pasará a través del modelo de lenguaje, y presentará la respuesta generada por el modelo, junto con los fragmentos de texto fuente utilizados para generar la respuesta.
Uso

Para ejecutar chat.py, simplemente ejecute el script con Python:

bash

python chat.py

A continuación, se le pedirá que introduzca su consulta. Para terminar el programa, introduzca exit.
Advertencia

Este proyecto está destinado a ser utilizado con fines de demostración y no es adecuado para su uso en un entorno de producción sin modificaciones significativas. Por favor, asegúrese de entender completamente el código y las implicaciones de su uso antes de ejecutarlo en un entorno de producción.
