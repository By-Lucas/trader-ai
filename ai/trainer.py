import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ai.config import MODEL_DIR, MODEL_PATH, ENCODER_ORDER_TYPE, ENCODER_ASSET_ORDER


class TradeModelTrainer:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)
        self.model = None
        self.encoders = {}

    def preprocess(self):
        df = self.df.dropna(subset=["order_type", "order_result_status", "amount", "open_time", "asset_order"])
        df = df[df["order_result_status"].isin(["WIN", "LOSS"])]

        df["amount"] = df["amount"].str.replace(",", ".", regex=False).astype(float)
        df["open_time"] = pd.to_datetime(df["open_time"])
        df["hour"] = df["open_time"].dt.hour
        df["minute"] = df["open_time"].dt.minute
        df["target"] = df["order_result_status"].map({"WIN": 1, "LOSS": 0})

        order_type_encoder = LabelEncoder()
        asset_order_encoder = LabelEncoder()
        df["order_type_enc"] = order_type_encoder.fit_transform(df["order_type"])
        df["asset_order_enc"] = asset_order_encoder.fit_transform(df["asset_order"])

        self.encoders["order_type"] = order_type_encoder
        self.encoders["asset_order"] = asset_order_encoder
        self.df = df


    def train(self):
        X = self.df[["hour", "minute", "order_type_enc", "asset_order_enc", "amount"]]
        y = self.df["target"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def save(self):
        MODEL_DIR.mkdir(exist_ok=True, parents=True)
        joblib.dump(self.model, MODEL_PATH)
        joblib.dump(self.encoders["order_type"], ENCODER_ORDER_TYPE)
        joblib.dump(self.encoders["asset_order"], ENCODER_ASSET_ORDER)
