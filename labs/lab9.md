# Lab 9 code 


```
// include the library code:
#include <LiquidCrystal.h>
#include <avr/interrupt.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28);
int __counter = 0;
int _minutes;
int _millisTimestamp;


//arduino runs the setup function first, then the loop function below
void setup() {
  pinMode(24, OUTPUT); //K
  pinMode(26, OUTPUT); //A
  pinMode(54, OUTPUT); //VSS
  pinMode(52, OUTPUT); //VDD
  pinMode(50, OUTPUT); //Contrasty pin

  // digitalWrite(50, LOW);
  digitalWrite(24, LOW); //Backlight
  digitalWrite(26, HIGH); //Backlight
  digitalWrite(54, LOW); //GND
  digitalWrite(52, HIGH); //VDD
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
  // Timer0 is used for millis() - we'll just interrupt
  // in the middle and call the compA
  OCR0A = 0x01;
  TIMSK0 |= _BV(OCIE0A);
  _minutes = 0;
  _millisTimestamp = millis();
}

SIGNAL(TIMER0_COMPA_vect) 
{
   __counter++;
   if (__counter > 14){
      digitalWrite(50,HIGH);
      __counter = 0;
   }
   else if (__counter > 3){
      digitalWrite(50, LOW);
   }
}



void displayTimer(String command) {
  int i;
  Serial.println(command);
  String time = "";
  time = String(time + command[1]);
  time = String(time + command[2]);
  time = String(time + ':');
  time = String(time + command[3]);
  time = String(time + command[4]);
  Serial.println(time);
  int hours = 10*(command[1] - '0') + (command[2] - '0');
  int minutes = 10*(command[3] - '0') + (command[4] - '0');
  _minutes = minutes + 60* hours;

}

//Here is where your code goes. Arduino runs this function in an infinite loop after running the setup function
void loop() {
  lcd.home();
  lcd.clear();
  //_minutes += 1;
  unsigned int _milisCurrent = millis();
  int _minutesCurrent = _minutes + ((_milisCurrent-_millisTimestamp)/1000/60);
  lcd.print(String(_minutesCurrent/60/10) + String(_minutesCurrent/60%10) + String(':') 
                                          + String(_minutesCurrent%60/10) + String(_minutesCurrent%60%10) + String(':') 
                                          + String(_milisCurrent/1000%60/10) + String(_milisCurrent/1000%60%10));
  if(Serial.available() > 0){
    String message = Serial.readString();// read a string sent from the computer
    displayTimer(message); 
  }
  //sleep for 2 second
}



```
