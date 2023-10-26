*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position. Domain Model \n\n https://github.com/level-up-program/team-11-dominators-73ebb1b4/blob/20d672e60910aa71bd39b729a7a94686c6b1927e/tests/robot/images/Dominators_DM.jpeg
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Move to the right one step.         5             5             1                     WEST          4           5           2
Spider-main                         4             5             1                     NORTH         4           6           2      
Fire                                5             5             104                   SOUTH         5           4           105
W                                   0             0             105                   EAST          1           0           106
A                                   0             0             121                   WEST          0           0           120
F                                   0             0             98                    NORTH         0           0           122
W1                                  0             0             100                   SOUTH         0           0           101      
F1                                  9             9             108                   EAST          9           9           109


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}