/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,ts,svelte}'],
  theme: {
    extend: {
      backgroundImage: {
        'dark4K': "url('/background/dark/dark4K.jpg')",
        'darkFHD': "url('/background/dark/darkFHD.jpg')",
        'darkHD': "url('/background/dark/darkHD.jpg')",
        'darkTBL': "url('/background/dark/darkTBL.jpg')",
        'darkMD': "url('/background/dark/darkMD.jpg')",
        'light4K': "url('/background/light/light4K.jpg')",
        'lightFHD': "url('/background/light/lightFHD.jpg')",
        'lightHD': "url('/background/light/lightHD.jpg')",
        'lightTBL': "url('/background/light/lightTBL.jpg')",
        'lightMD': "url('/background/light/lightMD.jpg')",
      },
    },
  },
  plugins: [],
}

