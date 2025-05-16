from ai.predictor import TradeEntryAI


ai = TradeEntryAI()

# Lista de trades simulados
trades = [
    {"hora": 9,  "minuto": 55,  "direcao": "SELL", "par": "AUDCAD", "valor": 50.0},
    {"hora": 9,  "minuto": 55,  "direcao": "BUY", "par": "GBPUSD", "valor": 50.0},
    {"hora": 9,  "minuto": 56,  "direcao": "SELL", "par": "AUDCHF", "valor": 50.0},
    {"hora": 9,  "minuto": 56,  "direcao": "BUY", "par": "EURCAD", "valor": 50.0},
    {"hora": 9,  "minuto": 56,  "direcao": "SELL", "par": "EURUSD", "valor": 50.0},
    {"hora": 9,  "minuto": 56,  "direcao": "BUY", "par": "EURJPY", "valor": 50.0},
]

# Testar cada trade na IA
for trade in trades:
    result = ai.predict(
        hora=trade["hora"],
        minuto=trade["minuto"],
        direcao=trade["direcao"],
        par=trade["par"],
        valor=trade["valor"]
    )

    print("📈 Análise do Trade")
    print(f"🔸 Par de moeda:       {result.get('ativo')}")
    print(f"🔸 Horário:            {result.get('hora'):02d}:{result.get('minuto'):02d}")
    print(f"🔸 Direção:            {result.get('direcao')}")
    print(f"🔸 Valor da entrada:   R$ {result.get('valor_entrada'):.2f}")
    print(f"🔸 Chance de WIN:      {result.get('chance_de_win')}%")
    print(f"🔸 Confiança:          {result.get('nivel_de_confianca')}")
    print(f"🔸 Classificação:      {result.get('classificacao_horario')}")
    print(f"🔸 Recomendado entrar: {'✅ SIM' if result.get('recomendado') else '❌ NÃO'}")
    print(f"🔍 Análise final:      {result.get('analise')}")
    print("-" * 60)
