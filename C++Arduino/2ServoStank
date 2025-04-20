#include <Servo.h>
Servo s1, s2;
int pan, tilt;
char mess;
int x, y;

void setup() {
    Serial.begin(9600);
    s1.attach(26);
    s2.attach(27);
}

void loop() {
    if (Serial.available() > 0) {
        mess = Serial.read();
        if (mess == 'P') {
            pan = Serial.parseInt();
            Serial.println(pan);
        }
        if (mess == 'T') {
            tilt = Serial.parseInt();
            Serial.println(tilt);
        }

        x = map(pan, 150, 400, 0, 180);
        y = map(tilt, 150, 330, 0, 180);
        Serial.println(String(x) + "\t" + String(y));
        s1.write(x);
        s2.write(y);
    }
}