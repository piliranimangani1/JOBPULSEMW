# app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
# from app.database import engine
from app.routers.auth import router as auth_router
from app.routers.main import router as main_router

app = FastAPI(title="Heartbeat Coders E-Recruitment")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
# Base.metadata.create_all(bind=engine)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(main_router, tags=["main"])

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})