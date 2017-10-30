import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 200)
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter, defaultdict
import numpy as np
from analysis_functions_similarity import *
import graphlab
from graphlab.toolkits.cross_validation import cross_val_score, KFold


import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_csv('/Users/brendanwong/galvanize/Capstone/crunchbase-data/investments.csv')
df = df_preprocessing(df)
df.head()
mask_d = (~df['funded_year_month'].isin(['2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12']))
observation_data = df[mask_d]
# observation_data = observation_data[(observation_data['funding_round_type'] == 'venture')]
holdout_data = df[(df['funded_year_month'].isin(['2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12']))]
holdout_data[['company_name', 'investor_name']]
holdout_data = holdout_data[(holdout_data['funding_round_type'] == 'venture')]
train = observation_data[['company_name', 'investor_name']]
test = holdout_data[['company_name', 'investor_name']]
train.to_csv('/Users/brendanwong/galvanize/interaction_data/interaction_data_final.csv')
test.to_csv('/Users/brendanwong/galvanize/interaction_data/test_data_final.csv')
sf = graphlab.SFrame.read_csv('/Users/brendanwong/galvanize/interaction_data/interaction_data_final.csv')
sf_test = graphlab.SFrame.read_csv('/Users/brendanwong/galvanize/interaction_data/test_data_final.csv')
m2 = graphlab.recommender.item_similarity_recommender.create(observation_data=sf, user_id = 'company_name', item_id = 'investor_name')
eval_2 = m2.evaluate(sf_test, cutoffs=[30])
eval_2
m2.get_current_options()

m2.recommend_from_interactions(['Beyond Meat'], k=30)
m2.recommend_from_interactions(['Yozio'], k=20).print_rows(20)
observation_data[(observation_data['investor_name'] == 'Obvious Ventures')]
observation_data[(observation_data['company_name'] == 'Beijing Weiying Technology')]

m2.recommend(['AppDynamics'])

len(holdout_data)
holdout_data.head()
holdout_data[['company_name', 'funding_round_type']].groupby(['company_name', 'funding_round_type']).count()
holdout_data[(holdout_data['company_name'] == 'CircleUp')]
observation_data[(observation_data['company_name'] == 'CircleUp')]
