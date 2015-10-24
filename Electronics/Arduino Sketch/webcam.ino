const int v1 = 6;
const int g1 = 10;
const int v2 = 9;
const int g2 = 11;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  pinMode(v1, OUTPUT);
pinMode(g1, OUTPUT);   
  pinMode(v2, OUTPUT);
pinMode(g2, OUTPUT); 
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  if(Serial.available()){
    if(Serial.read() == '0')
    {
      moveb();
    } else {
      movef();
    }
  }
  
}
void movef(){
  digitalWrite(v2,HIGH);
  digitalWrite(g2,LOW);
  digitalWrite(v1,HIGH);
  digitalWrite(g1,LOW);
  delay(200);
  digitalWrite(v2,LOW);
  digitalWrite(g2,LOW);
  digitalWrite(v1,LOW);
  digitalWrite(g1,LOW);
}

void moveb(){
  digitalWrite(v1,LOW);
  digitalWrite(g1,HIGH);
  digitalWrite(v2,LOW);
  digitalWrite(g2,HIGH);
  delay(200);
  digitalWrite(v2,LOW);
  digitalWrite(g2,LOW);
  digitalWrite(v1,LOW);
  digitalWrite(g1,LOW);
}
