from fastapi import FastAPI

# keep main.py lightweight: create app and include routers
app = FastAPI(title="Core Service")

# Import router with a fallback so the module is runnable both as a package
# (e.g. `uvicorn src.core.main:app`) and as a script when the working
# directory is `src/core` (e.g. `uvicorn main:app --app-dir src/core`).
try:
	from .controllers.user_controller import router as user_router
except Exception:
	from src.core.controllers.user_controller import router as user_router

app.include_router(user_router)
