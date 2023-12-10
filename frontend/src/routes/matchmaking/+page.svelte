<script lang="ts">
	import { page } from '$app/stores';
	import { onDestroy, onMount } from 'svelte';
	//import { randInt } from 'three/src/math/MathUtils';
	//import { loadingPhrases } from '$lib/types';

	const mode = $page.url.searchParams.get('mode');
	const user = $page.url.searchParams.get('user');
	//let randPhrase: string = loadingPhrases[randInt(0, loadingPhrases.length - 1)];

	let rival:string = "";
	function randomIntFromInterval(min: number, max: number)
	{
  		return Math.floor(Math.random() * (max - min + 1) + min)
	}

	async function matchmaking() {
		//TODO change to the actual endpoints for both casual and ranked matches
		const res =
			mode == 'casual'
				? await fetch('http://localhost:8000/matchmaking/search?mode=casual&user=' + user)
				: await fetch('http://localhost:8000/matchmaking/search?mode=ranked&user=' + user);
		if (res.ok) {
			//TODO must return the info of the lobby (?)
			rival = (await res.json())["rival"];
			return rival;
		}
		console.error("fetch request didn't resolve");
		throw new Error("Couldn't find an opponent, try again?");
	}

	// const interval = setInterval(() => {
	// 	randPhrase = loadingPhrases[randInt(0, loadingPhrases.length - 1)];
	// }, 5000);
	// onDestroy(() => {
	// 	clearInterval(interval);
	// });


	// window.onbeforeunload = () => {
	// 	destroyWindow()
	// };

	onDestroy(destroyWindow)
	
	function destroyWindow() {
		fetch('http://localhost:8000/matchmaking/delete?mode=casual&user=' + user)
	}

</script>

<svelte:head>
	<title>CyberPong - Matchmaking</title>
</svelte:head>

{#await matchmaking()}
	<div class="spinner-border" role="status">
		<span class="visually-hidden">Loading...</span>
	</div>
{:then player}
	<p>{player} wants to play!</p>
	<p><a href="../pong">Go to game</a></p>
{:catch error}
	<p>{error}</p>
	<p><a href="/">Go back</a></p>
{/await}
