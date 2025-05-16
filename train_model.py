# train_model.py
from ai.trainer import TradeModelTrainer

trainer = TradeModelTrainer("ai/data/TradeOrder-2025-05-15.csv")
trainer.preprocess()
trainer.train()
trainer.save()
