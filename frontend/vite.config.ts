import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	vite: {
		server: {
		  // Allow serving files from /app/static
		  // Adjust this path as needed for your project
		  allowFiles: ['/app/static']
		}
	  }
});
