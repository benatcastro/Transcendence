<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	const mode = $page.url.searchParams.get('mode');
	const user = $page.url.searchParams.get('user');
	let rival: string = '';

	onMount(async () => {
		const res =
			mode == 'casual'
				? await fetch('http://localhost:8000/matchmaking/search?mode=casual&user=' + user)
				: await fetch('http://localhost:8000/matchmaking/search?mode=ranked&user=' + user);
		if (res.ok) {
			rival = (await res.json())['rival'];
		} else {
			console.error("fetch request didn't resolve");
			throw new Error("Couldn't fetch rival");
		}
	});

	addEventListener('beforeunload', () => {
		fetch('http://localhost:8000/matchmaking/delete?mode=' + mode + '&user=' + user);
	});
</script>

<svelte:head>
	<title>CyberPong - Matchmaking</title>
</svelte:head>

{#if rival}
	<p>Player {rival} wants to play!</p>
	<p><a href="../pong">Go to game</a></p>
{:else}
	<div class="spinner-border" role="status">
		<span class="visually-hidden">Loading...</span>
	</div>
{/if}
