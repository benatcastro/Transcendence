<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	const mode = $page.url.searchParams.get('mode');
	const user = $page.url.searchParams.get('user');
	let rival: string;

	onMount(async () => {
		const res = await fetch(`http://localhost:8000/matchmaking/search?mode=${mode}&user=${user}`);
		if (res.ok) {
			rival = (await res.json())['rival'];
		} else {
			console.error("fetch request didn't resolve");
			throw new Error("Couldn't fetch rival");
		}
	});

	addEventListener('beforeunload', () => {
		fetch(`http://localhost:8000/matchmaking/delete?mode=${mode}&user=${user}`);
	});


	let socket;
	const roomName = 'mi_sala_de_pong';  // Nombre de la sala del juego
/*
	function connectWebSocket() {
	const socketURL = `ws://localhost:8000/ws/game/${roomName}/`; // Ajusta la URL según tu configuración
	socket = new WebSocket(socketURL);

	socket.onopen = (event) => {
		console.log('WebSocket conectado');
		// Puedes enviar mensajes aquí si es necesario
	};

	socket.onmessage = (event) => {
		const data = JSON.parse(event.data);
		console.log('Mensaje recibido desde el servidor:', data.message);
		// Maneja los mensajes recibidos del servidor aquí
	};

	socket.onclose = (event) => {
		console.log('WebSocket cerrado');
		// Maneja la lógica para reconectar o informar al usuario, si es necesario
	};
	}

	function sendMessageToServer() {
	const message = 'Hola desde el cliente';
	socket.send(JSON.stringify({ message }));
	}

	connectWebSocket();


*/

</script>

<svelte:head>
	<title>CyberPong - Matchmaking</title>

	<link
       href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
       rel="stylesheet"
	/>
	<link
		href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
		rel="stylesheet"
	/>
</svelte:head>

<div class="d-flex flex-center">
	{#if rival}
		<p>Player {rival} wants to play!</p>
		<p><a href="../pong">Go to game</a></p>
	{:else}
		<div class="spinner-border" role="status">
			<span class="visually-hidden">Loading...</span>
		</div>
	{/if}
</div>


  <!--<button on:click={sendMessageToServer}>Enviar mensaje al servidor</button>-->

