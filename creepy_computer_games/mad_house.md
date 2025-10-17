# Mad House

**Book**: _Creepy Computer Games_
**Author**: [Brendon Kavanagh, Colin Reynolds, Val Robinson, Alan Ramsey, Keith Campbell, Chris Oxlade](https://github.com/marcusjobb/UsborneBooks)
**Translator**: [Marcus Medina](http://marcusmedina.pro)

---

## Story

You’re trapped in a weird house where everything moves — even the walls!
If the doorways would just line up for a second, you might escape…

You’ve found a console that seems to control the movements in the house.
Keys **X** and **C** change the direction of the **top** doorway.
Keys **N** and **M** do the same for the **bottom** doorway.
There’s no way to control the **center** one — it moves on its own, and time is running out!

You can hear the phantom footsteps echoing closer and closer.
The counter at the top left of the screen shows how close they are.
If you can’t escape before they reach you...
**...you’ll become just another ghost wandering the Mad House!**

---

## Pseudocode

```plaintext
CREATE two arrays:
 - P(): position of each doorway
 - S(): direction of each doorway

MAKE a row of stars as the top of the room
SET footsteps counter = 240
SET directions for doorways at start
SET random starting positions

REPEAT until escape or footsteps reach 0
    CLEAR screen
    DISPLAY room and doorways
    PRINT footsteps counter (top left)
    CHECK if all three doorways align → YOU’RE FREE
    READ keyboard input:
        * changes top doorway
        X or C → reverse top doorway direction
        N or M → reverse bottom doorway direction
    EVERY 25 steps → move center doorway
    UPDATE doorway positions based on direction
    REDRAW the screen
    DECREASE footsteps counter
END LOOP

IF counter = 0 → TOO LATE, footsteps caught you!
```

---

## Flowchart

```mermaid
flowchart TD
    A[Start Game] --> B[Initialize arrays P() and S()]
    B --> C[Set doorway positions randomly]
    C --> D[Display room and counter]
    D --> E[Check if all three doorways align]
    E -->|Yes| F[Print "YOU ARE FREE!!"]
    E -->|No| G[Check for keypress]
    G --> H[Change doorway direction (X,C,N,M)]
    H --> I[Move doorways based on direction]
    I --> J[Decrease counter]
    J --> K[Check if counter = 0]
    K -->|Yes| L[Print "TOO LATE!"]
    K -->|No| D
    F --> M[End Game]
    L --> M
```

---

## Code

<details>
<summary>ZX-81</summary>

```basic
10 DIM P(3)
20 DIM S(3)
30 CLS
40 PRINT "MAD HOUSE"
50 LET L$=""
60 LET W=31
70 FOR I=1 TO W
80 LET L$=L$+"*"
90 NEXT I
100 LET CT=240
110 LET S(1)=1
120 LET S(3)=-1
130 FOR I=1 TO 3
140 LET P(I)=INT(RND*(W-4)+1)
150 NEXT I
160 CLS
170 FOR I=5 TO 15 STEP 5
180 PRINT AT I,0;L$
190 PRINT AT I,P(I)/5;"> <"
200 NEXT I
210 PRINT AT 0,0;CT;" "
220 IF CT<0 THEN GOTO 450
230 IF P(1)=P(2) AND P(2)=P(3) THEN GOTO 390
240 LET Z$=INKEY$
250 IF Z$="" THEN GOTO 300
260 IF Z$="X" THEN LET S(1)=-1
270 IF Z$="C" THEN LET S(1)=1
280 IF Z$="N" THEN LET S(3)=-1
290 IF Z$="M" THEN LET S(3)=1
300 IF CT/25=INT(CT/25) THEN LET P(2)=P(2)+INT(RND(1)*20)-10
310 LET CT=CT-1
320 LET P(1)=P(1)+S(1)
330 LET P(3)=P(3)+S(3)
340 FOR I=1 TO 3
350 IF P(I)<1 THEN LET P(I)=1
360 IF P(I)>(W-4) THEN LET P(I)=W-4
370 NEXT I
380 GOTO 170
390 LET P(1)=P(1)+1
400 FOR I=1 TO 15
410 PRINT AT I, L; "M"
420 NEXT I
430 PRINT "YOU ARE FREE!!"
440 STOP
450 PRINT "TOO LATE! THE FOOTSTEPS HAVE STOPPED."
460 PRINT "ARGHHHHH!!!!"
470 STOP
```

</details>

---

<details>
<summary>C#</summary>

```csharp
using System;
using System.Threading;

class MadHouse
{
    static void Main()
    {
        const int width = 31;
        int[] P = new int[3];
        int[] S = { 1, 0, -1 };
        Random rnd = new Random();
        int counter = 240;

        for (int i = 0; i < 3; i++)
            P[i] = rnd.Next(1, width - 4);

        while (counter > 0)
        {
            Console.Clear();
            Console.WriteLine($"Footsteps: {counter}");
            for (int i = 0; i < 3; i++)
            {
                string line = new string('*', width);
                line = line.Remove(P[i], 3).Insert(P[i], "> <");
                Console.WriteLine(line);
                Console.WriteLine();
            }

            if (P[0] == P[1] && P[1] == P[2])
            {
                Console.WriteLine("\nYOU ARE FREE!!");
                return;
            }

            if (Console.KeyAvailable)
            {
                var key = Console.ReadKey(true).Key;
                if (key == ConsoleKey.X) S[0] = -1;
                if (key == ConsoleKey.C) S[0] = 1;
                if (key == ConsoleKey.N) S[2] = -1;
                if (key == ConsoleKey.M) S[2] = 1;
            }

            if (counter % 25 == 0)
                P[1] += rnd.Next(-10, 11);

            for (int i = 0; i < 3; i++)
            {
                P[i] += S[i];
                if (P[i] < 1) P[i] = 1;
                if (P[i] > width - 4) P[i] = width - 4;
            }

            Thread.Sleep(50);
            counter--;
        }

        Console.WriteLine("\nTOO LATE! The footsteps have stopped...");
        Console.WriteLine("ARGHHHHHH!!!!");
    }
}
```

</details>

---

<details>
<summary>Python</summary>

```python
import random
import os
import time
import msvcrt

def mad_house():
    width = 31
    positions = [random.randint(1, width - 4) for _ in range(3)]
    directions = [1, 0, -1]
    counter = 240

    while counter > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Footsteps: {counter}\n")
        for p in positions:
            line = list("*" * width)
            line[p:p+3] = [">", " ", "<"]
            print("".join(line))
            print()

        if positions[0] == positions[1] == positions[2]:
            print("\nYOU ARE FREE!!")
            return

        if msvcrt.kbhit():
            key = msvcrt.getwch().upper()
            if key == "X": directions[0] = -1
            if key == "C": directions[0] = 1
            if key == "N": directions[2] = -1
            if key == "M": directions[2] = 1

        if counter % 25 == 0:
            positions[1] += random.randint(-10, 10)

        for i in range(3):
            positions[i] += directions[i]
            positions[i] = max(1, min(width - 4, positions[i]))

        counter -= 1
        time.sleep(0.05)

    print("\nTOO LATE! The footsteps have stopped.")
    print("ARGHHHHHH!!!!")

if __name__ == "__main__":
    mad_house()
```

</details>

---

## Explanation

You control a bizarre console in a shifting house.
Each doorway slides left and right, and you must align all three before the phantom footsteps reach you.
Top doorways respond to **X** and **C**, bottom ones to **N** and **M**.
When the doors line up, you dash through to freedom — but wait too long, and it’s all over...

---

## Challenges

1. **Sound Effects** – Add haunting footsteps and a scream when time runs out.
2. **Speed Mode** – Make the footsteps quicken the longer you play.
3. **Mirror Madness** – Randomly reverse doorway controls for extra chaos.
4. **Escape Counter** – Track how many escapes you manage before failing.
5. **Phantom Door** – Add a fourth, random-moving doorway for experts only.

---

## Copyright

These programs are adaptations of the original Usborne Computer Guides published in the 1980s.
The books are free to download for personal or educational use from
[Usborne’s Computer and Coding Books](https://usborne.com/row/books/computer-and-coding-books).
Programs and adaptations may **not** be used for commercial purposes.

Return to [Creepy Computer Games](./readme.md).
