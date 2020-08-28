import pandas as pd
import sys
from os import path

def prepend(file_path, text):
    if not path.exists(file_path):
        open(file_path,'w').close()
    with open(file_path, 'r+') as f:
        body = f.read()
        f.seek(0)
        f.write(text + body)

def main(user_id,image_id):
    df = pd.read_csv('Data/im_sim/%s.csv'%image_id)
    df = df['id']
    x = list(df)
    for i in reversed(x):
        prepend('Data/user_Recs/%s.txt'%user_id,i)
        prepend('Data/user_Recs/%s.txt'%user_id,'\n')

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
    
