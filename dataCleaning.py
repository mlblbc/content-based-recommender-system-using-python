def main():
    import pandas as pd
    import numpy as np

    df = pd.read_csv("Data/data.csv",sep=';',index_col=0)

    df['Artist'] = df['Artist'].map(lambda x:x.lower().replace(" ","_"))

    df['Style'] = df['Style'].map(lambda x:x.lower().replace(" ","_"))

    df['Subject'] = df['Subject'].map(lambda x:x.lower().replace(" ","_"))

    df.to_csv('Data/data_cleaned.csv')

if __name__ == "__main__":
    main()