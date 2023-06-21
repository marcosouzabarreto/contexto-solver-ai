from main import word_vectors
import pandas as pd
from contexto_game import ContextoGame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump


# Salva o modelo para um arquivo



print("started")
contexto = ContextoGame()

print("initialized game")
distances = {word: contexto.guess(word) for word in word_vectors.index_to_key}
print("Got Distances")
data = pd.DataFrame.from_dict(distances, orient='index', columns=['distance'])
print("Created Data for training")

X = [word_vectors[word] for word in data.index]
y = data['distance'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Model training init")
model = RandomForestRegressor(n_estimators=100, random_state=42)
print("finished training model")
model.fit(X_train, y_train)
dump(model, 'trained_contexto_model.joblib')

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f"MSE: {mse}")
