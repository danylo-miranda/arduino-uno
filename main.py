import serial
import time
import csv
from datetime import datetime

# ==============================
# CONFIGURAÇÕES
# ==============================
PORTA = "/dev/ttyUSB0"   # Porta do Arduino
BAUDRATE = 9600           # Mesmo valor usado no Serial.begin() do Arduino
ARQUIVO_SAIDA = "dados_serial.csv"

# ==============================
# INICIALIZAÇÃO
# ==============================
def inicializar_serial():
    try:
        ser = serial.Serial(PORTA, BAUDRATE, timeout=1)
        time.sleep(2)  # tempo para estabilizar a comunicação
        print(f"✅ Conectado à porta {PORTA}")
        return ser
    except Exception as e:
        print(f"❌ Erro ao conectar na porta {PORTA}: {e}")
        exit(1)

# ==============================
# FUNÇÃO PRINCIPAL
# ==============================
def registrar_dados():
    ser = inicializar_serial()

    # Cria o arquivo CSV (caso não exista)
    with open(ARQUIVO_SAIDA, mode="a", newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        # Cabeçalho (somente se o arquivo estiver vazio)
        if arquivo_csv.tell() == 0:
            writer.writerow(["timestamp", "valor"])

        print("📡 Iniciando leitura... (Ctrl+C para parar)\n")

        try:
            while True:
                if ser.in_waiting > 0:
                    linha = ser.readline().decode("utf-8").strip()
                    if linha:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        writer.writerow([timestamp, linha])
                        arquivo_csv.flush()
                        print(f"[{timestamp}] {linha}")
        except KeyboardInterrupt:
            print("\n🛑 Leitura encerrada pelo usuário.")
        finally:
            ser.close()
            print("🔌 Conexão serial encerrada.")

# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    registrar_dados()
