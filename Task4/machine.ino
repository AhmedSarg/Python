
#define led1 1
#define led2 2
#define led3 3
String data;
void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600)
}

void loop() {
  
  if (Serial.available() > 0) {
    data = Serial.readStringUntil("\n");
    if (data == "One") {
      digitaWrite(led1, HIGH);
      digitaWrite(led2, LOW);
      digitaWrite(led3, LOW);
    }
    else if (data == "Two") {
      digitaWrite(led1, LOW);
      digitaWrite(led2, HIGH);
      digitaWrite(led3, LOW);
    }
    else if (data == "Three") {
      digitaWrite(led1, LOW);
      digitaWrite(led2, LOW);
      digitaWrite(led3, HIGH);
    }
    else if (data == "Other") {
      digitaWrite(led1, LOW);
      digitaWrite(led2, LOW);
      digitaWrite(led3, LOW);
    }
  }
  
}
