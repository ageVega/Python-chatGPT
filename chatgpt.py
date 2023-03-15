import openai 

openai.api_key = ""

while True:

    prompt = input("\n- Introduce una pregunta:\n")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="code-cushman-001",
                                        prompt=prompt,
                                        max_tokens=4000)

    print(completion.choices[0].text)
