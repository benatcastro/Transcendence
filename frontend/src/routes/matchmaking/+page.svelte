<script lang="ts">
	import { page } from '$app/stores';
	import { json } from '@sveltejs/kit';
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	const mode = $page.url.searchParams.get('mode');
	const user = $page.url.searchParams.get('user');
	let rival: string;
	let room: string;
	let response_json;

	const socket = new WebSocket('wss://localhost/ws/matchmaking/');

	if (socket) {
		socket.onopen = (event) => {
			console.log('Conexion abierta:', event);
			socket.send(JSON.stringify({
				action: 'search',
				mode: 'casual',
				user: user.toString(),
			}));
		};

		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			console.log('Mensaje recibido:', data);


			rival = data.rival.toString();
			room = data.room.toString();
			socket.close();
			goto(`https://localhost/pong?user=${user}&rival=${rival}&room=${room}`);
		};

		socket.onclose = (event) => {
			console.log('Conexion cerrada:', event);
		};
	}

	// onMount(async () => {
		// const res = await fetch(`localhost:8000/matchmaking/search?mode=${mode}&user=${user}`);
		// if (res.ok) {
		// 	response_json = await res.json();
		// 	rival = response_json['rival'];
		// 	room = response_json['room'];
		// 	console.log(rival);
		// 	console.log(room);
		// 	goto(`http://localhost/pong?user=${user}&rival=${rival}&room=${room}`);
		// }
		// else {
		// 	console.error("fetch request didn't resolve");
		// 	throw new Error("Couldn't fetch rival");
		// }

		// socket.send(JSON.stringify({
		// 	action: 'search',
		// 	mode: 'casual',
		// 	user: user.toString(),
		// }));
	// });
	socket.send(JSON.stringify({
		action: 'search',
		mode: 'casual',
		user: user.toString(),
	}));

	addEventListener('beforeunload', () => {
		fetch(`localhost:8000/matchmaking/delete?mode=${mode}&user=${user}`);
	});
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