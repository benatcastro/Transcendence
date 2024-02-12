import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  ssr: {
    noExternal: ['three', 'postprocessing']
  },
  server: {
    hmr: {
      host: 'localhost',
      port: 443,
      protocol: 'wss'
    },
    port:443,
    strictPort: true,

  },
  proxy: {
    '/ws/game': {
      target: 'https://localhost/',
      ws: true,
      changeOrigin: true,
    },
  },
});