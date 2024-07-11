import ollama

res = ollama.chat(
    model='llava',
    messages=[
        {
            'role': 'user',
            'content': 'What do you see here?',
            'images': ['./img1.jpg']
        }
    ]
)

print(res['message']['content'])

# It will take a few minutes to complete