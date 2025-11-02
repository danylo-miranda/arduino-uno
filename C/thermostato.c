int thermistorPin = A1;
int seriesResistor = 10000; // Resistor de 10K

void setup() {
  Serial.begin(9600);
}

void loop() {
  int reading = analogRead(thermistorPin);
  float voltage = reading * 5.0 / 1023.0;
  float resistance = seriesResistor * (5.0 - voltage) / voltage;
  
  // NTC 100K com beta 3950
  float steinhart = log(resistance / 100000.0);
  steinhart /= 3950.0;
  steinhart += 1.0 / (25.0 + 273.15);
  steinhart = 1.0 / steinhart;
  float tempC = steinhart - 273.15;

  Serial.print("Temperatura: ");
  Serial.print(tempC);
  Serial.println(" °C");
  
  delay(10000);
}
