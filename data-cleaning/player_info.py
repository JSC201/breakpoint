import pandas as pd
from sqlalchemy import create_engine
import glob

engine=create_engine('postgresql://justinjchang@localhost:5432/breakpoint-ml')
all_files = glob.glob("/Users/justinjchang/Desktop/Tennis ML/JS Data/*.csv")
all_players_data = []


for file_path in all_files:
    df = pd.read_csv (file_path)

    winners = df[['winner_name', 'winner_hand']].rename(columns={'winner_name':'name', 'winner_hand':'hand'})
    losers = df[['loser_name', 'loser_hand']].rename(columns={'loser_name':'name', 'loser_hand':'hand'})

    yearly_players=pd.concat([winners, losers])
    all_players_data.append(yearly_players)

players = pd.concat(all_players_data)
players=players.drop_duplicates(subset=['name'])
players.to_sql('players', engine, if_exists='replace', index=False)
