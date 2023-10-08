/** @type {import('tailwindcss').Config} */

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
      colors: {
        'neonred': '#FE0000',
        'neonyellow': '#FFF205',
        'neongreen': '#00ff9f',
        'neonblue': '#00b8ff',
        'neonpink': '#ea00d9'
      }
    }
  },
  plugins: []
}

