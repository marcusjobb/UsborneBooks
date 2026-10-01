// Relativa Markdown-länkar räknas från KÄLLFILEN — precis som i VS Code och på GitHub —
// och skrivs om till den absoluta URL som Astro publicerar sidan på.
//
// Varför: Astro publicerar docs/oop/records.md som /oop/records/ (en mapp). En relativ
// länk som "../datastrukturer/linq.md" räknas då av webbläsaren från /oop/records/
// och hamnar en nivå fel. Jekyll löste det åt oss; Astro gör det inte.
//
// Alla dessa fungerar, från docs/oop/records.md:
//   [x](poco-dto.md)   [x](poco-dto)   [x](poco-dto/)   [x](../oop/poco-dto.md#rubrik)
//   [x](polymorfism/)  → docs/oop/polymorfism/index.md
import fs from 'node:fs';
import path from 'node:path';
import { visit } from 'unist-util-visit';

// http:, mailto:, #ankare och /absoluta sökvägar lämnas orörda
const SKIP = /^([a-z][a-z0-9+.-]*:|#|\/)/i;

// Skiftlägeskänslig kontroll även på Windows — servern skiljer på Json och json
function isFileExact(p) {
  try {
    return fs.readdirSync(path.dirname(p)).includes(path.basename(p)) && fs.statSync(p).isFile();
  } catch {
    return false;
  }
}

/**
 * @returns {{ skip: true } | { url: string, file?: string, anchor?: string } | { broken: true }}
 */
export function resolveDocLink(href, fromFile, docsDir, base) {
  if (!href || SKIP.test(href)) return { skip: true };

  const [, rawPath, suffix = ''] = href.match(/^([^#?]*)([?#].*)?$/);
  let rel;
  try {
    rel = decodeURI(rawPath);
  } catch {
    return { broken: true };
  }

  const target = path.resolve(path.dirname(fromFile), rel);
  const candidates = /\.mdx?$/.test(rel) ? [target] : [`${target}.md`, path.join(target, 'index.md'), target];

  for (const candidate of candidates) {
    if (!isFileExact(candidate)) continue;

    const relToDocs = path.relative(docsDir, candidate).split(path.sep).join('/');
    if (relToDocs.startsWith('../')) return { broken: true };

    // Bilder, PDF:er och andra filer: länka direkt till filen
    if (!/\.mdx?$/.test(candidate)) return { url: `${base}/${encodeURI(relToDocs)}${suffix}` };

    const id = relToDocs.replace(/\.mdx?$/, '').replace(/(^|\/)index$/, '');
    const anchor = suffix.startsWith('#') ? decodeURIComponent(suffix.slice(1)) : undefined;
    return { url: `${base}/${id ? `${encodeURI(id)}/` : ''}${suffix}`, file: candidate, anchor };
  }

  return { broken: true };
}

/** remark-plugin. Options: { docsDir: absolut sökväg till docs/, base: '/programmering-csharp' } */
export default function remarkDocLinks({ docsDir, base = '' }) {
  const root = fs.realpathSync(docsDir);
  const cleanBase = base.replace(/\/$/, '');

  return (tree, file) => {
    if (!file.path) return;
    const from = fs.realpathSync(file.path);

    visit(tree, ['link', 'definition'], (node) => {
      const result = resolveDocLink(node.url, from, root, cleanBase);
      if (result.url) node.url = result.url;
      else if (result.broken) file.message(`Trasig länk: ${node.url}`, node);
    });
  };
}
