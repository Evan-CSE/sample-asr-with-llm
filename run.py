import uvicorn
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("GOOGLE_API_KEY"))
    uvicorn.run("src.app.main:app", host="localhost", port=8080, reload=True)