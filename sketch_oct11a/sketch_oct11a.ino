#include <Servo>

#define IN1 4
#define IN2 3
#define IN3 6
#define IN4 5
#define CB 2

Servo s1;
Servo s2;

void setup() {
  Serial.begin(9600);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(CB, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  
  s1.attach(9);
  s2.attach(10);
  
  s1.write(180);
  s2.write(0);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);

    if (data == "1") {
      test_dc_run(135, 0);
    } else if (data == "2") {
      test_dc_run(180, 45);
    }
  }
}

void test_dc_run(int servo1_angle, int servo2_angle) {
  s1.write(servo1_angle);
  s2.write(servo2_angle);

  digitalWrite(IN1, LOW);
  analogWrite(IN2, 150);
  delay(4000);
  s1.write(180);
  s2.write(0);

  digitalWrite(IN1, LOW);
  analogWrite(IN2, LOW);
}
