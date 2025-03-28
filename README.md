# Ejercicio Técnico: Cliente y Servidor TCP en Python

## Objetivo
Evaluar conocimientos de redes y programación en Python mediante la creación de un servidor TCP que interactúe con un cliente.

## Tiempo Estimado
⏳ **2 horas**

## Herramientas
🛠 **Python** (puedes usar cualquier librería que desees)

## Entrega
📌 Sube tu código a un repositorio de **GitHub público** y envíalo a tu contacto de **Kosmos**.

---

## Descripción
Implementar un **servidor TCP** y un **cliente TCP** en Python que puedan comunicarse entre sí en la misma máquina (**localhost**) usando el **puerto 5000**.

---

## Detalles del Ejercicio

### 1. Servidor TCP:
- 🖥 El servidor debe iniciar en **localhost** y escuchar conexiones en el **puerto 5000**.
- 🔄 Una vez que el cliente se conecte, el servidor debe esperar a recibir un mensaje del cliente.
- ❌ Si el servidor recibe el mensaje **"DESCONEXION"**, debe:
  - Cerrar la conexión con ese cliente.
  - Mantenerse disponible para recibir conexiones de nuevos clientes.
- 🔠 Para cualquier otro mensaje recibido, el servidor debe responder al cliente devolviendo el mensaje en **mayúsculas**.

### 2. Cliente TCP:
- 📡 El cliente debe conectarse al servidor en **localhost** y puerto **5000**.
- 📝 El cliente debe solicitar al usuario que **ingrese un mensaje** y luego enviarlo al servidor.
- 🔄 Tras enviar el mensaje, el cliente debe **recibir y mostrar la respuesta** del servidor en consola.
- ❌ Si el usuario ingresa **"DESCONEXION"**, el cliente debe:
  - Enviar este mensaje al servidor.
  - Cerrar la conexión y finalizar su ejecución.

---

## Requisitos de Pruebas
🛠 **Incluye dos pruebas manuales:**
1. **Enviar un mensaje de texto normal** y verificar que el servidor responda con el mensaje en mayúsculas.
2. **Enviar el mensaje "DESCONEXION"** y verificar que la conexión se cierre correctamente en ambos lados.

---

## Documentación
📖 **Incluye un archivo README.md con instrucciones claras para:**
- Ejecutar el servidor y el cliente.
- Realizar las pruebas manuales.

---

## Ejemplo de Interacción

### 📡 Conexión establecida:
```shell
Cliente envía: hola servidor
Servidor responde: HOLA SERVIDOR
```

### ❌ Desconexión:
```shell
Cliente envía: DESCONEXION
Servidor cierra la conexión con el cliente.
```

---


