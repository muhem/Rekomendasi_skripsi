import pandas as pd
from surprise import *
from movielens_private_api import Movielens, MovielensException

m = Movielens(cookie=None, timeoutSececonds=1000, api_endpoint='https://movielens.org/api/', verifySSL=True)
cookie = m.login('muhem', 'erwinskripsi')

try:
    m.getMe()
except MovielensException as e:
    msg = str(e)
    print(msg)


df = pd.read_csv('ratings.csv')
df.drop(['timestamp'], axis=1, inplace=True)

class RecommenderSystem:
    def __init__(self, data):
        self.df = pd.read_csv(data)
        self.all_movie = self.df.movieId.unique()
        self.data = None

    def fit(self):
        data = Dataset.load_from_df(self.df[['userId', 'movieId', 'rating']], Reader(rating_scale=(1, 5)))
        self.data = data.build_full_trainset()
        self.model = SVD()
        self.model.fit(self.data)

    def recommend(self, userId, top=10):
        watch_movie = self.df[df.userId == userId].movieId
        not_watch_movie = [movieId for movieId in self.all_movie if movieId not in watch_movie]
        score = [self.model.predict(userId, movieId).est for movieId in not_watch_movie]

        result = pd.DataFrame({'movieId': not_watch_movie, 'score': score})
        result.sort_values('score', ascending=False, inplace=True)
        return result.head(top)

#%%
def results(userId):
    recsys = RecommenderSystem('ratings.csv')
    recsys.fit()
    return recsys.recommend(userId)



def hasil(results):
    object_list = []

    for row in results.itertuples():
        info = m.getMovieInfo(row.movieId)

        object_list.append(info)

    return object_list




# print(results(9))
# print(hasil(results(9)))
