<script lang="ts">
	import { page } from '$app/stores';
	import { onDestroy } from 'svelte';
	import { randInt } from 'three/src/math/MathUtils';
	import { loadingPhrases } from '$lib/types';

	const mode = $page.url.searchParams.get('mode');
	let randPhrase: string = loadingPhrases[randInt(0, loadingPhrases.length - 1)];

	async function matchmaking() {
		//TODO change to the actual endpoints for both casual and ranked matches
		const res =
			mode == 'casual'
				? await fetch('https://pokeapi.co/api/v2/pokemon?limit=1')
				: await fetch('https://pokeapi.co/api/v2/pokemon?limit=1');
		if (res.ok) {
			//TODO must return the info of the lobby (?)
			return (await res.json()).results[0].name;
		}
		console.error("fetch request didn't resolve");
		throw new Error("Couldn't find an opponent, try again?");
	}

	const interval = setInterval(() => {
		randPhrase = loadingPhrases[randInt(0, loadingPhrases.length - 1)];
	}, 5000);
	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<svelte:head>
	<title>CyberPong - Matchmaking</title>
</svelte:head>

{#await matchmaking()}
	<div class="spinner-border" role="status">
		<span class="visually-hidden">Loading...</span>
	</div>
	<p>{randPhrase}</p>
{:then player}
	<p>{player} wants to play!</p>
{:catch error}
	<p>{error}</p>
	<p><a href="/">Go back</a></p>
{/await}
