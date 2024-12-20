import streamlit as st
import openai

# Configura tu clave de API de OpenAI
openai.api_key = "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"

# Título de la aplicación
st.title("Analizador de Resultados Empresariales con Optimización SEO")

# Inputs del usuario
nombre_empresa = st.text_input("Nombre de la empresa")
contexto_empresa = st.text_area("Contexto de la empresa")
impresiones = st.number_input("Impresiones", min_value=0, step=1)
clicks = st.number_input("Clicks", min_value=0, step=1)
acciones = st.text_input("Acciones (separadas por coma)")

# Botón para generar resultado
if st.button("Obtener Resultado"):
    if nombre_empresa and contexto_empresa:
        # Llamada a la API de OpenAI
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Teniendo en cuenta esta información {contexto_empresa}, nombre de la empresa {nombre_empresa} "
                            f"Ten en cuenta {impresiones}, {clicks}, {acciones}"
                            f"Generame un reporte semanal SEO para enviarselo al cliente por correo, que tenga un formato legible y que lo puedan entender facilmente"
                        ),
                    }
                ],
            )
            description = completion.choices[0].message.content

            # Mostrar el resultado en la app
            st.success(f"La empresa {nombre_empresa}, tuvo {clicks} clicks y {impresiones} impresiones, y se realizaron estas acciones: {acciones}.")
            st.subheader("Encabezado SEO sugerido:")
            st.write(description)

        except Exception as e:
            st.error(f"Error al procesar la solicitud: {e}")
    else:
        st.error("Por favor, completa todos los campos requeridos.")
