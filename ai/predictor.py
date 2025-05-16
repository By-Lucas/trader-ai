import joblib
import pandas as pd

from ai.config import MODEL_PATH, ENCODER_ORDER_TYPE, ENCODER_ASSET_ORDER


class TradeEntryAI:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.enc_order = joblib.load(ENCODER_ORDER_TYPE)
        self.enc_asset = joblib.load(ENCODER_ASSET_ORDER)
    
    def classify_horario(self, probabilidade: float) -> str:
        if probabilidade >= 0.70:
            return "Horário ótimo"
        elif probabilidade >= 0.50:
            return "Horário mediano"
        else:
            return "Horário instável"
    
    def get_confianca_label(self, prob: float) -> str:
        if prob >= 0.85:
            return "Alta confiança"
        elif prob >= 0.70:
            return "Boa confiança"
        elif prob >= 0.50:
            return "Confiança moderada"
        else:
            return "Confiança baixa"

    def predict(self, hora: int, minuto: int, direcao: str, par: str, valor: float) -> dict:
        try:
            order_type_enc = self.enc_order.transform([direcao])[0]
            asset_order_enc = self.enc_asset.transform([par])[0]
        except ValueError:
            return {"erro": "Par de moeda ou direção desconhecida. Treine o modelo com mais dados."}
        
        input_data = pd.DataFrame([{
            "hour": hora,
            "minute": minuto,
            "order_type_enc": order_type_enc,
            "asset_order_enc": asset_order_enc,
            "amount": valor
        }])

        prob = self.model.predict_proba(input_data)[0][1]

        return {
            "ativo": par,
            "direcao": direcao,
            "hora": hora,
            "minuto": minuto,
            "valor_entrada": valor,
            "chance_de_win": round(prob * 100, 2),
            "recomendado": prob > 0.70,
            "classificacao_horario": self.classify_horario(prob),
            "nivel_de_confianca": self.get_confianca_label(prob),
            "analise": f"O par {par} às {hora:02d}:{minuto:02d} tem {round(prob * 100, 2)}% de chance de sucesso com a direção {direcao}."
        }
