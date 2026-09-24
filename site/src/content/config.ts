import { defineCollection, z } from 'astro:content';

const docs = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    parent: z.string().optional(),
    nav_order: z.coerce.number().optional(),
    has_children: z.boolean().optional(),
    layout: z.string().optional(),
  }),
});

export const collections = { docs };
