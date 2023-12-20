<script lang="ts">
	import { goto } from '$app/navigation';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import Modal from '$lib/components/Modal.svelte';

	export let gradient: string = '',
		rounded: string = '';

	let isLoggedIn: boolean; // TODO This will be a store so all urls can access it
	let username: string = '';
	async function getUser() {
		if (!isLoggedIn) {
			const res = await fetch('http://localhost:8000/matchmaking/create-usr?mode=casual');
			if (!res.ok) {
				throw new Error('Error while creating user');
			}
			username = (await res.json()).user;
		}
		return username;
	}

	async function handlePlayClick(option: string) {
		try {
			if (option !== 'ranked' || isLoggedIn) {
				await getUser();
				await goto(`/matchmaking?mode=${option}&user=${username}`);
			}
		} catch (e) {
			console.error(e.message);
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
		<MDBBtn color="secondary" on:click={() => toggle()}>Close</MDBBtn>
	</div>
</Modal>
