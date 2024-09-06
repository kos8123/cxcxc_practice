from fastapi import FastAPI
from controller import router
import uvicorn
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})



app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)