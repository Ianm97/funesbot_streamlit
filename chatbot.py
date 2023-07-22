import streamlit as st
from PIL import Image
from streamlit_chat import message
import requests
import os
import random
import base64
#from st.session_state import

def generate_response(input_text):
    url='http://127.0.0.1:8000/predict'

    params= {'user_query':input_text
         }
    response=requests.get(url=url,params=params).json()

    return response['answer_query']
#['Respuesta']
#['content']

def main():
    # Configuración de la página
    st.set_page_config(page_title="FunesBot Project", page_icon=":speech_balloon:")

    #Imagen de fondo
    image = Image.open("imagenfondo1.jpg")
    st.image(image, use_column_width=True)

    # Título y texto de bienvenida
    st.title("FunesBot: First Model")
    st.write("Welcome! This is a chatbot created by our team for the Data Science Batch 1203 Le Wagon, Buenos Aires. It can answer your questions about War and Peace by Tolstoy. Please enter your questions in the text field below.")
    ran_gif = random.randint(1,5)

    if ran_gif == 1:
        st.image(
        "https://i.gifer.com/Ao.gif",
        width=400,
    )

    if ran_gif == 2:
        st.image(
            "https://i.gifer.com/48Z.gif",
            width = 400,

        )


    if ran_gif == 3:
        st.image(
            "https://i.gifer.com/2GU.gif",
                    width = 400,

        )




    if ran_gif == 4:
        st.image(
            "https://i.gifer.com/Aw.gif",
                                width = 400,

        )


    if ran_gif == 5:
        st.image(
            "https://i.gifer.com/A7PB.gif",
                                width = 400,

        )

    # Lista para almacenar el historial de preguntas y respuestas
    if 'message' not in st.session_state:
        st.session_state['message'] = []

    messages = st.session_state['message']

    placeholder = st.empty()
    # Área de texto para que el usuario ingrese la pregunta
    user_input = st.text_input("Enter your question here:")
    button = st.button("Send")

    # Verificar si se presiona la tecla Enter en el teclado
    if user_input and (button or st.session_state.enter_pressed):
        # Generar respuesta
        response = generate_response(user_input)

        # Agregar la pregunta y respuesta al historial
        messages.append((user_input, response))

        # Restablecer el valor de enter_pressed
        st.session_state.enter_pressed = False

    # Mostrar el historial de preguntas y respuestas
    #container = st.container()
    with placeholder.container():
        for i, (question, answer) in enumerate(messages, 1):
                message(question, True, key=str(i*2))
                #st.write(f"**Question {i}:** {question}")
                message(answer, False, key=str(i*2+1))
                #st.write(f"**Answer {i}:** {answer}")

    if st.button('Restart Chat'):
      st.session_state['message'] = []
      placeholder.empty()

    # Mostrar la respuesta más reciente
    if len(messages) > 0:
        st.subheader("Respuesta más reciente:")
        st.text(messages[-1][1])

#Musica autoreproducción en sidebar
    def autoplay_audio(file_path: str):
         with open(file_path, "rb") as f:
             data = f.read()
             b64 = base64.b64encode(data).decode()
             md = f"""
                 <audio controls autoplay="true">
                 <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                 </audio>
                 """
             st.markdown(
                 md,
                 unsafe_allow_html=True,
             )
    st.write("Ambiental Music!")
    autoplay_audio("music.mp3")

#Define imagen de fondo principal
def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
             encoded_string = base64.b64encode(image_file.read())
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
         )
        add_bg_from_local('duotone.png')
if __name__ == "__main__":
    main()
