<script lang="ts">
	async function loadProfile() {
		const response = await fetch("http://localhost:8000/users");

		const data = await response.json();
		console.log(data);

		return data;
	}

	loadProfile();
</script>

<svelte:head>
	<title>CyberPong - Profile</title>
</svelte:head>

<h1>Profile mockup</h1>
