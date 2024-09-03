import pandas as pd
import ast

credit = pd.read_csv("tmdb_5000_credits.csv", header=0)

print(credit.head())

df_selected = credit[['title', 'cast']]

print(df_selected.head())

def get_actors(cast_str):
    try:
        cast_list = ast.literal_eval(cast_str)
        return ', '.join([actor['name'] for actor in cast_list])
    except:
        return 'No cast information'

df_selected['actors'] = df_selected['cast'].apply(get_actors)

for index, row in df_selected.head(10).iterrows():
    print(f"{row['title']} | {row['actors']}")

df_selected.to_csv('selected_movies_cast.csv', index=False)
