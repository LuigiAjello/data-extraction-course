import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin

class ConversorTemporal(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_modificado = X.copy()
        X_modificado['Data_Transacao'] = pd.to_datetime(X_modificado['Data_Transacao'])
        X_modificado['Is_Weekend'] = (X_modificado['Data_Transacao'].dt.dayofweek >= 5).astype(int)
        X_modificado = X_modificado.drop('Data_Transacao', axis=1)
        return X_modificado
