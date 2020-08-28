def main():
    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    df = pd.read_csv('Data/data_cleaned.csv',index_col=0)
    #df_ratings = pd.read_csv('Data/ratings.csv')

    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
                words = words + ''.join(row[col])+ ','
        row['bag_of_words'] = words
        
    df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)

    #tfidf = TfidfVectorizer()
    countvector = CountVectorizer()

    #tfidf_matrix = tfidf.fit_transform(df['bag_of_words'])
    cv_matrix = countvector.fit_transform(df['bag_of_words'])

    cos_sim = cosine_similarity(cv_matrix)

    df_cos_sim = pd.DataFrame(cos_sim,columns = df.index,index = df.index)

    df_cos_sim.to_csv('Data/similarities.csv')

    for i in range(len(df_cos_sim)):
        x = df_cos_sim.iloc[i].sort_values(axis=0,ascending=False)[1:11]
        x.to_csv('Data/im_sim/%s.csv'%x.name)
        
if __name__ == "__main__":
    main()