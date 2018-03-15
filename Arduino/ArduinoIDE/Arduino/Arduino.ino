#define LED 13

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        int intensity = Serial.read();
        if(intensity == '1'){
        digitalWrite(LED,HIGH);
        }
        else{
        digitalWrite(LED,LOW);
        }
    }
}


