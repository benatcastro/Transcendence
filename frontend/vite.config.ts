import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
<<<<<<< HEAD
	plugins: [sveltekit()]
=======
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
>>>>>>> login-api-implementation
});
