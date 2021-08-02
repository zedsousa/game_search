import pandas as pd
import json
from sqlalchemy import create_engine
        
df = pd.read_csv('database/games_info.csv')
engine = create_engine('postgresql://postgres:postgres@localhost:5432/games')
df.to_sql('games', engine)