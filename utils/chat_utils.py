import openai
import os
from dotenv import load_dotenv
import streamlit as st

# --- Варіант 1: Використання .env файлу для локальної розробки ---
# Завантаження змінних середовища
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key  # Встановлення API ключа напряму

# --- Варіант 2: Використання Streamlit Secrets для сервера ---
# Отримання API ключа зі Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key  # Встановлення API ключа напряму

def get_ai_response(user_input):
    # Визначення системного повідомлення
    system_prompt = """
    Ти — асистент для навчання користувача життєвим навичкам, який допомагає з інтеграцією нових знань і навичок у реальні ситуації.
    - **Сценарій 1**: Давай практичні рекомендації щодо того, як користувач може інтегрувати знання у повсякденне життя.
    - **Сценарій 2**: Проведи ретроспективу після 14-денного спринту, з аналізом результатів і рекомендаціями для подальших кроків.
    - **Сценарій 3**: Виступай у ролі "Компаньйона-співрозмовника", допомагаючи користувачу розвивати навички через діалог.
    - **Сценарій 4**: На основі результатів тесту створюй візуалізацію життя користувача через 20 років з урахуванням розвитку ключових навичок.
    При відповіді:
    - Став запитання, щоб допомогти користувачеві краще зрозуміти свої інсайти та ідеї.
    - Давай рекомендації, щоб користувач міг глибше засвоїти вивчене.
    - За необхідності використовуй діалогічний стиль, щоб користувач міг активно долучатися до обговорення.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    
    try:
        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100
        )
        return response.choices[0].message["content"]
    
    except openai.error.APIError as e:
        return "An API error occurred: {}".format(e)
    except openai.error.RateLimitError:
        return "You have exceeded your API rate limit. Please check your plan and quotas on the OpenAI Dashboard."
    except openai.error.AuthenticationError:
        return "Authentication error. Please check your API key in Streamlit secrets."
    except Exception as e:
        return f"An error occurred: {str(e)}"
