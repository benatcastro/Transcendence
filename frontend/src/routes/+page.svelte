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

	let username: string = "";

	$: menuOpts = isLoggedIn
		? menuItems.filter((item) => item.name !== 'Log in')
		: menuItems.filter((item) => item.name !== 'Log out');

	async function handleLoginClick() {
		console.log('Logging in...');
		//TODO fetch users info with promise
		//TODO User authentication succeeded
		const logged = await fetch('https://pokeapi.co/api/v2/pokemon?limit=1');
		if (!logged.ok) {
			//TODO User authentication failed
			return new Error('Incorrect username or password');
		}
		isLoggedIn = true;
		return (await logged.json()).results[0].name; //TODO mock users info
	}

	async function handleIsLoggedUsername(isLoggedIn: boolean) {
		if (!isLoggedIn) {
			//TODO change to the actual endpoints for both casual and ranked matches
			const res = await fetch('http://10.13.7.2:8000/matchmaking/?mode=casual');
			if (!res.ok) {
				//TODO must return the info of the lobby (?)
				console.error("fetch request didn't resolve");
				throw new Error("Couldn't find an opponent, try again?");
			}
			username = (await res.json()).user;
			console.log(username);
		}
		return (username);
	}

	function handlePlayClick(option: string) {
		if (option === 'ranked' && !isLoggedIn) {
			//TODO Temporary rejection for testing
			console.error('You are not logged in');
			handleLoginClick()
				.then(() => goto(`/matchmaking?mode=${option}&user=${username}`))
				.catch((e) => console.error(e.message));
		}
		else {
			console.log('Im here');
			handleIsLoggedUsername(isLoggedIn)
				.then(() => goto(`/matchmaking?mode=${option}&user=${username}`))
				.catch((e) => console.error(e.message));
		}
	}
</script>

<svelte:head>
	<meta
		name="description"
		content="Immerse yourself in a neon-lit cyberpunk world with our online 3D Pong app. Engage in intense matches, customize your profile, and climb the leaderboards in this futuristic gaming universe."
	/>
	<title>CyberPong</title>
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
