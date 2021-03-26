import matplotlib.pyplot as plt
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from fanflex_functions import *

pd.set_option("display.max_columns",100)

#artist database

shows_played = 0
num_venues = 0
avg_revenue = 0 
total_revenue = 0 
avg_ticket_price = 0 
tickets_sold = 0

artist = np.array([[shows_played,num_venues,avg_revenue,total_revenue,avg_ticket_price,tickets_sold]])

artist_df = pd.DataFrame(   data = artist, 
                            columns = ['shows_played','num_venues','avg_revenue','total_revenue',
                                        'avg_ticket_price','tickets_sold'])



'''
Generating individual show's data
'''
show1 = generate_df(att,1, np.random.choice(venue_name))
show2 = generate_df(att,2, np.random.choice(venue_name))
show3 = generate_df(att,3, np.random.choice(venue_name))
show4 = generate_df(att,4, np.random.choice(venue_name))
show5 = generate_df(att,5, np.random.choice(venue_name))


'''
Generating Master Show DataFrame
'''
show_df = concat_shows(show1, show2)
show_df = concat_shows(show_df, show3)
show_df = concat_shows(show_df, show4)
show_df = concat_shows(show_df, show5)


    
