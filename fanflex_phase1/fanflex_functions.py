import matplotlib.pyplot as plt
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

pd.set_option("display.max_columns",100)

show_col = ['show_id','name', 'age', 'gender', 'tickets_bought']
att = np.random.randint(1, 31)
venue_name = ['Ball Arena','Summit Music Hall','Marquis Theater','Dazzle',
                                    "Ophelia's Electric Soapbox","Herb's","Black Buzzard","Paramont Theatre",
                                    "Roxy Theatre","Cervantes & The Other Side","Mission Ballroom","Larimer Lounge",
                                    "Globe Hall","Ogden Theatre","Lost Lake","Walnut Room","Globe Hall","Your Mom's House",
                                    "Herman's Hideway","Broadway Roxy"]


def buyer_show(show_num):

    ''' 
        creates buyer profile to be added to panda dataframe
        show_num = show number
    '''
''' 
        creates buyer profile to be added to panda dataframe
        show_num = show number
    '''
    show_id = show_num
    name = np.random.choice(['Kirsty Millington', 'Donald McSherry', 'Charlotte Worth', 'Andre Botelho', 
                            'Keanu Reeves', 'John Travolta', 'Danzel Washington', 'Marlon Brandon', 
                            'Reese Witherspoon', 'Maryl Strip', 'Mari Nishida', 'Dustin Hoffman', 
                            'Bruce Wayne','Tony Stark', 'Peter Parker', 'Scarlett Johanssen', 
                            'Cristina Abdalla','Ronda Rousey','Joel Miller', 'Kalum Rooney',
                            'Luna Timms', 'Margaux Wolfe','Nazifa Jimenez','Wasim Gaines','Oliver Case',
                            'Aizah North','Harry Goodwin','Kerys Peralta', 'Bear Williamson',
                            'Dani Cunningham', 'Jayda Hutchings','Kobie Sears','Julie Wallace',
                            'Garry Mclellan','Virgil Gibbs','Alan Marquez','Fraser Barron'], replace=False)

    age = np.random.randint(18, 50)
    gender = np.random.choice(['M','F','NB','T'])
    num_bought = np.random.randint(1,5)
    ticket_bought = np.random.randint(1,5)


    buyer_profile = [show_num, name,age,gender, ticket_bought]

    return buyer_profile

def generate_df(num, show_num, v):
    '''
    num (int) = total attendees sold
    v (str) = venue name
    '''
    show_data = []
    
    for i in range(num):
        show_data.append(buyer_show(show_num))

    show_df = pd.DataFrame(data = show_data, columns = show_col)

    show_df['ticket_price']=np.random.choice(np.array([5,10,15,20]))
    show_df['total_revenue']= show_df['ticket_price']*show_df['ticket_bought']
    show_df['venue_name'] = v

    return show_df

def concat_shows(original_df, to_concat_df):
    show_df = pd.concat((original_df, to_concat_df), axis=0)
    show_df.reset_index(inplace=True, drop=True)
    return show_df