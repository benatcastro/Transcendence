<script lang="ts">

	let user = undefined;
	async function loadProfile() {
		const response = await fetch("http://localhost:8000/users/me", {
			credentials: 'include',
		});

		const data = await response.json();
		console.log(data);

		user = data;
	}

	loadProfile();
</script>

<svelte:head>
	<title>CyberPong - Profile</title>
</svelte:head>


<h1>Profile mockup</h1>
{#if user === undefined}
	<h2>Loading user....</h2>
{:else}
	<h2>Welcome, {user.username}!</h2>
{/if}

