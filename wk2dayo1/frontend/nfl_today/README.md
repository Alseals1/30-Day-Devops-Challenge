![Let's Play Football](https://www.pexels.com/photo/football-player-grayscale-photo-2253884/)

<h3 align="center">Football Today</h3>
<div>
<h2> Introduction</h2>

<p align="center">This is a Vite + React project template. It's set up with Vite for fast development and React for building the UI components. This README will guide you through the steps to run the project locally and configure the API gateway for local development.</p>
</div>
<h2> Prerequisites </h2>

Make sure you have the following installed on your machine:

- [Node.js](https://nodejs.org/)
- [Vite](https://vitejs.dev/)
- [React](https://reactjs.org/)
- [TailwindCSS](https://tailwindcss.com)

## Getting Started

1. Get a free API Key at [https://serpapi.com/users/sign_in](https://serpapi.com/users/sign_in)
2. Clone the repo

   ```sh
   git clone https://github.com/Alseals1/30-Day-Devops-Challenge.git
   ```

3. Install NPM packages

- npm
  ```sh
  npm install
  ```

4. Enter your API Gateway URL in `vite.config.js`
   ```js
   const API_Gatway_URL = "https://APIGATEWAY-api.us.whatever.amazon.com/dev";
   ```

<h1>API Proxy Configuration (Important)</h1>

<p>If you’re working with an API and want to avoid modifying CORS settings for local development, you can set up a proxy in your Vite configuration. This will allow API requests to be forwarded through your development server.</p>

<p>In the root of your project, the vite.config.js file includes the following proxy setup:</p>

```js
    import { defineConfig } from 'vite';

    export default defineConfig({
        server: {
            roxy: {
                '/api': {
                    target: <API_GATEWAY_URL>
                        changeOrigin: true,
                        rewrite: (path) => path.replace(/^\/api/''),
                        },
                    },
            },
        });

```

- target: This should be the URL of your API Gateway endpoint. Replace it with the actual API endpoint you are working with.
- changeOrigin: true: This ensures the origin of the request is updated to the target URL, which is required for most APIs.
- rewrite: This rewrites the path to remove the /api prefix. So, if you make a request to /api/endpoint, it will forward the request to <API_Gateway_URL>.

```sh
npm run dev
```

<h1>Accessing Your API</h1>

<p> Once the development server is running, you can access the API through http://localhost:{your_local_host}/api/endpoint, and Vite will forward the request to your API Gateway.</p>

<h2>Conclusion</h2>

<p>That’s it! You’re now ready to develop your Vite + React application with a working API proxy setup. Make sure to adjust the proxy configuration if you need to change the API URL or use additional endpoints</p>
