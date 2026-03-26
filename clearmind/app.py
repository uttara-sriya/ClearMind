from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from clearmind.agent import process_text_with_agent

# Initialize the FastAPI web server
app = FastAPI(title="ClearMind ADK API")

# Define what the incoming HTTP request should look like
class RequestBody(BaseModel):
    text: str = Field(..., description="The complex text to be simplified")

# Define what the HTTP response should look like
class ResponseBody(BaseModel):
    simplified_response: str

@app.post("/simplify", response_model=ResponseBody)
def simplify_endpoint(request: RequestBody):
    """
    HTTP POST endpoint that receives text and passes it to the ADK Agent.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
        
    # Send the text to our agent
    agent_output = process_text_with_agent(request.text)
    
    # Return the agent's output as a JSON response
    return ResponseBody(simplified_response=agent_output)