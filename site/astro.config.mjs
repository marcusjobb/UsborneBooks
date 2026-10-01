import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import expressiveCode from 'astro-expressive-code';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import { fileURLToPath } from 'node:url';
import remarkDocLinks from './src/plugins/doc-links.mjs';

const base = '/UsborneBooks';

// Converts `mermaid blocks to <pre class="mermaid"> before expressive-code sees them
function remarkMermaid() {
  return (tree) => {
    const hits = [];
    function walk(node, parent, index) {
      if (node.type === 'code' && node.lang === 'mermaid') hits.push({ node, parent, index });
      if (node.children) node.children.forEach((c, i) => walk(c, node, i));
    }
    walk(tree, null, 0);
    hits.reverse().forEach(({ node, parent, index }) => {
      // Escapa: annars tolkas <br/>, <|-- och liknande i diagramkoden som HTML-taggar
      const code = node.value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      parent.children[index] = { type: 'html', value: `<pre class="mermaid">${code}</pre>` };
    });
  };
}

export default defineConfig({
  site: 'https://marcusjobb.github.io',
  base,
  output: 'static',
  integrations: [
    expressiveCode({
      themes: ['github-dark', 'github-light'],
      defaultProps: { wrap: false },
    }),
    sitemap(),
  ],
  markdown: {
    remarkPlugins: [
      remarkMermaid,
      // Relativa länkar räknas från källfilen och blir absoluta URL:er (se pluginet)
      [remarkDocLinks, { docsDir: fileURLToPath(new URL('../docs', import.meta.url)), base }],
    ],
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
    ],
    syntaxHighlight: false,
  },
});
