import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import expressiveCode from 'astro-expressive-code';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';

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
      parent.children[index] = { type: 'html', value: `<pre class="mermaid"></pre>` };
    });
  };
}

export default defineConfig({
  site: 'https://marcusjobb.github.io',
  base: '/UsborneBooks',
  output: 'static',
  integrations: [
    expressiveCode({
      themes: ['github-dark', 'github-light'],
      defaultProps: { wrap: false },
    }),
    sitemap(),
  ],
  markdown: {
    remarkPlugins: [remarkMermaid],
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
    ],
    syntaxHighlight: false,
  },
});
