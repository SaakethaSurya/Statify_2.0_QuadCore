from transformers import pipeline
from tool import get_stock_price, get_company_news
from dotenv import load_dotenv

load_dotenv()

chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

print("Financial Analyst Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if "stock" in user_input.lower():
        company = input("Enter stock ticker (Example: AAPL): ")
        print(get_stock_price(company))

    elif "news" in user_input.lower():
        company = input("Enter company name: ")
        print(get_company_news(company))

    else:
        response = chatbot(
            user_input,
            max_length=50,
            num_return_sequences=1
        )

        print("Bot:", response[0]["generated_text"])