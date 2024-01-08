<script lang="ts">
	import { goto } from '$app/navigation';
	import {onMount} from "svelte";

	let menuOpts: string[] = ['Volume', 'Graphics', 'Game'];
	let volume: number = 1;

	function handleVolumeChange(e: Event) {
		volume = (e.target as HTMLInputElement).valueAsNumber / 100;
		let audio = document.querySelector('audio');

		audio.volume = volume;
	}

	onMount(() => {
		handleVolumeChange({
			target: {
				valueAsNumber: volume * 100
			} as any
		} as Event);
	});
</script>

<svelte:head>
	<title>CyberPong - Settings</title>
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
	<h2>Settings</h2>
	<menu class="d-flex flex-column p-2">
		<!-- Volume on click opens sub-menu for music and sound effects -->
		<!-- Graphics click opens sub-menu for animations and effects, as well as general graphics -->
		<!-- Game click opens sub-menu for skins and personalization -->
		{#each menuOpts as opt}
			{#if opt === 'Volume'}
				<p class="mx-auto">Volume</p>
				<input type="range" min="0" max="100" step="1" on:input={handleVolumeChange} />
			{:else}
				<button class="my-2">{opt}</button>
			{/if}
		{/each}
	</menu>
</div>
<a on:click={() => goto('/')} href="/">&lt;</a>

<style>
	/*
        Not decided yet, probably will try to simulate some electronic components
        and reflect how the electronics change as the settings do.

        I.E. You turn up the volume, and a bar connected to a sound system in the
        background goes up and changes on a gradient. Similar to electronic music
        components.
    */

	/* P.S.: Do not fucking touch my styles or I will eat your god damn eyeballs */
</style>
