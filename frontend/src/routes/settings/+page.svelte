<script lang="ts">
	import { goto } from '$app/navigation';

	let menuOpts: string[] = ['Volume', 'Graphics', 'Game'];
</script>

<svelte:head>
	<title>Cyberpong - Settings</title>
</svelte:head>

<h2>Settings</h2>
<menu>
	<!-- Volume on click opens sub-menu for music and sound effects -->
	<!-- Graphics click opens sub-menu for animations and effects, as well as general graphics -->
	<!-- Game click opens sub-menu for skins and personalization -->
	{#each menuOpts as opt}
		<li>{opt}</li>
	{/each}
</menu>
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
