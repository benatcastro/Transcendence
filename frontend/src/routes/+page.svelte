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
				throw new Error("Error while creating user");
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
	<meta
			name="description"
			content="Immerse yourself in a neon-lit cyberpunk world with our online 3D Pong app. Engage in intense matches, customize your profile, and climb the leaderboards in this futuristic gaming universe."
	/>
	<title>CyberPong</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
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
		<button on:click={() => openPlayMenu = false}>Go back</button>
	</div>
{/if}

<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#logInModal">Log in</button>
<div class="modal fade" id="logInModal" tabindex="-1" role="dialog" aria-labelledby="logInModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title" id="logInModalLabel">Log in</h3>
      </div>
      <div class="modal-body d-flex flex-column">
		  <button class="btn btn-lg btn-light" on:click={() => loginSelection = '42intra'}>
			<img src="/oauth2/42_Logo.svg" alt="42 Network logo" class="w-25 h-25" />
		</button>
		<button class="btn btn-lg btn-light" on:click={() => loginSelection = 'google'}>
			<img src="/oauth2/google.svg" alt="Google logo" class="w-25 h-25" />
		</button>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary center-block" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>