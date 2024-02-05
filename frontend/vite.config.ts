import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';


export default defineConfig({
	plugins: [sveltekit()],
	ssr: {
		noExternal: ['three', 'postprocessing']
	},

	server: {
		port:443,
		strictPort: true,
		watch: {
			usePolling: true,
		  },
	  },
	  proxy: {
		'/ws': {
		  target: 'https://localhost:442',
		  ws: true,
		  changeOrigin: true,
		  Clientport: 442,
		},
	},
});
