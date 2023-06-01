import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5003,
    host: true,
    proxy: {
      '/api': {
        target: 'http://api:5004', // connect to backend during development
        changeOrigin: true,
        secure: false,
      },
    },
  }
})
