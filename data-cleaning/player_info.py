import pandas as pd
import glob
from common.db import engine

all_files = glob.glob("/Users/justinjchang/Desktop/breakpoint/JS Data/*.csv")
all_players_data = []


for file_path in all_files:
    df = pd.read_csv (file_path)

    df[['tourney_date']] = pd.to_datetime(df['tourney_date'], format='%Y%m%d')

    winners = df[[
        'winner_name', 
        'winner_hand', 
        'winner_ht', 
        'winner_ioc', 
        'winner_id', 
        'tourney_date', 
        'winner_age'
    ]].rename(columns={
        'winner_name':'name', 
        'winner_hand':'hand', 
        'winner_ht':'height', 
        'winner_ioc': 'country', 
        'winner_id':'sackmann_id'})
    
    losers = df[[
        'loser_name', 
        'loser_hand', 
        'loser_ht', 
        'loser_ioc', 
        'loser_id', 
        'tourney_date', 
        'loser_age'
    ]].rename(columns={
        'loser_name':'name', 
        'loser_hand':'hand', 
        'loser_ht':'height', 
        'loser_ioc':'country', 
        'loser_id':'sackmann_id'})


    total_days_winners = winners['winner_age'] * 365
    winners['dob'] = winners['tourney_date'] - pd.to_timedelta(total_days_winners, unit='D')

    total_days_losers = losers['loser_age'] * 365 
    losers['dob'] = losers['tourney_date'] - pd.to_timedelta(total_days_losers, unit='D')

    winners = winners.drop(columns=['winner_age', 'tourney_date'])
    losers = losers.drop(columns=['loser_age', 'tourney_date'])
                     
    yearly_players=pd.concat([winners, losers])
    all_players_data.append(yearly_players)

players = pd.concat(all_players_data)
players=players.drop_duplicates(subset=['name'])
players.to_sql('players', engine, if_exists='replace', index=False)

