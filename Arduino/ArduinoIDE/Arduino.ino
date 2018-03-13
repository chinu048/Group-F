
int redLEDPin=13; //Declare redLEDPin an int, and set to pin 13
int numRedBlinks;  //Number of times to blink red LED
String redMessage="The Red LED is Blinking"; //Declaring a String Variable 
int redOnTime;
int redOffTime;
int intensity;
int time_duration;


void setup() {
  Serial.begin(9600);        // Turn on the Serial Port
  pinMode(redLEDPin, OUTPUT);  // Tell Arduino that redLEDPin is an output pin
  Serial.println("this shits here");
  Serial.println("Experiment Time "); //Prompt User for Input
  while (Serial.available()==0){ }  //Wait for User Input
  time_duration = Serial.parseInt(); //Read User Input
  Serial.println("this shit");
 
  Serial.println("ON time "); //Prompt User for Input
  while (Serial.available()==0){ }  //Wait for User Input
  redOnTime = Serial.parseInt(); //Read User Input
  
  Serial.println("OFF time "); //Prompt User for Input
  while (Serial.available()==0){ }  //Wait for User Input
  redOffTime = Serial.parseInt(); //Read User Input
  
  Serial.println("Intensity:"); //Prompt User for Input
  while (Serial.available()==0){ }  //Wait for User Input
  intensity = 51 * Serial.parseInt(); //Read User Input
}
 
void loop() {
 
int starttime = millis();
int endtime = starttime;
int loopcount = 0;
while (endtime - starttime <= time_duration ) // do this loop for up to 1000mS
{
   // Serial.println(redMessage); 
    analogWrite(redLEDPin, intensity); //Turn red LED on
    delay(redOnTime);             //Leave on for redOnTime
    analogWrite(redLEDPin, 0);  //Turn red LED off
    delay(redOffTime);            //Leave off for redOffTime
    loopcount = loopcount+1;
    endtime = millis();
}
    
}


