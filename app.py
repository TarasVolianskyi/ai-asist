import streamlit as st
import os
from dotenv import load_dotenv
from utils.chat_utils import get_ai_response
from datetime import datetime

# Завантаження змінних середовища
load_dotenv()

# Ініціалізація заголовка
st.title("AI Асистент")

# Ініціалізація історії чату
if "history" not in st.session_state:
    st.session_state.history = []

# Стилі для бульбашок повідомлень
user_style = "background-color: #DCF8C6; color: black; padding: 10px; border-radius: 8px; margin: 5px 0; text-align: right; width: fit-content; max-width: 80%;"
assistant_style = "background-color: #ECECEC; color: black; padding: 10px; border-radius: 8px; margin: 5px 0; text-align: left; width: fit-content; max-width: 80%;"

# Відображення повідомлень
for message in st.session_state.history:
    if message["role"] == "user":
        st.markdown(f"<div style='display: flex; justify-content: flex-end;'><div style='{user_style}'>{message['content']} <span style='font-size: small; color: grey;'>{message['time']}</span></div></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='display: flex; justify-content: flex-start;'><div style='{assistant_style}'>{message['content']} <span style='font-size: small; color: grey;'>{message['time']}</span></div></div>", unsafe_allow_html=True)

# Поле для вводу користувача знизу
with st.form("message_form", clear_on_submit=True):
    user_input = st.text_input("Напишіть повідомлення...", "")
    submitted = st.form_submit_button("Відправити")

# Обробка введення повідомлення
if submitted and user_input:
    current_time = datetime.now().strftime("%H:%M")
    
    # Додаємо повідомлення від користувача
    st.session_state.history.append({"role": "user", "content": user_input, "time": current_time})
    
    # Отримуємо відповідь від AI
    assistant_reply = get_ai_response(user_input)
    st.session_state.history.append({"role": "assistant", "content": assistant_reply, "time": current_time})

    # Очищення поля вводу після відправки
    st.experimental_rerun()
