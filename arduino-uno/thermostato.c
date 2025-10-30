#include <thermistor.h> //precisa instalar a lib no IDE arduino

int pinNTC = A1;
float temperatura;

// Parâmetros: (pino, resistência de referência, beta, resistência nominal)
THERMISTOR thermistor(pinNTC, 10000, 3950, 10000);

void setup() {
  Serial.begin(9600);  
}

void loop() {
  temperatura = thermistor.read();

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");
  Serial.println(""); // apenas uma linha em branco para espaçar

  delay(10000);
}
