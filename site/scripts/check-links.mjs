// Hittar trasiga interna länkar i docs/ — samma upplösning som bygget använder
// (site/src/plugins/doc-links.mjs), plus kontroll av #ankare mot rubrikerna i målfilen.
//
//   npm run check:links            → skriver ut trasiga länkar, exit 1 om någon finns
//   npm run check:links -- --warn  → skriver ut, men exit 0
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import { visit } from 'unist-util-visit';
import { toString } from 'mdast-util-to-string';
import GithubSlugger from 'github-slugger';
import { resolveDocLink } from '../src/plugins/doc-links.mjs';

const docsDir = fileURLToPath(new URL('../../docs', import.meta.url));
const IGNORE = new Set(['vendor', '.bundle', 'node_modules']);
const parser = unified().use(remarkParse).use(remarkGfm);

function* markdownFiles(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (IGNORE.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* markdownFiles(full);
    else if (/\.mdx?$/.test(entry.name)) yield full;
  }
}

function parse(file) {
  // Frontmatter byts mot lika många tomrader, så att radnumren stämmer med filen
  const text = fs.readFileSync(file, 'utf8').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, (fm) => fm.replace(/[^\n]/g, ''));
  return parser.parse(text);
}

// Samma slugs som rehype-slug ger rubrikerna på den byggda sidan
const slugCache = new Map();
function slugsOf(file) {
  if (!slugCache.has(file)) {
    const slugger = new GithubSlugger();
    const slugs = new Set();
    visit(parse(file), 'heading', (node) => slugs.add(slugger.slug(toString(node))));
    slugCache.set(file, slugs);
  }
  return slugCache.get(file);
}

const broken = [];
for (const file of markdownFiles(docsDir)) {
  visit(parse(file), ['link', 'definition'], (node) => {
    const where = `${path.relative(docsDir, file).split(path.sep).join('/')}:${node.position?.start.line}`;

    if (node.url.startsWith('#')) {
      const anchor = decodeURIComponent(node.url.slice(1));
      if (anchor && !slugsOf(file).has(anchor)) broken.push(`${where}  ${node.url}  (ankaret finns inte på sidan)`);
      return;
    }

    const result = resolveDocLink(node.url, file, docsDir, '');
    if (result.broken) broken.push(`${where}  ${node.url}  (filen finns inte)`);
    else if (result.anchor && result.file && !slugsOf(result.file).has(result.anchor))
      broken.push(`${where}  ${node.url}  (ankaret finns inte i målfilen)`);
  });
}

for (const line of broken) console.log(line);
console.log(`\n${broken.length} trasiga länkar`);
if (broken.length && !process.argv.includes('--warn')) process.exit(1);
