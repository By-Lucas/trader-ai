# 📊 IA para Previsão de Pontos de Entrada no Trading

Este projeto usa Machine Learning para prever se um trade tem alta chance de sucesso (WIN), com base em dados históricos de operações. A IA analisa hora, minuto, par de moeda, valor e direção (BUY/SELL), classificando o horário e retornando se é recomendável operar naquele momento.

Desenvolvido para testes e treinamentos, mas com uma boa base de dados, você poderá obter bons resultados, ou até mesmo reutilizar o modelo para outros métodos.

---

## 🚀 Funcionalidades

- Previsão de chance de WIN (em %)
- Classificação do horário (ótimo, mediano, instável)
- Recomendação automática (✅ entrar ou ❌ evitar)
- Suporte a múltiplos pares de moedas
- Retorno completo com análise detalhada

---

## ⚙️ Instalação

```bash
# Clonar o repositório
git clone https://github.com/By-Lucas/trader-ia.git
cd trader-ia

# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto
```bash
TraderIA/
│
├── ai/
│   ├── predictor.py          # Classe de predição
│   ├── trainer.py            # Classe de treinamento do modelo
│   ├── config.py             # Caminhos e diretórios
│   ├── data/                 # Caminho da pasta onde deve conter o csv para treinar
│
├── train_model.py            # Script para treinar o modelo
├── use_model.py              # Exemplo de uso com múltiplos trades
├── model_storage/            # Onde os modelos .pkl são salvos
│
└── requirements.txt
```

## 📊 Como Treinar a IA

- Certifique-se de ter um arquivo CSV com as colunas: open_time, order_type, order_result_status, amount, asset_order.

```bash
python train_model.py
```
- O modelo será treinado com base nos dados e salvo em model_storage/.

## 🤖 Como Usar a IA

- Você pode simular múltiplos trades e obter previsões assim:

```bash
from ai.predictor import TradeEntryAI

ai = TradeEntryAI()

res = ai.predict(hora=14, minuto=53, direcao="SELL", par="EURUSD_otc", valor=50.0)
print(res)
```

## 🔁 Exemplo de saída:
```bash

{
  "ativo": "EURUSD_otc",
  "hora": 14,
  "minuto": 53,
  "direcao": "SELL",
  "valor_entrada": 50.0,
  "chance_de_win": 76.4,
  "recomendado": true,
  "classificacao_horario": "Horário ótimo",
  "nivel_de_confianca": "Boa confiança",
  "analise": "O par EURUSD_otc às 14:53 tem 76.4% de chance de sucesso com a direção SELL."
}
```
