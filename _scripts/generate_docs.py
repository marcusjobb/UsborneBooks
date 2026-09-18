#!/usr/bin/env python3
"""
generate_docs.py — genererar docs/ från rotmapparnas källfiler.

Kör: python3 _scripts/generate_docs.py

För varje källfil:
  1. Extraherar titeln från första H1
  2. Lägger till Jekyll front matter (title, parent, nav_order)
  3. Wrappar innehållet i {% raw %}/{% endraw %} om filen innehåller {{
  4. Skriver till docs/<sektion>/<filnamn>.md

Lägg till nya böcker i BOOK_MAP nedan.
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR  = os.path.join(REPO_ROOT, "docs")

# Mappa: rotmapp → (docs-sektion, sidtitel i nav, nav_order för sektionen)
BOOK_MAP = {
    "computer_battlegames":  ("battlegames", "Computer Battlegames",  10),
    "computer_spacegames":   ("spacegames",  "Computer Spacegames",   20),
    "computer_spygames":     ("spygames",    "Computer Spy Games",    30),
    "creepy_computer_games": ("creepy",      "Creepy Computer Games", 40),
    "weird_computer_games":  ("weird",       "Weird Computer Games",  50),
}

SKIP_FILES = {"readme.md", "README.md"}


def extract_title(content: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def needs_raw_wrap(content: str) -> bool:
    return "{{" in content


def build_page(src_path: str, dest_dir: str, parent_title: str, nav_order: int) -> None:
    with open(src_path, encoding="utf-8") as f:
        body = f.read()

    fname   = os.path.basename(src_path)
    title   = extract_title(body, fname.replace("_", " ").replace(".md", "").title())

    front = (
        f"---\n"
        f'title: "{title}"\n'
        f"parent: {parent_title}\n"
        f"nav_order: {nav_order}\n"
        f"---\n"
    )

    if needs_raw_wrap(body):
        content = front + "\n{%- raw -%}\n" + body.rstrip("\n") + "\n{%- endraw -%}\n"
    else:
        content = front + "\n" + body

    dest_path = os.path.join(dest_dir, fname)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

    tag = " [raw]" if needs_raw_wrap(body) else ""
    print(f"  ✓ {os.path.relpath(dest_path, REPO_ROOT)}{tag}")


def main() -> None:
    for src_folder, (dest_section, parent_title, _) in BOOK_MAP.items():
        src_dir  = os.path.join(REPO_ROOT, src_folder)
        dest_dir = os.path.join(DOCS_DIR, dest_section)

        if not os.path.isdir(src_dir):
            print(f"⚠  {src_folder}/ saknas — hoppar över")
            continue

        files = sorted(
            f for f in os.listdir(src_dir)
            if f.endswith(".md") and f not in SKIP_FILES
        )

        print(f"\n{src_folder}/ → docs/{dest_section}/")
        for i, fname in enumerate(files, start=1):
            build_page(
                src_path   = os.path.join(src_dir, fname),
                dest_dir   = dest_dir,
                parent_title = parent_title,
                nav_order  = i,
            )

    print("\nKlart.")


if __name__ == "__main__":
    main()
