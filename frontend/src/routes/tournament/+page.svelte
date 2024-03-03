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
    import { userName, host, rival, room, mode } from '$lib/stores/stores';
    import {onMount} from "svelte";
	import { ws, tournamentName, inGame } from './tournament';
	import {ws as pong} from "../pong/store";

	let t_Name: string = "";
	let win: boolean = false;

	const send_json = {"type": "get_tournament",
		"user": $userName,
		"t_name": $tournamentName,
		"value": 0,
	}

	let response_json: JSON | undefined = undefined;
	let myTournament = undefined;

	export let interval = 500;
	let timer;

	// if ($userName == null || $userName == undefined || $userName == "")
	// 	goto('/');

    onMount(async () => {
        console.log($userName);
		$inGame = false;
		ws.set(new WebSocket("wss://" + host + ":443/ws/tournament/"));

		if ($ws) {
			$ws.onopen = () => {
				console.log('WebSocket connection opened');
				if ($ws)
				{
					send_json.type = "get_tournament";
					$ws?.send(JSON.stringify(send_json));

					if ($tournamentName != "")
					{
						send_json.type = "set_status";
						send_json.t_name = $tournamentName;
						$ws?.send(JSON.stringify(send_json));
					}
					else
						myTournament = undefined;
				}
			};
			$ws.onmessage = (event) => {
				//console.log('WebSocket message received:', event.data);
				try {
					response_json = JSON.parse(event.data);

					if (Object.values(response_json)[0] == undefined)
					{
						$tournamentName = "";
						myTournament = undefined;
					}
					for (let i = 0; i < Object.values(response_json).length; i++)
					{
						let players: Array<string> = Object.values(response_json)[i].players;
						if (players.includes($userName))
							myTournament = Object.values(response_json)[i];
					}

					if (myTournament.started && myTournament.players.length == 1 && myTournament.players[0] == $userName)
						win = true;
				}
				catch (e) {
					console.log('WebSocket message received:', event.data);
					goToPong(event.data);
				}
			};
			$ws.onclose = () => {
				console.log('WebSocket connection closed');
				$ws = null;
			};
		}

		fetchData();
    });

	timer = setInterval(async () => {
		fetchData();
	}, interval);

	async function fetchData() {
		//console.log("Find_Match: " + $tournamentName );
		//console.log(myTournament);
		if ($tournamentName != "" && myTournament && myTournament.started && $inGame == false)
		{
			send_json.type = "find_match";
			send_json.t_name = $tournamentName;
			$ws?.send(JSON.stringify(send_json));
		}
	}

	async function goToPong(msg: string) {
		if (msg.includes($userName) && $userName!= "")
		{
			if (msg.startsWith($userName))
				$rival = msg.replace($userName + "_", "");
			else
				$rival = msg.replace("_" + $userName, "");
			$room = msg;
			$mode = "tournament";
			//$ws?.close();
			$inGame = true;
			// send_json.type = "disconnect";
			// $ws?.send(JSON.stringify(send_json));
			await goto("/pong");
		}
		else if ($userName == "" || $userName == null || $userName == undefined)
			await goto("/");
	}

	async function handleSearchClick() {
		if ($ws)
		{
			send_json.type = "get_tournament";
			$ws?.send(JSON.stringify(send_json));
		}
	}

	async function handleCreateClick() {
		if ($ws && t_Name != "" && $userName != "")
		{
			send_json.type = "create_tournament";
			send_json.t_name = t_Name;
			$ws?.send(JSON.stringify(send_json));
			$tournamentName = t_Name;
		}
	}

	async function handleJoinClick(name: string) {
		if ($ws)
		{
			send_json.type = "join_tournament";
			send_json.t_name = name;
			$ws?.send(JSON.stringify(send_json));
			$tournamentName = name;
		}
	}
	async function handleLeaveClick() {
		if ($ws)
		{
			send_json.type = "leave_tournament";
			send_json.t_name = $tournamentName;
			send_json.user = $userName;
			$ws?.send(JSON.stringify(send_json));

			myTournament = undefined;
			$tournamentName = "";
		}
	}
	async function handleStartClick() {
		if ($ws)
		{
			send_json.type = "start_tournament";
			send_json.t_name = $tournamentName;
			$ws?.send(JSON.stringify(send_json));
		}
	}
	async function winButton() {
		send_json.type = "end_tournament";
		send_json.t_name = $tournamentName;
		$ws?.send(JSON.stringify(send_json));
		myTournament = undefined;
		$tournamentName = "";
		await goto("/");
	}

	addEventListener('beforeunload', () => {
		if ($userName && myTournament && !myTournament.started)
			handleLeaveClick();
	});

</script>

