<script lang="ts">
	import MDBContainer from 'mdbsvelte/src/MDBContainer.svelte';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import MDBModal from 'mdbsvelte/src/MDBModal.svelte';
	import MDBModalHeader from 'mdbsvelte/src/MDBModalHeader.svelte';
	import MDBModalBody from 'mdbsvelte/src/MDBModalBody.svelte';
	import MDBModalFooter from 'mdbsvelte/src/MDBModalFooter.svelte';
	export let title: string = '',
		color: string = '',
		gradient: string = '',
		rounded: string = '';

	let state: boolean = false;
	function toggle() {
		state = !state;
	}
</script>

<MDBContainer>
	<MDBBtn {color} {gradient} {rounded} on:click={() => toggle()}>
		{title}
	</MDBBtn>
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
