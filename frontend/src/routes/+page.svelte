<script lang="ts">
	import { goto } from '$app/navigation';
    let openPlayMenu: boolean = false;
    let isLoggedIn: boolean;

	function handlePlayClick(option: string) {
		goto(`/matchmaking?mode=${option}`);
	}
</script>

<svelte:head>
	<title>Cyberpong</title>
</svelte:head>

<h1>Main menu</h1>
<nav>
	<ul>
		<li><a on:click={() => openPlayMenu = true } href="/">Play</a></li>
		<li><a href="/">Log in</a></li>
		<li><a href="/">Log out</a></li>
		<li><a href="/profile">Profile</a></li>
		<li><a href="/leaderboard">Leaderboard</a></li>
		<li><a href="/settings">Settings</a></li>
	</ul>
</nav>

{#if openPlayMenu}
    <div class="play-menu">
        <button on:click={() => handlePlayClick("casual")}>Casual</button>
        <button on:click={() => handlePlayClick("ranked")}>Ranked</button>
        <button on:click={() => openPlayMenu = false}>Go back</button>
    </div>
{/if}