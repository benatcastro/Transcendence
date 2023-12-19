<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { goto } from '$app/navigation';
	import LogInModal from '$lib/components/LogInModal.svelte';
	import { loginStorage } from '$lib/stores/stores';
	import Button from '$lib/components/Button.svelte';

	let openPlayMenu: boolean = false;
	let isLoggedIn: boolean;
	let username: string = '';
	let audio;
	let menuItems = [
		{ component: Button, props: { title: 'Play', gradient: 'purple' } },
		{ component: LogInModal, props: { title: 'Log in', gradient: 'purple' } },
		{ component: Button, props: { title: 'Log out', gradient: 'purple' } },
		{ component: Button, props: { title: 'Profile', gradient: 'purple', href: '/profile' } },
		{ component: Button, props: { title: 'Leaderboard', gradient: 'purple', href: '/rank' } },
		{ component: Button, props: { title: 'Settings', gradient: 'purple', href: '/settings' } }
	];

	onMount(() => {
		audio.play();
	});

	/* $: menuOpts = isLoggedIn
		? menuItems.filter((item) => item.props.title !== 'Log in')
		: menuItems.filter((item) => item.props.title !== 'Log out'); Not working as expected at the moment */

	loginStorage.subscribe((loginSelection) => {
		if (browser && loginSelection) {
			goto(`http://localhost:8000/auth/${loginSelection}/login`);
		}
	});

	async function getUser() {
		if (!isLoggedIn) {
			const res = await fetch('http://localhost:8000/matchmaking/create-usr?mode=casual');
			if (!res.ok) {
				throw new Error('Error while creating user');
			}
			username = (await res.json()).user;
		}
		return username;
	}

	async function handlePlayClick(option: string) {
		try {
			if (option === 'ranked' && !isLoggedIn) {
				openPlayMenu = false;
				return;
			} else {
				await getUser();
			}
			await goto(`/matchmaking?mode=${option}&user=${username}`);
		} catch (e) {
			console.error(e.message);
		}
	}
</script>

<svelte:head>
	<title>CyberPong</title>
	<meta
		name="description"
		content="Immerse yourself in a neon-lit cyberpunk world with our online 3D Pong app. Engage in intense matches, customize your profile, and climb the leaderboards in this futuristic gaming universe."
	/>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" />
	<link
		rel="stylesheet"
		href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
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

<audio bind:this={audio} on:ended={audio.play} src="/sound/Half_Mystery.mp3" />

<h1>Main menu</h1>
<nav>
	<ul class="list-unstyled">
		{#each menuItems as item}
			<li><svelte:component this={item.component} {...item.props} /></li>
		{/each}
	</ul>
</nav>

{#if openPlayMenu}
	<div>
		<button on:click={() => handlePlayClick('casual')}>Casual</button>
		<button on:click={() => handlePlayClick('ranked')}>Ranked</button>
		<button on:click={() => (openPlayMenu = false)}>Go back</button>
	</div>
{/if}
