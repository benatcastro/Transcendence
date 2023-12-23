<script lang="ts">
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import MDBContainer from 'mdbsvelte/src/MDBContainer.svelte';

	export let title: string,
		color: string = '',
		gradient: string = '',
		href: string = '',
		rounded: string = '',
		action: () => void = () => {};
</script>

<MDBContainer>
	<MDBBtn {color} {gradient} {rounded} {href} on:click={action}>
		{title}
	</MDBBtn>
</MDBContainer>
