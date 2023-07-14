from scripts.typer.typer_endpoints import TyperEndpoints,app
import asyncio
import logging
from scripts.Device.data_generator.Data_Genrator import GenerateData
import uvicorn
from scripts.api.servicers.services import user
# async def main():
#     try:
#         async with asyncio.TaskGroup() as tg:
#             task1=tg.create_task(GenerateData.simulate_data_a())
#             task2 = tg.create_task(GenerateData.simulate_data_b())
#     except Exception as e:
#         logging.exception(e)

# if __name__ == "__main__":
#     asyncio.run(main())

if __name__ == "__main__":
    app()
    # uvicorn.run("main:user", host="127.0.0.1", port=8001, reload=True)
