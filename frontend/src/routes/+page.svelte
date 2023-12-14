<script lang="ts">
	import { goto } from '$app/navigation';

	let openPlayMenu: boolean = false;
	let loginSelection: string;
	let isLoggedIn: boolean;
	let username: string = '';
	let menuItems = [
		{ name: 'Play', link: '/', action: () => (openPlayMenu = true) },
		{ name: 'Log in', link: '/', action: () => (isLoggedIn = true) },
		{ name: 'Log out', link: '/', action: () => (isLoggedIn = false) },
		{ name: 'Profile', link: '/profile' },
		{ name: 'Leaderboard', link: '/leaderboard' },
		{ name: 'Settings', link: '/settings' }
	];

	$: menuOpts = isLoggedIn
		? menuItems.filter((item) => item.name !== 'Log in')
		: menuItems.filter((item) => item.name !== 'Log out');

	$: if (loginSelection != null) {
		goto(`http://localhost:8000/auth/${loginSelection}/login`);
	}

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
</svelte:head>

<h1>Main menu</h1>
<nav>
	<ul>
		{#each menuOpts as option}
			{#if option.link === '/'}
				<li><a on:click|preventDefault={option.action} href={option.link}>{option.name}</a></li>
			{:else}
				<li><a href={option.link}>{option.name}</a></li>
			{/if}
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
