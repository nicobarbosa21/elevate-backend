from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main_api.routers import employee_routers, seniority_routers, nationality_routers, job_routers
from jokes_api import jokes_routers
from harry_potter_api import hp_routers

app = FastAPI(title="Elevate Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_routers.router)
app.include_router(seniority_routers.router)
app.include_router(nationality_routers.router)
app.include_router(job_routers.router)
app.include_router(jokes_routers.router)
app.include_router(hp_routers.router)
