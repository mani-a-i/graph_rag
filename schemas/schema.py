from pydantic import BaseModel,Field
from typing import Optional,Dict

class llmInferenceRequest(BaseModel):
    user_input:str
    model: Optional[str] = "gemini-1.5-flash"
    temperature: Optional[float] =  0.1
    max_output_tokens: Optional[int] = 500

class llmInferenceResponse(BaseModel):
    response:Dict
