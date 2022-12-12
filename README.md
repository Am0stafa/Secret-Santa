# Secret-Santa

```
ICS 505
Cryptography
```
# Assignment 1

# Secret Santa

Secret Santa is a Christmas tradition involving multiple people who are family and friends exchanging gifts they bought for each
other anonymously. The process starts with every member participating drawing a random name, where the name drawn cannot
be the same as that of the person drawing the name.

After the drawing process when each person is assigned someone they will be getting a gift to, each participant then goes and
buys a gift for their supposed recipient, and then the gifts are exchanged.

There are different variations on the process, where some people opt to reveal who the anonymous gifter is, while others assume
a system where each person attempts to guess their gifter, and can only ask once, and be replied to with yes or no.

## Deliverables

- A report in which you include:
    - Your chosen constraints for the problem (You may choose to add as many constraints if you so please, just add a
       clarification as to why you chose said constraints)
    - An explanation of how your protocol works, explained in steps
    - A documentation for the methods in your code (just a brief description of each method is enough)
    - A justification for your chosen protocol/ method of sharing/ method of encryption (if exists)
    - A briefing on how your protocol does against cheaters and how it handles cheater identification and combating
- Your implementation of the secret Santa algorithm, including:
    - A means for drawing/ randomly assigning the gifters for each individual.
    - A means for ensuring anonymity in the system.
    - A means for verifying that each person has received a gift.
    - A means for identifying maliciousness within the system.

## Keys

List of public and private keys for p,q,n,phi = 11,13,143,120 :\n
{
1: 1, 103: 7, 11: 11, 37: 13, 113: 17, 19: 19, 47: 23, 29: 29, 31: 31, 13: 37, 41: 41, 67: 43, 23: 47, 49: 49, 77: 53, 59: 59, 61: 61, 43: 67, 71: 71, 97: 73, 53: 77, 79: 79, 107: 83, 89: 89, 91: 91, 73: 97, 101: 101, 7: 103, 83: 107, 109: 109, 17: 113, 119: 119
}
