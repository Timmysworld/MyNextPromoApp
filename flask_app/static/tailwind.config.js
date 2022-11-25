/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./templates/*.html",
    "./index.html",
    // "./signup.html"
  ],
  theme: {
    extend: {
      colors:{
        'RBlue': '#041336',
      },
    },
  },
  plugins: [
    // require('@tailwindcss/forms')({
    //   strategy: 'base', // only generate global styles
    //   strategy: 'class' // only generate classes
    // })
  ],
}
