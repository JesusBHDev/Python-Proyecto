# 🛒 Sistema de Recomendación de Productos – Proyecto de Aprendizaje Automático

**Sistema de Recomendación de Productos** es una aplicación que utiliza un modelo de **reglas de asociación** desarrollado en **Python** para recomendar productos basados en el comportamiento de compra de los usuarios. El modelo se encuentra alojado en **Render** y se comunica con una **API RESTful** desarrollada en **Node.js** para realizar recomendaciones en tiempo real.

---

## 🚀 Características

- 🤖 Implementación de un **modelo de reglas de asociación**
- 🌐 Consultas en tiempo real a la **API Node.js** para obtener recomendaciones.
- 🧑‍💻 Desarrollado en **Python** utilizando bibliotecas de aprendizaje automático.
- 📦 Utiliza un **backend Node.js** para manejar las solicitudes y entregar las recomendaciones.
- 📈 El modelo fue entrenado utilizando datos reales de compras.

---

## 🛠️ Tecnologías utilizadas

| Tecnología     | Descripción                                         |
|----------------|-----------------------------------------------------|
| Python         | Lenguaje principal para la creación del modelo      |
| pandas         | Biblioteca para manipulación de datos               |
| apriori        | Algoritmo de reglas de asociación                   |
| Node.js        | Backend de la API RESTful                           |
| Express.js     | Framework para construir la API                    |
| Render         | Plataforma de despliegue del modelo de Python       |

---

## 🧑‍💻 Flujo del proyecto

1. **Entrenamiento del modelo:**  
   El modelo de reglas de asociación se entrenó con datos de compras, utilizando el algoritmo **Apriori** para descubrir asociaciones entre productos.

2. **Despliegue del modelo en Render:**  
   El modelo entrenado se subió a **Render** y está disponible a través de una API que permite obtener recomendaciones de productos.

3. **Consumo de la API:**  
   La **API de Node.js** consulta el modelo en **Render** para obtener las recomendaciones, las cuales son devueltas y presentadas al usuario en la interfaz.

4. **Recomendación de productos:**  
   El sistema recomienda productos en base a las reglas descubiertas, mejorando la experiencia de compra.
