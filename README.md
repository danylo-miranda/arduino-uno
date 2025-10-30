# 📡 Projeto Arduino + Python + FastAPI

## 🧠 Visão Geral

Este projeto tem como objetivo coletar **dados do Arduino via porta serial**, registrar em arquivo CSV e disponibilizá-los por meio de uma **API desenvolvida com FastAPI**, incluindo uma **interface web interativa (dashboard)** para visualização dos dados em tempo real.

---

## ⚙️ Estrutura do Projeto

```
arduino-uno/
│
├── main.py # Script Python para leitura da porta serial e gravação dos dados
├── main_api.py # API FastAPI para servir os dados
├── start_api.sh # Script para iniciar a API e o túnel ngrok automaticamente
├── dados_serial.csv # Arquivo gerado com as leituras do Arduino
└── templates/
└── dashboard.html # Página web com gráfico interativo (Chart.js)
```

---

## 🧩 Componentes

### 🔸 Arduino
O Arduino coleta dados de sensores (por exemplo: temperatura, umidade, luminosidade, etc.) e envia as leituras pela porta serial via `Serial.println()`.

### Exemplo simples de código Arduino:
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(1000);
}
```

### 🔸 Python – Leitura Serial (main.py)

### Responsável por:

* Ler os dados do monitor serial do Arduino

* Armazenar em dados_serial.csv

### 🔸 API – FastAPI (main_api.py)

### A API lê o arquivo CSV e disponibiliza endpoints para:

* Consultar os dados em JSON

* Baixar o CSV completo

* Visualizar os dados em gráfico interativo

**Principais Endpoints:**

| Endpoint     | Descrição                          | Tipo |
| ------------ | ---------------------------------- | ---- |
| `/`          | Status da API                      | JSON |
| `/dados`     | Últimos 100 registros              | JSON |
| `/dados/csv` | Download do arquivo completo       | CSV  |
| `/dashboard` | Visualização interativa (Chart.js) | HTML |


### 🔸 Dashboard (templates/dashboard.html)

Interface web simples e responsiva feita com Chart.js.

Exibe os 100 últimos registros do CSV em um gráfico de linha com atualização manual.

### 🌍 Publicação Online

O projeto usa ngrok para tornar a API acessível pela internet (sem precisar de hospedagem externa).

**Instalar o ngrok:**

```
sudo snap install ngrok
ngrok config add-authtoken SEU_TOKEN_AQUI
```

**Executar o túnel:**

```
ngrok http 8000
```

**Após executar, será exibido um link como:**

```
Forwarding https://overfearfully-ineffective-noah.ngrok-free.dev -> http://localhost:8000
```

**Esse é o endereço público para você acessar:**

* API JSON: https://.../dados

* CSV: https://.../dados/csv

* Dashboard: https://.../dashboard

### 🚀 Execução Completa
1️⃣ Iniciar coleta de dados

Conecte o Arduino e rode:

python3 main.py

2️⃣ Subir API e túnel ngrok (automático)

Execute o script:

./start_api.sh


Ele fará:

Iniciar a API (Uvicorn)

Criar o túnel com ngrok

Exibir o link público automaticamente

Exemplo de saída:

🚀 Iniciando API FastAPI na porta 8000...
🌍 Iniciando túnel ngrok...
✅ API está online!
📡 Link público: https://example.ngrok-free.dev
🧩 Endpoints disponíveis:
   🔹 / 
   🔹 /dados
   🔹 /dados/csv
   🔹 /dashboard

### 🧠 Tecnologias Utilizadas

| Componente      | Descrição                      |
| --------------- | ------------------------------ |
| **Arduino UNO** | Leitura de sensores            |
| **Python 3**    | Processamento e API            |
| **FastAPI**     | Framework web para APIs        |
| **Pandas**      | Manipulação de dados CSV       |
| **Jinja2**      | Renderização de templates HTML |
| **Chart.js**    | Visualização de dados          |
| **ngrok**       | Exposição segura da API online |

### 🧪 Possíveis Extensões

Atualização automática do gráfico em tempo real (via AJAX ou WebSocket)

Integração com banco de dados (SQLite, PostgreSQL)

Envio de alertas (e-mail ou Telegram)

Armazenamento em nuvem (Google Sheets, Firebase, etc.)

### 👨‍💻 Autores

Danylo Miranda
Misael Rodrigues

Franca, 30 de Outubro de 2025

📝 Licença

Este projeto é de uso educacional e pode ser modificado livremente para fins de estudo e pesquisa.
