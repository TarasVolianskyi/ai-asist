import openai
import os
from dotenv import load_dotenv

# Завантажуємо API ключ і ініціалізуємо клієнт
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def get_ai_response(user_input):
    # Визначаємо системне повідомлення
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
        # Викликаємо новий метод через клієнта
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100
        )
        return response.choices[0].message.content
    
    except openai.exceptions.RateLimitError:
        return "Ви перевищили ліміт використання API. Перевірте ваш план та квоти в OpenAI Dashboard."
    except openai.exceptions.AuthenticationError:
        return "Помилка автентифікації. Перевірте API ключ у файлі .env."
    except openai.exceptions.OpenAIError as e:
        return f"Інша помилка API OpenAI: {str(e)}"