import pickle

with open('C:/Users/ASUS Vivobook/Desktop/Mission_ACA/Stock_Price_Prediction_System/models/brent_crude_price_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
print(loaded_model)
print(loaded_model.feature_names_)