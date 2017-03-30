import numpy as np
import pandas as pd

from dateutil.parser import parse

N_SP = 16

columns = [
    'name',
    'age',
    'sex',
    'born',
    'lived',
    'lived_longest',
    'home_country',
    'education',
] + sum(
    [[f'similar_{n}', f'country_{n}', f'standard_{n}'] for n in range(16)], []
) + [
    'stood_out',
    'overall_sim',
    'overall_diff']


american_ixes = [1, 2, 4, 5, 7, 8, 9, 14]
canadian_ixes = [0, 3, 6, 10, 11, 12, 13, 15]

country_am = [f'country_{i}' for i in american_ixes]
similar_am = [f'similar_{i}' for i in american_ixes]
standard_am = [f'standard_{i}' for i in american_ixes]
country_ca = [f'country_{i}' for i in canadian_ixes]
similar_ca = [f'similar_{i}' for i in canadian_ixes]
standard_ca = [f'standard_{i}' for i in canadian_ixes]

df = pd.read_csv('data.csv').iloc[:, 1:]
df.columns = columns

americans = df['home_country'] == 'United States'
print('can(resp)-can similarity: ', df.loc[~americans, country_ca].median().median())
print('can(resp)-am similarity: ', df.loc[~americans, country_am].median().median())
print('am(resp)-can similarity: ', df.loc[americans, country_ca].median().median())
print('am(resp)-am similarity: ', df.loc[americans, country_am].median().median())

#Can/ Am English is different?
print('can(resp) AE CE different:' , df.loc[~americans, f'overall_sim'].mean().mean())
print('am(resp) AE CE different: ', df.loc[americans, f'overall_sim'].mean().mean())
print('all resp: CE, AE different', df.loc[:, f'overall_sim'].mean().mean())
