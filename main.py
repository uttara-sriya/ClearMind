import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables (like your GOOGLE_API_KEY)
load_dotenv()

if __name__ == "__main__":
    # Ensure the API key is set before starting
    if not os.getenv("GOOGLE_API_KEY"):
        print("WARNING: GOOGLE_API_KEY environment variable is not set!")
        print("Please set it in your terminal or a .env file.")
    
    print("Starting ClearMind API Server...")
    # Run the FastAPI app located in clearmind/app.py
    uvicorn.run("clearmind.app:app", host="0.0.0.0", port=8080, reload=True)