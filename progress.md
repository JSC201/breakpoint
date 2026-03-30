Project BreakPoint 
Objective: DL and organize tennis data, create ELO ranking system, use ML & ELO system to predict Roland Garros Bracket 2026 
Phase 1: Data
1. Ingest tennis up to most recent tennis data Miami Open 2026 
- find sources for data most recent tennis matches 2025/2026 
- create ingestion pipeline 
    - 2026 Clay season tournaments:
        - March 30 - April 5 [Houston/Marrakech/Bucharest] ATP 250 
        - April 5 - April 12 [Rolex Monte Carlos Masters] ATP 1000
        - April 13 - April 19 [Barcelona Open/BMR Open] ATP 500
        - April 22 - May 3 [Mutua Madrid Open] ATP 1000
        - May 6 - May 17 [Internazionali BNL d'Italia] ATP 1000
        - May 17 - May 23 [Hamburg Open] ATP 500
        - May 17 - May 23 [Geneva Open] ATP 250 
        - May 24 - June 7 [Roland-Garros] Grand Slam 

2. create clean data table
    - player info
        - player_id 
        - sackmann_id
        - name 
        - handedness
        - height
        - country 
        - DOB
    - match stats 
        - match id
        - round
        - best_of 
        - date 
        - surface 
        - break points saved/facd
        - serve stats 
        - groundstrokes stats (if possible)
        - player_1_id
        - player_2_id
        - player_1_rank
        - player_2_rank
        - score
        - match duration 
        - winner_id 
        - loser_id
    - tournmanet_metadata
        - tournament_id 
        - tournament_name 
        - level 
        - surface
        - location 
