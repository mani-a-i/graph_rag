from fastapi import APIRouter
from settings import get_settings
from schemas.schema import llmInferenceRequest,llmInferenceResponse
import google.generativeai as genai


def llm_routers():

    env_var = get_settings()
    router = APIRouter()

    @router.post("/llmInference",
                 tags=['llm_inference'],
                 summary="Hit this router for Inference")
    async def llmInference(
        payload: llmInferenceRequest
    ):
        genai.configure(api_key=env_var.GOOGLE_API_KEY)
        
        model = genai.GenerativeModel(payload.model)
        response = model.generate_content( contents=payload.user_input,
                                        generation_config=genai.types.GenerationConfig(                                 
                                        max_output_tokens=payload.max_output_tokens,
                                        temperature=payload.temperature,
                                                                          ),
                                    )
        return llmInferenceResponse(
            response={
                "Answer":response.text
            }
        )
    
    return router

main_router = llm_routers()
        





