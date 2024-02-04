<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	const mode = $page.url.searchParams.get('mode');
	const user = $page.url.searchParams.get('user');
	let rival: string;
	let room: string;
	let response_json;

	onMount(async () => {
		const res = await fetch(`http://localhost/matchmaking/search?mode=${mode}&user=${user}`);
		if (res.ok) {
			response_json = await res.json();
			rival = response_json['rival'];
			room = response_json['room'];
			goto(`https://localhost/pong?user=${user}&rival=${rival}&room=${room}`);
		}
		else {
			console.error("fetch request didn't resolve");
			throw new Error("Couldn't fetch rival");
		}
	});

	addEventListener('beforeunload', () => {
		fetch(`http://localhost/matchmaking/delete?mode=${mode}&user=${user}`);
	});
</script>

<svelte:head>
	<title>CyberPong - Matchmaking</title>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
			rel="stylesheet"
	/>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
			rel="stylesheet"
	/>
</svelte:head>

<div class="d-flex flex-center screen-container">
  <p class="cyber-text side-text">In the year 2077, the world is ruled by corporations...</p> <!-- Cyberpunk paragraph at the start -->
    {#if rival}
      <p>Player {rival} wants to play!</p>
      <p><a href="../pong">Go to game</a></p>
    {:else}
    {/if}
    <div class="spinner-border" role="status" />
  <p class="cyber-text side-text">The only hope for humanity is pong... for.. some reason....</p> <!-- Cyberpunk paragraph at the end -->
</div>

<style>
	.side-text {
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		width: 30%;
		text-align: justify;
	}

	.side-text:first-child {
		left: 15%;
	}

	.side-text:last-child {
		right: 15%;
	}

	.spinner-border {
		width: 3rem;
		height: 3rem;
	}

	.cyber-text {
		color: #00ffff;
		margin: 0 10px;
	}

	.screen-container {
		background: linear-gradient(90deg, #000, #111);
		border: 3px solid #ff00ff;
		box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
		padding: 20px;
		color: #00ffff;
		font-family: 'Courier New', Courier, monospace;
		line-height: 1.5;
		overflow: hidden;
		position: relative;
		animation: glow 2s ease-in-out infinite alternate;
	}

	.screen-container::before {
		content: "";
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: repeating-linear-gradient(
		180deg,
		rgba(0, 255, 255, 0.2),
		rgba(0, 255, 255, 0.2) 1px,
			transparent 1px,
			transparent 2px
		);
		pointer-events: none;
	}

	@keyframes glow {
		from {
			box-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff, 0 0 15px #00ffff, 0 0 20px #00ffff;
		}
		to {
			box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
		}
	}
</style>