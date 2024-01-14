<script lang="ts">
	import { goto } from '$app/navigation';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import Modal from '$lib/components/Modal.svelte';

	export let gradient: string = '',
		rounded: string = '';

	let isLoggedIn: boolean = false; // TODO This will be a store so all urls can access it
	let username: string = '';
	async function getUser() {
		if (!isLoggedIn) {
			const res = await fetch('django:8000/matchmaking/create-usr?mode=casual');
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
