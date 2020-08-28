import sys
import os
import random
import pandas as pd
    
def main(user_id):
    df = pd.read_csv('Data/similarities.csv',index_col=0)

    df_index = list(df.index)
    print(type(df_index))

    x = random.sample(df_index,20)
    
    open('Data/user_Recs/%s.txt'%user_id,'w').close()
    with open('Data/user_Recs/%s.txt'%user_id,'a') as f:
        for i in x:
            f.write('\n')
            f.write(i)
            

if __name__ == "__main__":
    main('U0124')
