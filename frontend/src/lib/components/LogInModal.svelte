<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import { loginStorage } from '$lib/stores/stores';
	export let gradient: string = '',
		rounded: string = '';
</script>

<Modal title="Log in" {gradient} {rounded}>
	<div slot="modalBody">
		<MDBBtn on:click={() => loginStorage.set('42intra')}>
			<img src="/assets/oauth2/42_Logo.svg" alt="42 Network logo" class="w-25 h-25" />
		</MDBBtn>
		<MDBBtn on:click={() => loginStorage.set('google')}>
			<img src="/assets/oauth2/google.svg" alt="Google logo" class="w-25 h-25" />
		</MDBBtn>
	</div>
	<div slot="modalFooter">
		<MDBBtn color="secondary" on:click={() => toggle()}>Close</MDBBtn>
	</div>
</Modal>
