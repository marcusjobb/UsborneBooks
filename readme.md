# Usborne Computer Games Adaptation Project

## About the Project

This project is a modern adaptation of the classic Usborne computer books from the 1980s, specifically designed to bring their timeless games into the world of modern programming languages. These books originally featured games and programs for early computers like the ZX-81, BBC Micro, and Commodore 64, making programming accessible and fun for beginners.

The wonderful graphics are not included in this project, but the core gameplay and mechanics are preserved in the code adaptations. Check out the [original Usborne books](https://usborne.com/row/books/computer-and-coding-books) for the full experience.

By converting the games into contemporary languages like C#, Python, Java, and more, this project aims to:

1. **Preserve History**: Keep these classic programs alive for a new generation.
2. **Inspire New Coders**: Introduce programming concepts through fun, engaging games.
3. **Celebrate Nostalgia**: Revisit the joy of coding inspired by Usborne books.

## Books Covered

The project includes adaptations from the following books:

1. [**Computer Battlegames**](./computer_battlegames/readme.md)

Each game is provided with:

- **The original story**: Capturing the charm and imagination of the 1980s.
- **Code translations**: Written in multiple programming languages, starting with C#.
- **Beginner-friendly comments**: Explaining key concepts like random number generation and loops.
- **Suggestions for challenges**: Ideas to make the games harder or extend their functionality.

## Why Adapt These Books?

When I was in my teens, I learned programming on my ZX-81 and later on my C64, inspired by the books from Usborne. These books made coding fun and approachable, sparking a lifelong passion for programming. Revisiting and adapting these books is my way of preserving their legacy and sharing that magic with others.

## Copyright Notice

These programs are adaptations of the original Usborne Computer Guides published in the 1980s. The books are free to download for personal or educational use from [Usborne's Computer and Coding Books](https://usborne.com/row/books/computer-and-coding-books). Programs and adaptations may not be used for commercial purposes.

## How the Project is Structured

Each Usborne book has its own folder, and each game from the book is stored as a separate Markdown file within that folder. The Markdown files include:

- **The original story**
- **Code translations**: Starting with C#, Python, Java, Go and Rust.
- **Beginner-friendly explanations**
- **Challenge suggestions**

Additionally, code is wrapped in expandable `<details>` tags for easy readability.

## The process of adaptation

To start with I downloaded the original books from the Usborne website. I then read through the books and selected the games that I wanted to adapt.

But since I am lazy I used Google NotebookLM to extract the code and texts, ChatGPT is not vey good at reading code from images I noticed. Then I started to adapt the code to C#, python and Java. The rest was converted by either ChatGPT or Claude. I did cheat a little with CoPilot too, to comment the code.

Amazingly enough, what took most time was using ChatGPT to convert the code properly, it has a tendency to remove parts it doesn't feel is necessary. I had to go through the code several times to make sure it was correct.

### LLMs

- [NotebookLM](https://notebook.lm.goo.gle/) works well for extracting code and text from images.
- [Claude](https://claude.gg/) is good for converting code to other languages.
- [ChatGPT](https://app.inferkit.com/demo) is good for commenting code and writing text.
- [CoPilot](https://copilot.github.com/) is good for commenting code and writing text.

### Why I chose these languages

- **C#**: I am most familiar with C# and it is a good language for beginners. I love C#!
- **Python**: Python is a great language for beginners and is very popular. I'm learning it.
- **Java**: Java is a good language for beginners and is very popular. I like java, but I love C#.
- **Go**: Go is a good language for beginners and is very popular. A student used it for a project.
- **Rust**: Rust is a good language for beginners and is very popular. A student used it for a project.
- **C++**: I used that a long time ago... but at the moment my nephew is learning it, so I added it.

I did consider...

- JavaScript: I might add it later.
- Kotlin: But it's very similar to Java. So I skipped it.
- R: Not sure if it's a good language for games. I might add it later.
- PowerShell: Not for games but just for the fun of it. I might add it later.

## Contributing

If you’d like to adapt these games into other programming languages, add features, or improve the explanations, feel free to fork this repository and submit a pull request. Please ensure you credit the original Usborne books and provide a link to the official page.

Let me know if you have any questions or suggestions. Enjoy coding!

## Bugs and Issues

If you find any bugs or issues with the code, please open an issue on GitHub. I’ll do my best to address them as soon as possible.

## License

This project is licensed by same rules as the original Usborne books. It is free to download for personal or educational use. Programs and adaptations may not be used for commercial purposes.

## Acknowledgements

Special thanks to Usborne Publishing for creating the original Computer Guides and inspiring generations of programmers. Also, thanks to my students that are a constant inspiration for creating new content.

I love them so much for releasing these books for free. I hope they don't mind me adapting them.
