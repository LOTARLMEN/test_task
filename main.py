from fastapi import FastAPI
import uvicorn
from app.api.v1.wallets.wallets import router as wallet_router

app = FastAPI()

app.include_router(wallet_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8000)
