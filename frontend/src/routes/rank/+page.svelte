<script lang="ts">
	import {onMount} from "svelte";

	let users = [];

	onMount(async () => {
		const response = await fetch("http://localhost:8000/api/users/");
		users = await response.json();
		users.sort((a, b) => a.username.localeCompare(b.username));
	});
</script>

<svelte:head>
	<title>CyberPong - Leaderboard</title>
	<meta
		name="description"
		content="Check the rankings and standings in our cyberpunk 3D Pong leaderboard. See where you stand among global players and strive to reach the top with your gaming skills."
	/>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
			rel="stylesheet"
	/>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
			rel="stylesheet"
	/>
</svelte:head>

<div class="d-flex flex-column flex-center">
	<h1>Ranking mockup</h1>
	<ul>
		{#each users as user}
			<li>{user.username} - {user.id}</li>
		{/each}
	</ul>
</div>