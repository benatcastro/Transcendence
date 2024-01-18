<script lang="ts">
	import { goto } from '$app/navigation';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';

	export let gradient: string = '',
		rounded: string = '';

	let isLoggedIn: boolean = false; // TODO This will be a store so all urls can access it
	let username: string = '';

	onMount(async () => {
		socket = new WebSocket('wss://django:8000/ws/matchmaking/');

		if (socket) {
			socket.onopen = (event) => {
				console.log('Conexion abierta:', event);
			};

			socket.onmessage = (event) => {
				const data = JSON.parse(event.data);
				console.log('Mensaje recibido:', data);

				// Haz algo con los datos recibidos.
			};

			socket.onclose = (event) => {
				console.log('Conexion cerrada:', event);
			};
		}
	});

	async function getUser() {
		if (!isLoggedIn) {
			// Ejemplo de creacion de partida casual
			if (socket)
			{
				socket.send(JSON.stringify({
					action: 'create',
					mode: 'casual',
					user: 'usuario123',
				}));
			}
			 const res = await fetch('localhost:8000/matchmaking/create-usr?mode=casual');
			 if (!res.ok) {
			 	throw new Error('Error while creating user');
			 }
			 else
			console.log("TEST");
			 username = (await res.json()).user;
		}
		else
			console.log("TEST2");
		return username;
	}

	async function handlePlayClick(option: string) {
		try {
			if (option !== 'ranked' || isLoggedIn) {
				await getUser();
				
				await goto(`/matchmaking?mode=${option}&user=${username}`);
			}
			else
				console.log("TEST3");
		} catch (e) {
			console.error("error_aherrero_____" + option + "____" + isLoggedIn + getUser());
		}
	}
</script>

<Modal title="Play" {gradient} {rounded}>
	<div slot="modalBody">
		<MDBBtn on:click={() => handlePlayClick('casual')}>
			<p>Casual</p>
		</MDBBtn>
		<MDBBtn on:click={() => handlePlayClick('ranked')}>
			<p>Ranked</p>
		</MDBBtn>
	</div>
	<div slot="modalFooter">
		<MDBBtn color="secondary" on:click={() => MDBBtn.toggle()}>Close</MDBBtn>
	</div>
</Modal>
