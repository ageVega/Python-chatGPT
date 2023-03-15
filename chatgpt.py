import openai 
from dotenv import load_dotenv
from os import environ

load_dotenv()
openai.api_key = environ.get('OPENAI_API_KEY')

Engine = "text-davinci-003"
Max_tokens = 4000

while True:

    prompt = input("\n- Introduce una pregunta:\n")
    
    while prompt == "":
        print("No has introducido ninguna pregunta. Por favor, inténtalo de nuevo.")
        prompt = input("\n- Introduce una pregunta:\n")

    if prompt == "exit":
        break    


    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'user', 'content': prompt}
        ],
        temperature = 0
        )

    print(completion['choices'][0]['message']['content'])
