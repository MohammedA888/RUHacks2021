# Home Servant Bot

## Inspiration

As lazy university students we never put our shoes away properly when we get home, this causes our parents (especially mom) to get angry because its messy and dangerous. To solve this issue we created an AI/Robot system that checks when a shoe is taken off and then proceeds to place it into the shoe rack for you.

## What it does

The robot scans the area using a camera, then using AI it checks if there is a SHOE on the mat then checks if there is space on the shoe rack (using Ultrasonic Distance Sensors), then proceeds to use a combination of DC and Stepper Motors to pick the shoes up and place it into the shoe rack.

## How we built it

We used 3 Stepper Motors, to control the arms of the robot allowing it to elevate up and down, turn left and right, and rotate forwards and backwards. We created an arm that can move with 5 degrees of freedom in 3D Space. Then we used 2 DC motors to control the "Wrist" of the arms to turn the ramp that holds the shoe into place, and the other DC motor to move the shoe off the ramp using a treadmill like system. We used a camera system that we trained using Neural Networks to recognize the left and right shoe, along with the sole. Also we used the camera to figure the approximate distance from the shoe so the motors may turn accordingly to reach the shoe. We have 2 sensors that check for whether or not the current shoe rack is being occupied, and if it is not then we tell the motor to move up down left or right depending on availability. We ran the entire system through Raspberry Pi 3 Model B and coded it using Python.


## Demo Video

[![Home Servant Bot](https://github.com/MohammedA888/RUHacks2021/blob/main/RU%20Hacks%20Image.png)](https://www.youtube.com/watch?v=YLyF9gJMwVE)


## Sample Training Pictures

## Shoe Example 1 - 120°

<img src="https://github.com/MohammedA888/RUHacks2021/blob/main/CNN%20Training%20Dataset/1587065460-Mens-193-Royale-TripleBlack-3RBW-Product-102_987ae47c-343a-4a46-9902-2f233bd5452c.jpg" alt="Shoe Example 1" width="400" height="500">

## Shoe Example 1 - 240°

<img src="https://github.com/MohammedA888/RUHacks2021/blob/main/CNN%20Training%20Dataset/84bbb268364a43cb9766b5aeb71901b9.jpg" alt="Shoe Example 2" width="400" height="500">


## Challenges we ran into

Due to time constraints it was extremely difficult to train the neural networks really well. Another complication we ran into because of time was that we weren't able to 3D print a proper ramp to fit the shoe onto it. Near the end due to us running the circuit for a extended period of time (to record) the final step of the robot was unable to work due to circuit shorting. Due to COVID-19 it was hard to gather ALL the parts needed to run this exactly how we wanted to.


## Accomplishments that we're proud of

We are extremely proud of the fact that we were able to get all the motors to turn and compact it into a small design. We were able to connect all the circuits through a color coded system that we were able to utilize really well. We are also proud of using the CNN to train the program to recognize shoes only, since we have never worked with Neural Networks this was huge for us. We are also really proud of using Raspberry Pi for the first time in connection with the motors and the entire system. Also because it was Ramadan, we were limited to time because 2 of our 4 members partake in fasting and were fatigued throughout the day alone with having to gather with family and eat dinner after the sunset.


## What we learned

To procure better materials in order to distribute the weight of the system better, because it was unable to hold near the end.

## What's next for Home Servant Bot

We are going to continue working on this project as a Summer Project for the 4 of us since we are extremely ambitious about what we can accomplish with this. We are going to 3D print the entire system better, and train the CNN for longer so that we will have a fully running system that we will hopefully use if made compact.

## Built With

C++, Python, TensorFlow, Raspberry Pi
