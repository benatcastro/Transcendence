<script lang="ts">
	let images: string[][] = [
		['Aingeru Álvarez', '/assets/team/aingeru.jpg'],
		['Ander Herrero', '/assets/team/ander.jpg'],
		['Antonio del Corral', '/assets/team/antonio.jpg'],
		['Beñat Castro', '/assets/team/beñat.jpg'],
		['Cristian Bustamante', '/assets/team/cristian.jpg']
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

<div class="d-flex flex-column align-items-center justify-content-evenly vh-100">
	<h2>Meet the team behind CyberPong</h2>
	<div class="container">
		{#each images as image}
			<div class="card">
				<div class="wrapper">
					<img src="https://assets.codepen.io/527512/zelda_cover-image.webp" class="cover-image" alt="cover image" />
				</div>
				<img src={image[1]} class="character" alt={image[0]} />
			</div>
		{/each}
    </div>
</div>

<style>
	:root {
		--card-height: 15vh;
		--card-width: calc(var(--card-height) / 1.5);
	}

	* {
		box-sizing: border-box;
	}

	.card {
		width: var(--card-width);
		height: var(--card-height);
		position: relative;
		display: flex;
		justify-content: center;
		align-items: flex-end;
		padding: 0 36px;
		perspective: 2500px;
		margin: 0 50px;
	}

	.cover-image {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.wrapper {
		transition: all 0.5s;
		position: absolute;
		width: 100%;
		z-index: -1;
	}

	.card:hover .wrapper {
		transform: perspective(900px) translateY(-5%) rotateX(25deg) translateZ(0);
		box-shadow: 2px 35px 32px -8px rgba(0, 0, 0, 0.75);
		-webkit-box-shadow: 2px 35px 32px -8px rgba(0, 0, 0, 0.75);
		-moz-box-shadow: 2px 35px 32px -8px rgba(0, 0, 0, 0.75);
	}

	.wrapper::before,
	.wrapper::after {
		content: "";
		opacity: 0;
		width: 100%;
		height: 80px;
		transition: all 0.5s;
		position: absolute;
		left: 0;
	}

	.wrapper::before {
		top: 0;
		height: 100%;
		background-image: linear-gradient(
			to top,
			transparent 46%,
			rgba(12, 13, 19, 0.5) 68%,
			rgba(12, 13, 19) 97%
		);
	}

	.wrapper::after {
		bottom: 0;
		opacity: 1;
		background-image: linear-gradient(
			to bottom,
			transparent 46%,
			rgba(12, 13, 19, 0.5) 68%,
			rgba(12, 13, 19) 97%
		);
	}

	.card:hover .wrapper::before,
	.wrapper::after {
		opacity: 1;
	}

	.card:hover .wrapper::after {
		height: 120px;
	}

	.character {
		width: 100%;
		opacity: 0;
		transition: all 0.5s;
		position: absolute;
		z-index: -1;
	}

	.card:hover .character {
		opacity: 1;
		transform: translate3d(0%, -30%, 100px);
	}
</style>
