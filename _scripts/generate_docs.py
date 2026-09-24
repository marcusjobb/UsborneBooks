#!/usr/bin/env python3
"""
generate_docs.py — genererar docs/<sektion>/ från rotmapparnas källfiler.

Kör lokalt:  python3 _scripts/generate_docs.py
Körs också automatiskt av GitHub Actions innan Astro bygger.

Lägg till nya böcker i BOOK_MAP nedan — det är den enda raden du behöver ändra.
"""

import os
import re
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR  = os.path.join(REPO_ROOT, "docs")
LINKEDIN  = "https://www.linkedin.com/in/marcusmedina/"

# Mappa: rotmapp → (docs-sektion, sidtitel, nav_order, beskrivning, original-länk)
BOOK_MAP = {
    "computer_battlegames": (
        "battlegames", "Computer Battlegames", 10,
        "stridsbaserade spel för ZX-81, BBC Micro och Commodore 64 — moderniserade i C#.",
        "https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view?usp=sharing&resourcekey=0-v2liG0G60g8b7DXjJtDBXg",
    ),
    "computer_spacegames": (
        "spacegames", "Computer Spacegames", 20,
        "rymdspel för ZX-81, BBC Micro och Commodore 64 — moderniserade i C#.",
        "https://usborne.com/",
    ),
    "computer_spygames": (
        "spygames", "Computer Spy Games", 30,
        "spionspel för ZX-81, BBC Micro och Commodore 64 — moderniserade i C#.",
        "https://usborne.com/",
    ),
    "creepy_computer_games": (
        "creepy", "Creepy Computer Games", 40,
        "läskiga spel för ZX-81, BBC Micro och Commodore 64 — moderniserade i C#.",
        "https://usborne.com/",
    ),
    "weird_computer_games": (
        "weird", "Weird Computer Games", 50,
        "konstiga spel för ZX-81, BBC Micro och Commodore 64 — moderniserade i C#.",
        "https://usborne.com/",
    ),
}

SKIP_FILES = {"readme.md", "README.md"}


def extract_title(content: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def write_index(dest_dir: str, title: str, nav_order: int, description: str,
                original_url: str, game_count: int) -> None:
    os.makedirs(dest_dir, exist_ok=True)
    content = (
        f"---\n"
        f"title: {title}\n"
        f'description: "{title} — Usborne Revival"\n'
        f"nav_order: {nav_order}\n"
        f"has_children: true\n"
        f"---\n\n"
        f"# {title}\n\n"
        f"Originalboken av [Usborne Publishing]({original_url}).\n"
        f"Kodomvandling av [Marcus Ackre Medina]({LINKEDIN}).\n\n"
        f"{game_count} {description}\n"
    )
    with open(os.path.join(dest_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ index.md")


def write_game_page(src_path: str, dest_dir: str, parent_title: str,
                    nav_order: int) -> None:
    with open(src_path, encoding="utf-8") as f:
        body = f.read()

    fname = os.path.basename(src_path)
    title = extract_title(body, fname.replace("_", " ").replace(".md", "").title())

    # Fixa HTML-block så markdown (kodblock) inuti <details> renderas
    body = re.sub(r"<details(?!\s[^>]*markdown)", r'<details markdown="1"', body)

    front = (
        f"---\n"
        f'title: "{title}"\n'
        f"parent: {parent_title}\n"
        f"nav_order: {nav_order}\n"
        f"---\n"
    )

    page = front + "\n" + body

    with open(os.path.join(dest_dir, fname), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  ✓ {fname}")


def main() -> None:
    for src_folder, (dest_section, title, nav_order, description, original_url) in BOOK_MAP.items():
        src_dir  = os.path.join(REPO_ROOT, src_folder)
        dest_dir = os.path.join(DOCS_DIR, dest_section)

        if not os.path.isdir(src_dir):
            print(f"⚠  {src_folder}/ saknas — hoppar över")
            continue

        game_files = sorted(
            f for f in os.listdir(src_dir)
            if f.endswith(".md") and f not in SKIP_FILES
        )

        os.makedirs(dest_dir, exist_ok=True)
        print(f"\n{src_folder}/ → docs/{dest_section}/")

        write_index(dest_dir, title, nav_order, description, original_url,
                    len(game_files))

        for i, fname in enumerate(game_files, start=1):
            write_game_page(
                src_path     = os.path.join(src_dir, fname),
                dest_dir     = dest_dir,
                parent_title = title,
                nav_order    = i,
            )

        # Kopiera alla bildundermappar (t.ex. img/, eller creepys egennamngivna mapp)
        for entry in sorted(os.listdir(src_dir)):
            src_sub = os.path.join(src_dir, entry)
            if not os.path.isdir(src_sub):
                continue
            dest_sub = os.path.join(dest_dir, entry)
            if os.path.exists(dest_sub):
                shutil.rmtree(dest_sub)
            shutil.copytree(src_sub, dest_sub)
            print(f"  ✓ {entry}/ ({len(os.listdir(dest_sub))} filer)")

    print("\nKlart.")


if __name__ == "__main__":
    main()
