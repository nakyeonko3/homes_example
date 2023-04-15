import joblib

load_model = joblib.load("df_clf.pkl")
pred = load_model.predict([[6.8, 3.0, 5.5, 2.1]])
result = pred
print(result)
