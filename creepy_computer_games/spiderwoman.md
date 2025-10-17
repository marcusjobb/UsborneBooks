# Spiderwoman

**Book**: _Creepy Computer Games_
**Author**: [Brendon Kavanagh, Colin Reynolds, Val Robinson, Alan Ramsey, Keith Campbell, Chris Oxlade](https://github.com/marcusjobb/UsborneBooks)
**Translator**: [Marcus Medina](http://marcusmedina.pro)

---

## Story

**Eek! It’s Spiderwoman!**
You’ve stumbled into her web, and she’s in a teasing mood.
She has chosen a secret **letter**, and if you can guess it quickly enough, she might set you free.

To find out what letter she’s thinking of, you must give her a **word**.
If your word contains her letter, she’ll tell you so — but if not, she’ll simply giggle and tighten the web.
Take too many turns and you’ll **transform into a fly**, forever trapped in her silky trap.

---

## Pseudocode

```plaintext
SET number_of_goes = 0
CLEAR screen
CHOOSE a random letter (A–Z)
PRINT "SPIDERWOMAN HAS CHOSEN"

REPEAT UNTIL guessed OR 15 tries used
    ASK player for a word
    INCREASE number_of_goes
    IF word too short (<4) OR too long (>8), ask again

    CHECK if the word contains the chosen letter
    IF yes:
        PRINT "YES – IT’S ONE OF THOSE"
        ASK if player wants to guess the letter
        IF yes:
            ASK for guess
            IF correct:
                PRINT "OK – YOU CAN GO"
                END game
            ELSE:
                PRINT "YOU ARE TOO LATE"
                END game
    ELSE:
        PRINT "IT’S NOT IN THAT WORD"

END LOOP

IF 15 tries used THEN PRINT "YOU ARE NOW A FLY"
```

---

## Flowchart

```mermaid
flowchart TD
    A[Start Game] --> B[Choose random letter A–Z]
    B --> C[Ask for a word]
    C --> D[Increase guess counter]
    D --> E[Check word length 4–8]
    E -->|Invalid| C
    E --> F[Does word contain the letter?]
    F -->|No| G[Print "It's not in that word"]
    G --> H[Delay and repeat]
    F -->|Yes| I[Print "Yes – it's one of those"]
    I --> J[Ask if player wants to guess]
    J -->|No| H
    J -->|Yes| K[Ask for guess]
    K --> L[Correct?]
    L -->|Yes| M[Print "OK – You can go" → End]
    L -->|No| N[Print "You are too late" → End]
    H --> O[If >15 tries → "You are now a fly"]
```

---

## Code

<details>
<summary>ZX-81</summary>

```basic
10 LET G=0
20 CLS
30 LET T=INT(RND*26+38)
40 LET T$=CHR$(T)
50 PRINT "SPIDERWOMAN"
60 PRINT "HAS CHOSEN"
70 PRINT
80 PRINT "TRY A WORD"
90 PRINT
100 INPUT W$
110 LET G=G+1
120 LET L=LEN(W$)
130 IF L<4 OR L>8 THEN GOTO 70
140 LET F=0
160 FOR I=1 TO L
170 LET A$=W$(I TO I)
180 IF A$=T$ THEN LET F=1
190 NEXT I
200 IF F=1 THEN GOTO 280
210 PRINT
220 PRINT "IT'S NOT IN THAT WORD"
230 FOR A=1 TO 20
240 NEXT A
250 IF G>15 THEN GOTO 400
260 CLS
270 GOTO 70
280 PRINT "YES - IT'S ONE OF THOSE"
290 PRINT
300 PRINT "DO YOU WANT TO GUESS? (Y OR N)"
310 INPUT R$
320 IF R$="N" THEN GOTO 250
330 PRINT "WHAT IS YOUR GUESS THEN?"
350 INPUT G$
360 IF G$<>T$ THEN GOTO 410
370 PRINT "OK - YOU CAN GO"
380 PRINT "(THIS TIME)"
390 STOP
400 PRINT "YOU ARE TOO LATE"
410 PRINT "YOU ARE NOW A FLY"
420 STOP
```

</details>

---

<details>
<summary>C#</summary>

```csharp
using System;

class Spiderwoman
{
    static void Main()
    {
        Random rnd = new Random();
        char target = (char)('A' + rnd.Next(0, 26));
        int tries = 0;

        Console.WriteLine("SPIDERWOMAN HAS CHOSEN...");
        Console.WriteLine("Try to find her letter!");

        while (tries < 15)
        {
            Console.Write("\nEnter a word (4–8 letters): ");
            string word = Console.ReadLine()?.ToUpper() ?? "";
            tries++;

            if (word.Length < 4 || word.Length > 8)
                continue;

            if (word.Contains(target))
            {
                Console.WriteLine("Yes – it’s one of those!");
                Console.Write("Do you want to guess the letter? (Y/N): ");
                var answer = Console.ReadKey(true).KeyChar;
                if (char.ToUpper(answer) == 'Y')
                {
                    Console.Write("\nWhat’s your guess? ");
                    var guess = Console.ReadKey(true).KeyChar;
                    if (char.ToUpper(guess) == target)
                    {
                        Console.WriteLine("\nOK – you can go (this time)!");
                        return;
                    }
                    else
                    {
                        Console.WriteLine("\nYou are too late… You are now a fly!");
                        return;
                    }
                }
            }
            else
            {
                Console.WriteLine("It’s not in that word.");
            }
        }

        Console.WriteLine("\nYou’ve taken too long... You are now a fly!");
    }
}
```

</details>

---

<details>
<summary>Python</summary>

```python
import random

def spiderwoman():
    target = chr(random.randint(65, 90))  # A–Z
    tries = 0
    print("SPIDERWOMAN HAS CHOSEN...")
    print("Try to find her letter!")

    while tries < 15:
        word = input("\nEnter a word (4–8 letters): ").upper()
        tries += 1
        if len(word) < 4 or len(word) > 8:
            continue

        if target in word:
            print("Yes – it's one of those!")
            choice = input("Do you want to guess the letter? (Y/N): ").upper()
            if choice == "Y":
                guess = input("What’s your guess? ").upper()
                if guess == target:
                    print("OK – you can go (this time)!")
                    return
                else:
                    print("You are too late... You are now a fly!")
                    return
        else:
            print("It’s not in that word.")

    print("\nYou’ve taken too long... You are now a fly!")

if __name__ == "__main__":
    spiderwoman()
```

</details>

---

## Explanation

Spiderwoman secretly picks a random letter from **A–Z**.
Each turn, you type in a word — if her letter appears within it, she’ll admit it.
You can then decide to make a final guess.
Get it right, and she lets you go.
Get it wrong, and she wraps you in silk forever.

---

## Challenges

1. **Double Chance Rule** – Allow two guesses if the letter is in your word, but lose five turns if wrong.
2. **Spiderweb Timer** – Add a countdown that shortens with every failed guess.
3. **Hint System** – Let Spiderwoman reveal whether her letter is before or after the first letter of your word.
4. **Sound & Color** – Add eerie effects for success and failure.
5. **Word Trap Mode** – If you repeat a word, she automatically wins!

---

## Copyright

These programs are adaptations of the original Usborne Computer Guides published in the 1980s.
The books are free to download for personal or educational use from
[Usborne’s Computer and Coding Books](https://usborne.com/row/books/computer-and-coding-books).
Programs and adaptations may **not** be used for commercial purposes.

Return to [Creepy Computer Games](./readme.md).
