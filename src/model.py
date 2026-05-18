from catboost import CatBoostClassifier

def train_model(X_train, y_train):
    model = CatBoostClassifier(
        iterations=500,
        depth=8,
        learning_rate=0.05,
        loss_function="Logloss",
        verbose=False
    )

    model.fit(X_train, y_train)
    return model


def predict_ko(model, X, threshold=0.5):
    proba = model.predict_proba(X)[:, 1]
    return (proba > threshold).astype(int), proba