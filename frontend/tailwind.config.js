/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      keyframes: {
      },
      animation: {
      }
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
      cyberpunk_dark: {    
            "primary": "#0c4383",
            "secondary": "#21a1b6",
            "accent": "#cb0c59",
            "neutral": "#06394c",
            "base-100": "#071e26",
            "info": "#0c4383",
            "success": "#36d399",
            "warning": "#fbbd23",
            "error": "#7b1346",
          },
      },
    "cupcake",
    "dark"
  ],
  },
}

