# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

# Vite + React Project

## Introduction

This is a Vite + React project template. It's set up with Vite for fast development and React for building the UI components. This README will guide you through the steps to run the project locally and configure the API gateway for local development.

## Prerequisites

Make sure you have the following installed on your machine:

- [Node.js](https://nodejs.org/)
- [Vite](https://vitejs.dev/)
- [React](https://reactjs.org/)

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine.

npm install

API Proxy Configuration (Important)

If you’re working with an API and want to avoid modifying CORS settings for local development, you can set up a proxy in your Vite configuration. This will allow API requests to be forwarded through your development server.

In the root of your project, the vite.config.js file includes the following proxy setup:

import { defineConfig } from 'vite';

export default defineConfig({
server: {
proxy: {
'/api': {
target: <API_GATEWAY_URL>
changeOrigin: true,
rewrite: (path) => path.replace(/^\/api/, ''),
},
},
},
});
• target: This should be the URL of your API Gateway endpoint. Replace it with the actual API endpoint you are working with.
• changeOrigin: true: This ensures the origin of the request is updated to the target URL, which is required for most APIs.
• rewrite: This rewrites the path to remove the /api prefix. So, if you make a request to /api/endpoint, it will forward the request to <API_Gateway_URL>.
npm run dev

Accessing Your API

Once the development server is running, you can access the API through http://localhost:3000/api/endpoint, and Vite will forward the request to your API Gateway.

Conclusion

That’s it! You’re now ready to develop your Vite + React application with a working API proxy setup. Make sure to adjust the proxy configuration if you need to change the API URL or use additional endpoints
