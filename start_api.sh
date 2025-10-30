#!/bin/bash
# =========================================
# Inicia a API FastAPI e cria túnel ngrok
# =========================================

API_PORT=8000
PROJECT_DIR="/home/dsm/Documents/arduino-uno"
LOGFILE="$PROJECT_DIR/api.log"

# Vai para a pasta do projeto
cd "$PROJECT_DIR" || exit 1

echo "🚀 Iniciando API FastAPI na porta $API_PORT..."
# Inicia FastAPI em background
uvicorn main_api:app --host 0.0.0.0 --port $API_PORT > "$LOGFILE" 2>&1 &

# Guarda o PID do processo (para encerrar depois, se quiser)
API_PID=$!

# Aguarda API iniciar
sleep 3

echo "🌍 Iniciando túnel ngrok..."
# Inicia o túnel (em background)
ngrok http $API_PORT > "$LOGFILE.ngrok" 2>&1 &

# Aguarda ngrok subir e buscar a URL pública
sleep 5

# Extrai o link público do ngrok
PUBLIC_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[a-zA-Z0-9./-]*ngrok-free.dev' | head -n 1)

if [ -z "$PUBLIC_URL" ]; then
  echo "❌ Não foi possível obter o link público do ngrok."
else
  echo "✅ API está online!"
  echo "📡 Link público: $PUBLIC_URL"
  echo "🧩 Endpoints disponíveis:"
  echo "   🔹 $PUBLIC_URL/"
  echo "   🔹 $PUBLIC_URL/dados"
  echo "   🔹 $PUBLIC_URL/dados/csv"
fi

echo ""
echo "🛑 Para parar tudo, use:"
echo "   kill $API_PID"
