---
layout: post
title: "Bluetooth-controlled autonomous robot using Python"
description: " "
date: 2023-09-18
tags: [define, define]
comments: true
share: true
---

In this blog post, we will discuss how to create a Bluetooth-controlled autonomous robot using Python. By combining the power of Python programming language and Bluetooth communication, we can create a robot that can be controlled wirelessly. So, let's dive right in!

## Hardware Requirements:
- Microcontroller board (e.g., Arduino or Raspberry Pi)
- Bluetooth module (e.g., HC-05)
- Motor driver module
- Motors and wheels
- Power supply
- Chassis

## Software Requirements:
- Arduino IDE
- Python IDE (e.g., PyCharm)

## 1. Setting up the Hardware

First, we need to assemble the robot by connecting the components together. Attach the motors to the chassis and connect them to the motor driver module. Connect the power supply to the motor driver and the microcontroller board. Finally, connect the Bluetooth module to the microcontroller board.

## 2. Programming the Microcontroller Board

Now, let's write the code for the microcontroller board (e.g., Arduino) to control the motors based on the commands received from the Bluetooth module.

```arduino
#define ENA 5 // PWM pin for Motor A speed control
#define IN1 6 // Motor A direction control pin
#define IN2 7 // Motor A direction control pin
#define ENB 9 // PWM pin for Motor B speed control
#define IN3 10 // Motor B direction control pin
#define IN4 11 // Motor B direction control pin

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    // Forward
    if (command == 'F') {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
    }

    // Backward
    else if (command == 'B') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
    }

    // Left
    else if (command == 'L') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
      analogWrite(ENA, 150);
      analogWrite(ENB, 150);
    }

    // Right
    else if (command == 'R') {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
      analogWrite(ENA, 150);
      analogWrite(ENB, 150);
    }

    // Stop
    else if (command == 'S') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
      analogWrite(ENA, 0);
      analogWrite(ENB, 0);
    }
  }
}
```

Upload this code to the microcontroller board using the Arduino IDE.

## 3. Writing the Python Code

Next, we need to write Python code to establish a Bluetooth connection with the microcontroller board and send commands to control the robot.

```python
import serial

bluetooth_port = "/dev/rfcomm0"  # Bluetooth port
bluetooth_baud = 9600  # Baud rate

# Establish Bluetooth connection
bluetooth = serial.Serial(bluetooth_port, bluetooth_baud)

def send_command(command):
    bluetooth.write(command.encode())

# Command the robot
send_command('F')  # Move forward
send_command('L')  # Turn left
send_command('R')  # Turn right
send_command('B')  # Move backward
send_command('S')  # Stop

# Close Bluetooth connection
bluetooth.close()
```

Save this Python code as `autonomous_robot.py` and run it from the Python IDE.

## Conclusion

By following the steps above, we have successfully created a Bluetooth-controlled autonomous robot using Python and Arduino (or any other microcontroller board). This allows us to control the robot wirelessly and enable it to perform various tasks autonomously. The possibilities are endless when it comes to extending the functionalities of this robot. So, grab your hardware, write your own code, and start exploring the world of Bluetooth-controlled robotics! 

Remember to use the hashtags: #Python #Robotics