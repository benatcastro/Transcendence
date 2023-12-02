# index tsx

- const server = Bun.serve({ ... });: This line initializes the server using Bun.serve() and sets it to listen on port 3000.

- port: 3000,: Specifies that the server should listen on port 3000.

- fetch(req) { ... }: Defines a function that will handle all incoming HTTP requests. When a request comes in, it returns a new HTTP response with the text "Bun!".

- return new Response(Bun!);: Creates a new HTTP response object with the text "Bun!".

- console.log(Listening on localhost:${server.port} ...);: Logs a message to the console, indicating that the server is listening. It uses template literals to insert the port number dynamically.

- import { renderToReadableStream } from "react-dom/server";: Imports the function renderToReadableStream from the react-dom/server package for server-side React rendering.

- import Pokemon from "./components/Pokemon";: Imports a React component named Pokemon from a relative file path.

- Bun.serve({ ... });: Uses the Bun.serve() method to set up an HTTP server. It includes an asynchronous fetch function to handle incoming HTTP requests.

- async fetch(request) { ... }: An asynchronous function that will be triggered for each HTTP request coming to the server.

- const stream = await renderToReadableStream(<Pokemon />);: Asynchronously renders the Pokemon React component to a readable stream.

- return new Response(stream, { ... });: Returns a new HTTP Response object with the readable stream and sets the "Content-Type" header to "text/html".

- console.log("Listening ...");: Outputs a message to the console indicating that the server is listening for incoming requests.
# Run bun 
- bun --watch index.tsx

## Building Dynamic Routes with a Pokémon Twist

- Navigating to /pokemon will trigger a fetch request to the Pokémon API, rendering the results as a clickable list of anchor tags.

- Clicking any of these anchors takes you to /pokemon/[pokemonName], where a specific Pokémon is fetched, server-side rendered (SSR), and then streamed back to your client.

## A lot is going on here. Let's dive deeper into the interesting pieces.

- Initialize HTTP Server with Bun: The Bun.serve() method sets up an HTTP server and specifies an asynchronous fetch function to handle incoming requests, effectively acting as the entry point for all HTTP traffic.

- Route for All Pokémon: When the URL path is /pokemon, the server fetches a list of Pokémon from an external API and renders a PokemonList React component to HTML. This HTML is then sent back to the client.

- Route for Specific Pokémon: The code uses a Regular Expression to match URL paths that specify a particular Pokémon's name (e.g., /pokemon/pikachu). If such a path is detected, the server fetches details for that specific Pokémon and renders it using the Pokemon React component.

- Server-Side React Rendering: For both the general and specific Pokémon routes, the renderToReadableStream function converts React components to a readable stream, which is then returned as an HTML response.

- Error Handling: The code includes specific handling for 404 errors. If a Pokémon is not found in the API or if the URL doesn't match any expected routes, a "Not Found" message is returned with a 404 status code.

# Package jackson

- add dev ando production script
"scripts": {
    "start": "bun run index.tsx",
    "dev": "bun --watch index.tsx"
},
```sh
bun run dev
```
or
```sh
bun run start
```

# Build and compile bun 
```sh
bun build ./cli.ts --compile --outfile mycli
$ ./mycli
Hello world!
bun build index.tsx --outfile out/frontend --compile
```

Note — Currently, the --compile flag can only accept a single entrypoint at a time and does not support the following flags:

--outdir — use outfile instead.
--external
--splitting
--public-path

# create project using bun with svelte

- https://bun.sh/guides/ecosystem/sveltekit
