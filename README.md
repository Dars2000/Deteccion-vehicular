
<body>
    <div class="container">
        <h1>Sistema de Detección Vehicular</h1>
        <p>Este repositorio contiene un sistema de detección vehicular que utiliza técnicas de visión por computadora y aprendizaje profundo para detectar vehículos en imágenes y videos. El sistema se ha implementado utilizando las siguientes librerías principales: <code>cv2</code>, <code>torch</code>, <code>time</code>, <code>threading</code>, <code>requests</code>, <code>uvicorn</code>, y <code>fastapi</code>.</p>
        <h2>Descripción</h2>
        <p>La detección vehicular es un componente esencial en numerosas aplicaciones, como sistemas de seguridad, monitoreo de tráfico, y análisis de tráfico urbano. Este sistema utiliza técnicas avanzadas de visión por computadora para detectar la presencia de vehículos en imágenes y videos en tiempo real.</p>
        <h2>Funcionalidades</h2>
        <ul>
            <li>Detección de vehículos en imágenes estáticas.</li>
            <li>Detección de vehículos en secuencias de video.</li>
            <li>Interfaz de usuario basada en API utilizando FastAPI para la integración con otras aplicaciones.</li>
            <li>Procesamiento paralelo de múltiples imágenes utilizando hilos (threading) para una mayor eficiencia.</li>
        </ul>
        <h2>Instalación</h2>
        <ol>
            <li>Clona este repositorio en tu máquina local:</li>
        </ol>
        <pre><code>git clone https://github.com/Dars2000/Deteccion-vehicular.git</code></pre>
        <ol start="2">
            <li>Instala las dependencias del proyecto utilizando <code>pip</code>:</li>
        </ol>
        <pre><code>pip install -r requirements.txt</code></pre>
        <h2>Uso</h2>
            <li>Para detectar vehículos en un video, ejecuta el siguiente comando:</li>
        </ol>
        <pre><code>python detect_vehicle_video.py</code></pre>
          <li>PD: Para cambiar la ruta del video entra a Deteccion-vehicular.py y modifica el nombre del video hacia la ruta del otro video</li>
          <br>
        <ol start="3">
            <li>Para iniciar el servidor FastAPI, ejecuta el siguiente comando:</li>
        </ol>
        <pre><code>python API-Prueba.py</code></pre>
            <li>Para leer la api puedes entrar al siguiente link:</li>
        </ol>
        <pre><code>http://localhost:5030/leer</code></pre>
        <h2>Créditos</h2>
        <p>Este proyecto ha sido desarrollado por el Ing. de Sistemas Diego Robertis</a>.</p>
        <h2>Licencia</h2>
        <p>Licencia MIT 2024</p>
</body>
</html>