{#if (win)}
	<div class="modal-background">
    	<div class="modal-content victory-content" on:click|stopPropagation />
		<h1 class="modal-title victory-title">Victory Achieved</h1>
        <p class="tournament-name victory-tournament-name">Cybernetic Clash Tournament</p>
        <p class="subtext victory-subtext">Congratulations on your triumph in the cybernetic arena!</p>
        <button type="button" class="btn btn-secondary" on:click={() => winButton()}>Go Home</button>
    </div>
{:else if ($tournamentName === "" || $tournamentName === undefined)}
	<div class="modal-background">
		<div class="modal-content" on:click|stopPropagation>
			<h1 class="modal-title">Create Tournament</h1>
			<input bind:value={t_Name} placeholder="Enter name for tournament" />
			<button type="button" class="btn btn-secondary" on:click={() => handleCreateClick()}>Create Tournament</button>
			<button type="button" class="btn btn-secondary" on:click={() => handleSearchClick()}>Search Tournaments</button>
			-------------------------------------------------------------------
			{#if (response_json)}
				{#each Object.values(response_json) as tournament}
					{#if (!tournament.started)}
						<button type="button" class="btn btn-secondary" on:click={() => handleJoinClick(tournament.name)}>{tournament.name}</button>
					{/if}
				{/each}
			{/if}
		</div>
	</div>
{:else if ($tournamentName !== "" && myTournament && myTournament.started)}
	<div class="flex flex-center">
		<div class="flex flex-center container cyber-container h-75">
			<div class="row">
				{#each myTournament.players as player, index}
					<div class="col-sm-4 mb-3">
						<div class="card cyber-card">
							<div class="card-body">
								<h5 class="card-title cyber-title">{player}</h5>
								<p class="card-text">
									{#if myTournament.status[index] === 1}
									<span class="badge badge-success cyber-badge">In Game</span>
									{:else if myTournament.status[index] === -1}
									<span class="badge badge-danger cyber-badge">Lost</span>
									{:else}
									<span class="badge badge-warning cyber-badge">In Waiting Room</span>
									{/if}
								</p>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
{:else}
	<div class="modal-background">
		<div class="modal-content" on:click|stopPropagation>
			{#if (response_json && myTournament)}
				<h1 class="modal-title">Create Tournament</h1>
				{#if (myTournament.owner === $userName && myTournament.players.length >= 4 && myTournament.players.length % 2 === 0)}
					<button type="button" class="btn btn-secondary" on:click={() => handleStartClick()}>Start Tournament</button>
				{/if}
					<button type="button" class="btn btn-secondary" on:click={() => handleLeaveClick()}>Leave Tournaments</button>
				-------------------------------------------------------------------<br>
				{#each myTournament.players as player}
					{player}
					<br>
				{/each}
			{/if}
		</div>
	</div>
{/if}

<style>
	.victory-content {
    	background-color: rgba(0, 0, 0, 0.5);
    	border-radius: 10px;
    	padding: 20px;
    	text-align: center;
	}

	.victory-title {
    	font-size: 3rem;
    	text-transform: uppercase;
    	letter-spacing: 3px;
    	margin: 0;
    	color: #ff00ff; /* Cyberpunk pink */
	}

	.victory-tournament-name {
    	font-size: 1.5rem;
    	margin-top: 20px;
    	color: #ff00ff; /* Cyberpunk pink */
	}

	.victory-subtext {
    	font-size: 1rem;
    	margin-top: 20px;
    	color: #ff00ff; /* Cyberpunk pink */
	}

.victory-btn {
    background-color: transparent;
    border: 1px solid #00ffff; /* Cyberpunk blue */
    color: #00ffff; /* Cyberpunk blue */
    text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
    margin-top: 20px;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.victory-btn:hover {
    background-color: rgba(0, 255, 255, 0.5); /* Lighter shade of Cyberpunk blue */
    border-color: #00ffff; /* Cyberpunk blue */
    box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
}

.victory-btn:active {
    transform: translateY(2px);
}

.victory-btn {
    background-color: transparent;
    border: 1px solid #00ffff;
    color: #00ffff;
    text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
    margin-top: 20px;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.victory-btn:hover {
    background-color: rgba(0, 255, 255, 0.5);
    border-color: #00ffff;
    box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
}

.victory-btn:active {
    transform: translateY(2px);
}
	.btn.btn-cyberpunk {
		background-color: transparent;
		border: 1px solid #00ffff;
		color: #00ffff;
		text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
		margin-top: 20px;
		padding: 10px 20px;
		text-decoration: none;
		display: inline-block;
		border-radius: 5px;
    	transition: all 0.3s ease;
	}

	.btn.btn-cyberpunk:hover {
		background-color: rgba(0, 255, 255, 0.5);
   	 	border-color: #00ffff;
		box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
	}

	.btn.btn-cyberpunk:active {
    	transform: translateY(2px);
	}
	.container.cyber-container {
	  background-color: rgba(255, 0, 255, 0.2);
	  border: 2px solid #ff00ff;
	  border-radius: 5px;
	  box-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff;
	}

	.card.cyber-card {
	  background-color: rgba(83, 155, 155, 0.8);
	  border: 2px solid #62b4b4;
	  border-radius: 5px;
	  box-shadow: 0 0 10px #30a1a1, 0 0 20px #48c0c0, 0 0 30px #7bc9c9, 0 0 40px #7ddcdc;
	}

	.card-title.cyber-title {
		color: #000000;
		text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
	}

	.card-text {
		color: #00ffff;
		text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
	}

	.badge.cyber-badge {
		border: 1px solid #00ffff;
		box-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
	}

	.badge-success {
		background-color: #00ff00;
	}

	.badge-danger {
		background-color: #ff0000;
	}

	.badge-warning {
		background-color: #ffff00;
	}

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
</style>
