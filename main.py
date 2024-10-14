from fastapi import FastAPI
from settings import get_settings
import google.generativeai as genai
import os
from routers.llm_inference import main_router


def get_app():  

    api = FastAPI(
        title='graph-rag',
        summary='poc for graph rag',
        openapi_tags=[
          {  
              'name':'llm_inference'
          }
        ]
        )
    
    
    api.include_router(main_router)
    
    return api
    

api = get_app()



