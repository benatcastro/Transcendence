import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  ssr: {
    noExternal: ['three', 'postprocessing']
  },
  server: {
    host: true,
    watch:{
        usePolling: true,
    },
    port:443,
    strictPort: true,
  },
  hmr: {
      protocol: 'wss',
      host: 'localhost',
      port: 443,
      path:'/ws/game',
    },
    optimizeDeps: {
      include: ['three', 'postprocessing']
    },

});