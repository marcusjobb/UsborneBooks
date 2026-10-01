# UsborneBooks

## Länkar mellan sidor

Skriv interna länkar **relativt till källfilen**, med `.md` — som du skulle göra i VS Code eller på GitHub:

```markdown
[Annan sida](annan-sida.md)                    <!-- samma mapp -->
[Sida i annan avdelning](../avdelning/sida.md) <!-- annan avdelning -->
[Avdelningen](../avdelning/index.md)           <!-- en avdelnings index -->
[Rubrik](annan-sida.md#en-rubrik)              <!-- med ankare -->
```

Pluginet `site/src/plugins/doc-links.mjs` gör om dem till rätt absoluta URL:er vid bygget.

Skriv **inte** länkar utifrån den publicerade URL:en (`../annan-sida/`, `annan-sida/`) — de räknas från fel mapp och blir trasiga.

Kontrollera innan commit: `python3 _scripts/generate_docs.py` och sedan `npm run check:links` (bok-sidorna genereras från `computer_*`-mapparna). CI kör samma kontroll och stoppar deployen om någon länk är trasig.
