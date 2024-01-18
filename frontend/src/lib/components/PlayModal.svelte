<script lang="ts">
	import { goto } from '$app/navigation';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';

	export let gradient: string = '',
		rounded: string = '';

	let isLoggedIn: boolean = false; // TODO This will be a store so all urls can access it
	let username: string = '';
	let optionType: string = '';

	const socket = new WebSocket('wss://localhost/ws/matchmaking/');

	if (socket) {
		socket.onopen = (event) => {
			console.log('Conexion abierta:', event);
		};

		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			console.log('Mensaje recibido:', data);

			username = data.user.toString();
			socket.close();
			goto(`/matchmaking?mode=${optionType}&user=${username}`);
		};

		socket.onclose = (event) => {
			console.log('Conexion cerrada:', event);
		};
	}

	async function getUser() {
		if (!isLoggedIn) {
			// Ejemplo de creacion de partida casual
			if (socket)
			{
				socket.send(JSON.stringify({
					action: 'create',
					mode: 'casual',
				}));
			}
		}
		else
			console.log("TEST2");
		return username;
	}

	async function handlePlayClick(option: string) {
		try {
			if (option !== 'ranked' || isLoggedIn) {
				optionType = option;
				await getUser();

				//await goto(`/matchmaking?mode=${option}&user=${username}`);
			}
			else
				console.log("TEST3");
		} catch (e) {
			console.error("error_aherrero_____" + option + "____" + isLoggedIn);
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
