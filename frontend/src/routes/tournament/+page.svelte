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

<script lang="ts">
    import { goto } from '$app/navigation';
    import { browser } from '$app/environment';
    import { userName } from '$lib/stores/stores';
    import {onMount} from "svelte";
	import { ws } from './tournament';
	import {ball, isPlayer1, rival, room, user} from "../pong/store";

	let tournamentName: string = "";

    onMount(async () => {
        console.log($userName);

		ws.set(new WebSocket('wss://localhost/ws/tournament/'));

		if ($ws) {
			$ws.onopen = () => {
				console.log('WebSocket connection opened');
			};
			$ws.onmessage = (event) => {
				console.log('WebSocket message received:', event.data);
			};
			$ws.onclose = () => {
				console.log('WebSocket connection closed');
			};
		}

    });

	async function handleSearchClick() {
		if ($ws)
			$ws?.send("get_tournaments");
	}
</script>

<div class="modal-background">
	<div class="modal-content" on:click|stopPropagation>
		<h1 class="modal-title">Create Tournament</h1>
		<input bind:value={tournamentName} placeholder="Enter name for tournament" />
		<button type="button" class="btn btn-secondary" on:click={() => handleSearchClick()}>Create Tournament</button>
		<button type="button" class="btn btn-secondary" on:click={() => handleSearchClick()}>Search Tournaments</button>
	</div>
</div>

<style>

    .modal-background {
        background: white;
		margin: 1%;
		margin-top: 80px;
		font-family: 'xenotron', sans-serif;
    }

    .modal-content {
		align-items: center;
		justify-content: center;
    }

    div.btn:hover {
        background-color: rgba(0, 255, 255, 0.5);
        border-color: #00ffff;
        box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
    }

    div.btn button:hover {
        background-color: transparent;
        border-color: transparent;
        box-shadow: none;
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
