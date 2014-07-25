#include <IRremote.h>

// An IR LED must be connected to Arduino PWM pin 3.

IRsend irsend;
char cmd = ' '; 

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        cmd = Serial.read();
        Serial.print("received: ");
        Serial.println(cmd);
        switch(cmd) {
            case 'p':
                irsend.sendNEC(0x10AF8877, 32);
                Serial.println("power");
                break;
            case 'u':
                irsend.sendNEC(0x10AF708F, 32);
                Serial.println("temperature up");
                break;
            case 'd':
                irsend.sendNEC(0x10AFB04F, 32);
                Serial.println("temperatue down");
                break;
            case 'l':
                irsend.sendNEC(0x10AF20DF, 32);
                Serial.println("fan slower");
                break;
            case 'r':
                irsend.sendNEC(0x10AF807F, 32);
                Serial.println("fan faster");
                break;
            case 'c':
                irsend.sendNEC(0x10AF906F, 32);
                Serial.println("cool");
                break;
            case 'e':
                irsend.sendNEC(0x10AF40BF, 32);
                Serial.println("energy saver");
                break;
            case 'f':
                irsend.sendNEC(0x10AFE01F, 32);
                Serial.println("fan only");
                break;
            Serial.println("bad command");
        }
    }
}
