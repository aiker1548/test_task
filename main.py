import logging
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/app/logs/app.log"),  
        logging.StreamHandler()  
    ]
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=PlainTextResponse)
async def home(name: str = "Recruto", message: str = "Давай дружить"):
    response = f"Hello {name}! {message}!"
    logging.info(f"Request: name={name}, message={message} -> Response: {response}")
    return response
