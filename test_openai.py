import os
from openai import OpenAI
from dotenv import load_dotenv
# Завантажуємо змінні середовища
load_dotenv()
# Ініціалізуємо клієнт
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
try:
    # Створюємо запит на завершення чату
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ти – асистент, який говорить українською."},
            {"role": "user", "content": "Привіт"}
        ],
        max_tokens=50
    )
    
    # Виводимо результат
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Помилка: {e}")