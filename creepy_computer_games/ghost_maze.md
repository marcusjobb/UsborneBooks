# Ghost Maze

**Book**: _Creepy Computer Games_
**Author**: [Brendon Kavanagh, Colin Reynolds, Val Robinson, Alan Ramsey, Keith Campbell, Chris Oxlade](https://github.com/marcusjobb/UsborneBooks)
**Translator**: [Marcus Medina](http://marcusmedina.pro)

---

## Story

It’s a **creepy maze** — a place of identical dark corridors that all look the same.
You can only see **straight ahead**, and the walls seem to shift when you turn.
Some say the maze is haunted, others say it’s alive…

You must find the **cross-shaped exit** to escape.
Your position is marked as **Y**, walls are **#**, and ghosts appear as **G**.
If you get too close to a ghost, it will teleport you somewhere random — disoriented and lost!

Move forward, turn left or right, and watch the corridors ahead.
Can you find the exit before the ghosts close in?

---

## Controls

- **X** → Move Forward
- **M** → Turn Right
- **N** → Turn Left

You can only see what’s directly ahead — every turn changes your perspective.
Ghosts move unpredictably, and each turn draws them nearer...

---

## Pseudocode

```plaintext
CREATE array E() for maze layout (1 = path, 0 = wall, 9 = exit)
CREATE array V$() for visible 4x3 section
CREATE array F() for ghost positions

SET random start position for player in a corridor
SET random direction (1–4)
SET ghost position randomly

LOOP until escaped
    GET player input:
        N = turn left
        M = turn right
        X = move forward
    MOVE ghost every 5 turns
    UPDATE player position and facing direction
    PRINT visible section of maze
    IF player reaches exit → print “You Have Escaped!”
    IF ghost catches player → teleport to new position
END LOOP
```

---

## Flowchart

```mermaid
flowchart TD
    A[Start Game] --> B[Create Maze Arrays]
    B --> C[Set Player Start and Direction]
    C --> D[Set Ghost Position]
    D --> E[Draw Maze Section]
    E --> F[Player Input N/M/X]
    F --> G[Move or Turn]
    G --> H[Move Ghost Every 5 Turns]
    H --> I[Check for Ghost Encounter]
    I -->|Caught| J[Teleport Player]
    I -->|Safe| K[Check for Exit]
    K -->|Found Exit| L[Print "You Have Escaped!"]
    K -->|Still Inside| E
    J --> E
    L --> M[End Game]
```

---

## Code

<details>
<summary>ZX-81</summary>

```basic
10 DIM E(70)
20 DIM V$(4,3)
30 DIM F(3)
40 LET W$=""
50 LET W$=W$+"0000000000"
60 LET W$=W$+"0111100110"
70 LET W$=W$+"0010111000"
80 LET W$=W$+"0110100110"
90 LET W$=W$+"0011111000"
100 LET W$=W$+"0000000900"
120 FOR I=1 TO 70
130 LET E(I)=VAL(MID$(W$,I,1))
140 NEXT I
150 LET S=-1
160 LET H=0
170 LET X=INT(RND*50)+10
180 IF E(X)<1 THEN GOTO 170
190 GOSUB 860
200 LET D=INT(RND*4)+1
210 IF X+10 OR X=G-10 THEN GOTO 170
220 IF X+1 OR X=G-1 THEN GOTO 170
230 LET H=H+1
240 IF H=5 THEN GOSUB 860
250 GOSUB 390
260 LET A$=INKEY$
270 IF A$="" THEN GOTO 260
280 IF A$="M" THEN LET D=D+1
290 IF A$="N" THEN LET D=D-1
300 IF D=5 THEN LET D=1
310 IF D=0 THEN LET D=4
320 IF A$="X" THEN GOTO 330
330 IF D=1 AND E(X-10)>0 THEN LET X=X-10
340 IF D=3 AND E(X+10)>0 THEN LET X=X+10
350 IF D=2 AND E(X+1)>0 THEN LET X=X+1
360 IF D=4 AND E(X-1)>0 THEN LET X=X-1
370 IF E(X)=9 THEN GOTO 930
380 GOTO 210
390 FOR I=1 TO 4
400 LET T=I-1
410 GOTO 380+40*T
420 LET F(1)=X-10+T
430 LET F(2)=X-10
440 LET F(3)=X-10-T
450 GOTO 570
460 LET F(1)=X+10+T
470 LET F(2)=X+10
480 LET F(3)=X+10-T
490 GOTO 570
500 LET F(1)=X-T
510 LET F(2)=X
520 LET F(3)=X+T
530 GOTO 570
540 LET F(1)=X-T
550 LET F(2)=X-T
560 LET F(3)=X-T
570 FOR J=1 TO 3
580 IF F(J)<1 OR F(J)>69 THEN GOTO 640
590 IF E(F(J))=0 THEN LET V$(I,J)="#"
600 IF E(F(J))=1 THEN LET V$(I,J)="="
610 IF E(F(J))=9 THEN LET V$(I,J)="+"
620 IF E(F(J))=2 THEN LET V$(I,J)="G"
630 NEXT J
640 NEXT I
650 LET V$(1,2)="Y"
660 CLS
670 PRINT
680 PRINT "**** GHOST MAZE ****"
690 PRINT
700 PRINT "FORWARD X"
710 PRINT "TURN RIGHT M"
720 PRINT "TURN LEFT N"
730 FOR I=1 TO 5
740 PRINT
750 NEXT I
760 FOR I=4 TO 1 STEP -1
770 LET P$=""
780 FOR J=3 TO 1 STEP -1
790 LET P$=P$+V$(I,J)
800 NEXT J
810 PRINT TAB(7);P$
820 NEXT I
830 RETURN
840 LET V$(I,J)="#"
850 LET E(G)=1
860 LET G=INT(RND*50)+10
870 IF E(G)<1 THEN GOTO 870
880 LET E(G)=2
890 LET H=0
900 LET S=0
910 RETURN
920 PRINT "YOU HAVE ESCAPED"
930 PRINT "IN ";S*5+H;" MOVES"
940 STOP
```

</details>

---

<details>
<summary>C#</summary>

```csharp
using System;
using System.Threading;

class GhostMaze
{
    static int[,] maze;
    static (int x, int y) player;
    static (int x, int y) ghost;
    static int direction; // 0=N, 1=E, 2=S, 3=W
    static int steps;
    static Random rnd = new Random();

    static void Main()
    {
        GenerateMaze();
        direction = rnd.Next(0, 4);
        player = (rnd.Next(1, 6), rnd.Next(1, 6));
        ghost = (rnd.Next(1, 6), rnd.Next(1, 6));
        while (maze[player.x, player.y] != 1)
            player = (rnd.Next(1, 6), rnd.Next(1, 6));

        while (true)
        {
            Console.Clear();
            DrawView();
            Console.WriteLine("\nMove: X=Forward, N=Left, M=Right");
            Console.WriteLine($"Steps: {steps}");

            if (maze[player.x, player.y] == 9)
            {
                Console.WriteLine("\nYOU HAVE ESCAPED!");
                return;
            }

            if (player == ghost)
            {
                Console.WriteLine("\nA ghost caught you! Teleporting...");
                Thread.Sleep(1000);
                player = (rnd.Next(1, 6), rnd.Next(1, 6));
            }

            var key = Console.ReadKey(true).Key;
            if (key == ConsoleKey.N) direction = (direction + 3) % 4;
            if (key == ConsoleKey.M) direction = (direction + 1) % 4;
            if (key == ConsoleKey.X) MovePlayer();

            if (steps % 5 == 0) MoveGhost();
            steps++;
        }
    }

    static void GenerateMaze()
    {
        int[,] map = {
            {0,0,0,0,0,0,0},
            {0,1,1,1,1,0,0},
            {0,0,1,0,1,1,0},
            {0,1,1,1,0,1,0},
            {0,0,1,1,1,1,0},
            {0,0,0,0,0,9,0},
            {0,0,0,0,0,0,0},
        };
        maze = map;
    }

    static void MovePlayer()
    {
        var (x, y) = player;
        (int dx, int dy) = direction switch
        {
            0 => (-1, 0),
            1 => (0, 1),
            2 => (1, 0),
            3 => (0, -1),
            _ => (0, 0)
        };

        int nx = x + dx, ny = y + dy;
        if (maze[nx, ny] != 0)
            player = (nx, ny);
    }

    static void MoveGhost()
    {
        int dx = Math.Sign(player.x - ghost.x);
        int dy = Math.Sign(player.y - ghost.y);
        if (maze[ghost.x + dx, ghost.y + dy] != 0)
        {
            ghost.x += dx;
            ghost.y += dy;
        }
    }

    static void DrawView()
    {
        for (int i = 1; i < 6; i++)
        {
            for (int j = 1; j < 6; j++)
            {
                char c = maze[i, j] switch
                {
                    0 => '#',
                    1 => ' ',
                    9 => '+',
                    _ => '?'
                };
                if (i == player.x && j == player.y) c = 'Y';
                if (i == ghost.x && j == ghost.y) c = 'G';
                Console.Write(c);
            }
            Console.WriteLine();
        }
    }
}
```

</details>

---

<details>
<summary>Python</summary>

```python
import random, os, time, msvcrt

def ghost_maze():
    maze = [
        [0,0,0,0,0,0,0],
        [0,1,1,1,1,0,0],
        [0,0,1,0,1,1,0],
        [0,1,1,1,0,1,0],
        [0,0,1,1,1,1,0],
        [0,0,0,0,0,9,0],
        [0,0,0,0,0,0,0],
    ]
    player = [1,1]
    ghost = [4,3]
    direction = random.randint(0,3)
    steps = 0

    while True:
        os.system("cls" if os.name=="nt" else "clear")
        print(f"Steps: {steps}\n")
        for i in range(1,6):
            line = ""
            for j in range(1,6):
                ch = "#" if maze[i][j]==0 else " "
                if maze[i][j]==9: ch="+"
                if [i,j]==player: ch="Y"
                if [i,j]==ghost: ch="G"
                line += ch
            print(line)

        if maze[player[0]][player[1]] == 9:
            print("\nYOU HAVE ESCAPED!")
            break
        if player == ghost:
            print("\nA ghost caught you! Teleporting...")
            player = [random.randint(1,5), random.randint(1,5)]
            time.sleep(1)

        if msvcrt.kbhit():
            key = msvcrt.getwch().upper()
            if key == "N": direction = (direction - 1) % 4
            elif key == "M": direction = (direction + 1) % 4
            elif key == "X":
                moves = [(-1,0),(0,1),(1,0),(0,-1)]
                dr,dc = moves[direction]
                nr,nc = player[0]+dr, player[1]+dc
                if maze[nr][nc] != 0:
                    player = [nr,nc]

        if steps % 5 == 0:
            dr = (player[0]>ghost[0]) - (player[0]<ghost[0])
            dc = (player[1]>ghost[1]) - (player[1]<ghost[1])
            if maze[ghost[0]+dr][ghost[1]+dc] != 0:
                ghost[0]+=dr; ghost[1]+=dc

        steps += 1
        time.sleep(0.2)

if __name__ == "__main__":
    ghost_maze()
```

</details>

---

## Explanation

You wander through a haunted maze, seeing only the corridor in front of you.
Ghosts move mysteriously — if they catch you, you’re whisked to another part of the labyrinth.
The exit is hidden, but each turn reveals part of your surroundings.
Find the cross (**+**) and escape before the maze traps your soul!

---

## Challenges

1. **Add Sound** – Play a sound whenever a ghost appears.
2. **Better Graphics** – Replace symbols with colored characters or emoji.
3. **Bigger Maze** – Expand the grid for longer exploration.
4. **Haunting Fog** – Randomly hide parts of the maze for added fear.
5. **Multiple Ghosts** – Spawn more enemies that move independently.

---

## Copyright

These programs are adaptations of the original Usborne Computer Guides published in the 1980s.
The books are free to download for personal or educational use from
[Usborne’s Computer and Coding Books](https://usborne.com/row/books/computer-and-coding-books).
Programs and adaptations may **not** be used for commercial purposes.

Return to [Creepy Computer Games](./readme.md).
