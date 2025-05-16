# train_model.py
from ai.trainer import TradeModelTrainer

trainer = TradeModelTrainer("ai/data/trade_sample.csv")
trainer.preprocess()
trainer.train()
trainer.save()
