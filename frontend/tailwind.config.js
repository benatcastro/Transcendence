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
        'primaryl': 'calc(0.3em + 3vh)',
        'primaryp': 'calc(0.3em + 3vw)',
        'secodaryl': 'calc(0.3em + 2vh)',
        'secodaryp': 'calc(0.3em + 2vw)'
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

