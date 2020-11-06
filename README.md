# Kata-Python-Elevator
This kata is here for OOP-thinking training.

## Instructions
You have to create an elevator and this is how it should behave.

A building contains an elevator and few floors.
On each floor, there is a button to call the elevator.
Users will interact only with buttons.
A button can ask the elevator to go to a specific floor.
There are buttons inside the elevator and outside of it (on and for each floor).
The elevator can open or close the door and go to a specific floor.
The door can open or close itself.


Once you have done all of this and created a few tests to make sure everything works as intended,
another task awaits you.
A lot of people have complained that the door closes when they are in its way, and it's hurting them.
To prevent this from happening, we need to change the door to one that can sense if people are in the way or not.

You CANNOT update the door that already exists, we need a new one.


After that, we want to have new buttons inside the elevator. 
Buttons with a light that should be on as soon as a user press it and until the elevator reaches the required floor.
Once again, we don't want to modify the existing buttons (and certainly not those on the outside of the elevator). 


# Rules
Create a few classes that represent the system.

## Code
In the `src/main` folder, you should create your classes and in the `src/test` folder, you should put your tests.

## Test it
It is you task to create tests according to your own implementation.


## How to run and test
``` 
git clone --branch adnene-first-try https://github.com/codeworks-data/Kata-Python-Elevator.git
cd Kata-Python-Elevator
export $PYTHONPATH=($PWD)/src/main
```

### Run main
```
python src/main/main.py
```

### Run tests
```
python src/test/ElevatorTest.py
python src/test/FloorButtonsTest.py
```