#define LED 13
int onTime = 2000;
int offTime = 1000;


void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    while (Serial.available() == 0){}
    int intensity = Serial.read();
    Serial.println(intensity);
    digitalWrite(LED,HIGH);
    delay(onTime);
    digitalWrite(LED,LOW);
    delay(offTime);
    
}
