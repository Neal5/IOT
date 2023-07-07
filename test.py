from scripts.fastapi.DB.database import engine
import pandas as pd
a=pd.read_sql('SELECT * FROM public."Data"',con=engine)
print(a)