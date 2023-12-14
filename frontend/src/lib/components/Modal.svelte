<script lang="ts">
	import MDBContainer from 'mdbsvelte/src/MDBContainer.svelte';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import MDBModal from 'mdbsvelte/src/MDBModal.svelte';
	import MDBModalHeader from 'mdbsvelte/src/MDBModalHeader.svelte';
	import MDBModalBody from 'mdbsvelte/src/MDBModalBody.svelte';
	import MDBModalFooter from 'mdbsvelte/src/MDBModalFooter.svelte';
	export let modalTitle: any,
		modalBody: any,
		modalFooter: any,
		modalBtn: { title: string; color?: string };

	let state = false;
	function toggle() {
		state = !state;
	}
</script>

<MDBContainer>
	<MDBBtn color={modalBtn.color} on:click={() => toggle()}>{modalBtn.title}</MDBBtn>
	<MDBModal isOpen={state} toggle={() => toggle()}>
		<MDBModalHeader toggle={() => toggle()}>
			<slot name="modalTitle" />
		</MDBModalHeader>
		<MDBModalBody>
			<slot name="modalBody" />
		</MDBModalBody>
		<MDBModalFooter>
			<slot name="modalFooter" />
		</MDBModalFooter>
	</MDBModal>
</MDBContainer>
