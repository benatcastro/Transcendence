<script lang="ts">
	let images: string[][] = [
		['Aingeru Álvarez', ''],
		['Ander Herrero', ''],
		['Antonio del Corral', ''],
		['Beñat Castro', ''],
		['Cristian Bustamante', '']
	];
</script>

<svelte:head>
	<title>CyberPong - Meet the team</title>
	<meta
		name="description"
		content="Get to know the passionate minds behind our futuristic cyberpunk 3D Pong web app. Discover the talented team dedicated to bringing you an immersive gaming experience."
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

<h2>Meet the team behind CyberPong</h2>
{#each images as image}
	<section>
		<img src={image[1]} alt={image[0]} />
		<p>Description for {image[0]}</p>
	</section>
{/each}

<style>
	/*
        The names are organized alphabetically, which I think makes sense if
        it supposed to simulate a futuristic terminal screen.
    */

	/*
        I will create a consistent background simulating the screen of some
        futuristic-like terminal, with a preview of everyone in the team, when
        hovering over one of the sections, it will display the whole paragraph
        with the general contribution of each one.
    */

	/* P.S.: Do not fucking touch my styles or I will eat your god damn eyeballs */
</style>
