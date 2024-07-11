from fastapi import FastAPI, File, UploadFile, Body
from fastapi.middleware.cors import CORSMiddleware
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/recognize/')
async def recognize(file: UploadFile = File(...), query:str = Body(...)):
    contents = await file.read()
    
    with open(file.filename, 'wb') as f:
        f.write(contents)
        
    print("Received File:", file.filename)
    res = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user',
                'content': query,
                'images': [f"{file.filename}"]
            }
        ]
    )
    
    print(res['message']['content'])
        
    return {"filename": file.filename, "query": query, "response": res['message']['content']}

# It's gonna take a bit