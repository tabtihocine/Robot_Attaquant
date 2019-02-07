#include <Servo.h> 
Servo myservo; 
int Echo = A4;  
int Trig = A5; 
int in1 = 6;
int in2 = 7;
int in3 = 8;
int in4 = 9;
int ENA = 5;
int ENB = 11;
int ABS = 100;
int rightDistance = 0;
int leftDistance = 0;
int middleDistance = 0;
char str;

/*
#################### 
##    mouvments    ##
####################
*/
void _mForward()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
 digitalWrite(in1,HIGH);//digital output
 digitalWrite(in2,LOW);
 digitalWrite(in3,LOW);
 digitalWrite(in4,HIGH);
 Serial.println("go forward!");
}

void _mBack()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
 Serial.println("go back!");
}

void _mLeft()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW); 
 Serial.println("go left!");
}

void _mRight()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
 Serial.println("go right!");
} 
void _mStop()
{
  digitalWrite(ENA,LOW);
  digitalWrite(ENB,LOW);
  Serial.println("Stop!");
} 

/*
####################### 
## calcul distance  ##
#######################
*/
int Distance_test()   
{
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance/58;       
  return (int)Fdistance;
} 

/*
####################### 
##        Setup      ##
#######################
*/
void setup() {
  myservo.attach(3);
  Serial.begin(9600);     
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT);  
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);

}

/*Fonction pour faire marcher le robot d'une façon autonome 
*Cette fonction est appelée en appuyant sur la "autonome" dans l'application
*/
void autonome (){
  
    myservo.write(80);
    delay(500); 
    middleDistance = Distance_test();

    if(middleDistance<=60)
    {     
      _mStop();
      delay(500);
           
      myservo.write(90);          
      delay(1000);      
      rightDistance = Distance_test();


      delay(500);
       myservo.write(10);              
      delay(1000);                                                  
      myservo.write(180);              
      delay(1000); 
      leftDistance = Distance_test();

      delay(500);
      myservo.write(90);              
      delay(1000);
      if(rightDistance>leftDistance)  
      {
        _mRight();
        delay(100);
       }
       else if(rightDistance<leftDistance)
       {
        _mLeft();
        delay(100);
       }
       else if((rightDistance<=60)||(leftDistance<=60))
       {
        _mBack();
        delay(180);
       }
       else
       {
        _mForward();
       }
    }  
    else
        _mForward(); 
  }
  

void loop() {
  
    str=Serial.read();

     if(str=='f')
  {
    _mForward();
  }
  else if(str=='b')
  {
    _mBack();
    delay(200);
  }
  else if(str=='l')
  {
    _mLeft();
    delay(200);
  }
  else if(str=='r')
  {
    _mRight();
    delay(200);
    
  }else if (str=='s'){
    _mStop();
    delay(1000);
  }
  else if (str=='a'){
    autonome();
    delay(200);
  }
   
 
}
