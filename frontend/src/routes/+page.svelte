<script lang="ts">
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import { loginStorage } from '$lib/stores/stores';
	import PlayModal from '$lib/components/PlayModal.svelte';
	import Button from '$lib/components/Button.svelte';

	let menuItems = [
		{ component: PlayModal, props: { gradient: 'aqua' } },
		{
			component: Button,
			props: { title: 'Profile', gradient: 'aqua', href: '/profile' }
		},
		{
			component: Button,
			props: { title: 'Leaderboard', gradient: 'aqua', href: '/rank' }
		}
	];

	loginStorage.subscribe((loginSelection) => {
		if (browser && loginSelection) {
			goto(`http://localhost:8000/auth/${loginSelection}/login`);
		}
	});
</script>

<svelte:head>
	<title>CyberPong</title>
	<meta
		name="description"
		content="Immerse yourself in a neon-lit cyberpunk world with our online 3D Pong app. Engage in intense matches, customize your profile, and climb the leaderboards in this futuristic gaming universe."
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
	<nav>
		<ul class="list-unstyled d-flex flex-column align-items-center">
			<li class="font-xe btn-lg w-100">
				<div class="card mb-3 p-5 m-3 btn cyberpunk-background">
					<svelte:component this={menuItems[0].component} {...menuItems[0].props} />
				</div>
			</li>
			<li class="d-flex justify-content-around w-100">
				<div class="card mb-3 p-5 m-3 btn cyberpunk-background">
					<svelte:component this={menuItems[1].component} {...menuItems[1].props} />
				</div>
				<div class="card mb-3 p-5 m-3 btn cyberpunk-background">
					<svelte:component this={menuItems[2].component} {...menuItems[2].props} />
				</div>
			</li>
		</ul>
	</nav>
</div>

<style>
	.cyberpunk-background {
		background: linear-gradient(90deg, rgba(204,0,255,0.8) 35%, rgba(0,255,255,0.8) 100%);
		border: 1px solid #00ffff;
		box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
	}

	.btn:hover {
		background-color: rgba(0, 255, 255, 0.5);
		border-color: #00ffff;
		box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
	}

	.btn {
		background-color: transparent;
		border: 1px solid #00ffff;
		color: #00ffff;
		text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
	}

	main {
		text-align: center;
		margin-top: 50px;
	}

	@font-face {
		font-family: 'xenotron';
		src: url('/fonts/xenotron/XENOTRON.TTF') format('truetype');
	}

	.font-xe {
		font-family: 'xenotron', sans-serif;
	}
</style>
