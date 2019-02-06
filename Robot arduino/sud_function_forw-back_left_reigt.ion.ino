
// roux droite 
int ENA=5; 
int IN1=6;
int IN2=7;

// roux gauche 
int ENB=11; 
int IN3=8;
int IN4=9;

//avancer
void forward(){
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB, HIGH);
  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("Forward");
 
}

//reculer
void move_back(){
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB, HIGH);
  
  digitalWrite(IN1, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("move back");
  
}

//stop
void _stop(){
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB, HIGH);
  
  digitalWrite(IN1, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN4, LOW);
  Serial.println("Stooop");
 
}

// tourner à droite
void turn_right(){
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB, HIGH);

  
  digitalWrite(IN3,LOW);      
  digitalWrite(IN4,HIGH);
  
  //digitalWrite(IN1, LOW);
  //digitalWrite(IN3, LOW);
  //digitalWrite(IN2, HIGH);
  //digitalWrite(IN4, HIGH);
  Serial.println("turn to right");
}

// tourner à gauche
void turn_left(){
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB, HIGH);

   digitalWrite(IN2,LOW);      
  digitalWrite(IN1,HIGH);
  
 // digitalWrite(IN1, LOW);
 // digitalWrite(IN3, HIGH);
 // digitalWrite(IN2, LOW);
 // digitalWrite(IN4, HIGH);
 // Serial.println("turn to left");
  
}


void setup() {
  Serial.begin(9600);
  pinMode(IN1,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
}

void loop() {
  forward();
  delay(2000);
  
  _stop();
  delay(500); 
  
  turn_right();
  delay(50); 
  
  _stop();
  delay(500); 

  forward();
  delay(2000);
 
  _stop();
  delay(500); 
  
  turn_left();
  delay(50);
  
  _stop();
  delay(500);
   
  forward();
  delay(2000);

  _stop();
  delay(500);

  move_back();
  delay(6000);

  _stop();
  delay(500);

}
