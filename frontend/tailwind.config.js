/** @type {import('tailwindcss').Config} */

import { transform } from 'typescript';

export default {
  content: ['./src/**/*.{html,ts,svelte}'],
  theme: {
    extend: {
      screens: {
       'desktop': {
          'raw': '(hover: hover)'
        }
      },
      fontSize: {
        'titlel': 'calc(2em + 4vh)',
        'titlep': 'calc(2em + 4vw)',
        'primaryl': 'calc(1em + 1.5vh)',
        'primaryp': 'calc(1em + 1.5vw)',
        'secodaryl': 'calc(1em + 0.5vh)',
        'secodaryp': 'calc(1em + 0.5vw)'
      },
      backgroundImage: {
        'darkFHD': "url('/background/dark/darkFHD.jpg')",
        'lightFHD': "url('/background/light/lightFHD.jpg')"
      },
      keyframes: {
        'fade-in': {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        'fade-out': {
          '0%': { opacity: '1' },
          '100%': { opacity: '0' },
        }
      },
      animation: {
        'fade-in': 'fade-in 2s ease-in-out forwards',
        'fade-out': 'fade-out 2s ease-in-out forwards',
        'fade-in-out': 'fade-in 2s ease-in-out, fade-out 2s 2s ease-in forwards',
      },
      dropShadow: {
        'neonpink-s': '0 0 10px rgba(234, 0, 217, 0.8)',
        'neonblue-s': '0 0 5px rgba(0, 184, 255, 1)',
        'neongreen-s': '0 0 5px rgba(0, 255, 159, 1)'
      },
      colors: {
        'neonred': '#FE0000',
        'neonyellow': '#FFF205',
        'neongreen': '#00ff9f',
        'neonblue': '#00b8ff',
        'neonpink': '#ea00d9'
      }
    }
  },
  plugins: [
    require("tailwindcss-animation-delay")
  ]
}

