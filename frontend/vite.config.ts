import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';


export default defineConfig({
	plugins: [sveltekit()],
	ssr: {
		noExternal: ['three', 'postprocessing']
	},
	server: {
		port: 5173,
		strictPort: true,
		hmr: {
		  port: 5173,
		},
	  },
});
