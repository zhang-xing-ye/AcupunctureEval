from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from router import vqaRouter

# 配置FastAPI
app = FastAPI(
    title="AcupunctureEval API",
    version="1.0",
    description="AcupunctureEval API",
)
# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
# 重定位到docs
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

app.include_router(vqaRouter.router)


