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

	/* $: menuOpts = isLoggedIn
		? menuItems.filter((item) => item.props.title !== 'Log in')
		: menuItems.filter((item) => item.props.title !== 'Log out'); Not working as expected at the moment */

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
	<h1 class="font-cr">CyberPong</h1>
	<nav>
		<ul class="list-unstyled">
			{#each menuItems as item}
				<li class="font-xe"><svelte:component this={item.component} {...item.props} /></li>
			{/each}
		</ul>
	</nav>
</div>


 

<style>
		main {
	  text-align: center;
	  margin-top: 50px;
	}

	/*@font-face {
		font-family: 'Cyberway Riders';
		src: url('/fonts/cyberway_riders/Cyberway Riders.otf') format('opentype');
	}

	@font-face {
		font-family: 'xenotron';
		src: url('/fonts/xenotron/XENOTRON.TTF') format('truetype');
	}

	.font-cr {
		font-family: 'Cyberway Riders', sans-serif;
	}

	.font-xe {
		font-family: 'xenotron', sans-serif;
	}*/
</style>
