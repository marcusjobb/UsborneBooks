import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import expressiveCode from 'astro-expressive-code';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';

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
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
    ],
    syntaxHighlight: false,
  },
});
