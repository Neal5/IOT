from scripts.typer.typer_endpoints import app
import uvicorn
from scripts.api.servicers.services import user
if __name__ == "__main__":
    app()
    # uvicorn.run("main:user", host="127.0.0.1", port=8001, reload=True)

