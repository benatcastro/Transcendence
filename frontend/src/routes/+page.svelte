<script lang="ts">
	import { goto } from '$app/navigation';
	let openPlayMenu: boolean = false;
	let isLoggedIn: boolean; //TODO cookie management?
	let menuItems = [
		{ name: 'Play', link: '/', action: () => (openPlayMenu = true) },
		{ name: 'Log in', link: '/', action: () => handleLoginClick() },
		{ name: 'Log out', link: '/', action: () => (isLoggedIn = false) },
		{ name: 'Profile', link: '/profile' },
		{ name: 'Leaderboard', link: '/leaderboard' },
		{ name: 'Settings', link: '/settings' }
	];

	$: menuOpts = isLoggedIn
		? menuItems.filter((item) => item.name !== 'Log in')
		: menuItems.filter((item) => item.name !== 'Log out');

	async function handleLoginClick() {
		console.log('Logging in...');
		return new Promise<void>((resolve, reject) => {
			//TODO fetch user info with promise
			//User authentication succeeded
			isLoggedIn = true;
            resolve();
			reject(new Error('Login failed'));
			//User authentication failed
		});
	}
	function handlePlayClick(option: string) {
		if (option === 'ranked' && !isLoggedIn) {
			handleLoginClick()
				.then(() => goto(`/matchmaking?mode=${option}`))
				.catch((e) => console.error(e.message));
		} else {
			goto(`/matchmaking?mode=${option}`);
		}
	}
</script>

<svelte:head>
	<title>Cyberpong</title>
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
