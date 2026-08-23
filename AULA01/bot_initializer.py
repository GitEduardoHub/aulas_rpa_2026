# bot_initializer.py

# 1. Declaração e Inicialização de Variáveis
BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 120.5
IS_PRODUCTION = False

# 2. Exibição Formatada
print("=" * 40)
print("      INICIALIZAÇÃO DO BOT RPA      ")
print("=" * 40)

print(f"Nome do Bot:        {BOT_NAME} | Tipo: {type(BOT_NAME)}")
print(f"Max Tentativas:     {MAX_RETRIES} | Tipo: {type(MAX_RETRIES)}")
print(f"Timeout (s):        {EXECUTION_TIMEOUT} | Tipo: {type(EXECUTION_TIMEOUT)}")
print(f"Ambiente Produção: {IS_PRODUCTION} | Tipo: {type(IS_PRODUCTION)}")

print("=" * 40)