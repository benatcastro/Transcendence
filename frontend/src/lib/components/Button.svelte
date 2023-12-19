<script lang="ts">
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import MDBContainer from 'mdbsvelte/src/MDBContainer.svelte';

	export let title: string,
		color: string = '',
		gradient: string = '',
		href: string = '',
		action: () => void = () => {};
</script>

<MDBContainer>
	<MDBBtn {color} {gradient} {href} on:click={action}>
		{title}
	</MDBBtn>
</MDBContainer>
