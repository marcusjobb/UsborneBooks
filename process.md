▌ 1 - read all the images on ./img/ and transcribe only game description and zx81 code to ./{gamename}.md
▌ 2 - convert zx-81 code to c#, python, java, golang, c++ and rust
▌ 3 - check the code to make sure it's functional

Example:

# (game name)

**Book**: _(book name)_
**Author**: [(authors)](https://github.com/marcusjobb/UsborneBooks)
**Translator**: [Marcus Medina](http://marcusmedina.pro)

## Story

(game story and controls explanations)

## Pseudocode

```plaintext

```

## Flowchart

```mermaid
flowchart TD

```

## Code

<details>
<summary>ZX-81</summary>

```basic

```

</details>

<details>
<summary>C#</summary>

```csharp
```

</details>

<details>
<summary>Python</summary>

```python
import random

def tower_of_terror():
    pulse = 50
    room = 1

    while room <= 5 and pulse < 150:
        print(f"You are in room {room}.")
        print(f"Your pulse rate is {pulse}.")
        action = input("Press G to go or R to recover: ").upper()

        if action == 'G':
            room += 1
            pulse += random.randint(10, 40)
            print("You encountered something scary! Pulse increased.")
        elif action == 'R':
            pulse = max(50, pulse - 20)
            print("You rested and recovered some pulse.")

        if pulse >= 150:
            print("You jumped out of the tower in panic!")
            return

    if room > 5:
        print("Congratulations! You found the treasure!")
    else:
        print("Midnight struck. Game over.")

if __name__ == "__main__":
    tower_of_terror()
```

</details>

## Explanation

(game explanations)

## Challenges

1. **(challenges title)** : (challenge description)
2. **(challenges title)** : (challenge description)
3. **(challenges title)** : (challenge description)

## Copyright

These programs are adaptations of the original Usborne Computer Guides published in the 1980s. The books are free to download for personal or educational use from [Usborne's Computer and Coding Books](https://usborne.com/row/books/computer-and-coding-books). Programs and adaptations may not be used for commercial purposes.

Return to [Weird Computer Games](./readme.md).

```
