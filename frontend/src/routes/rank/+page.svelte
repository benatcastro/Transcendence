<script lang="ts">
    import {onMount} from "svelte";
    import {host} from "$lib/stores/stores";

    let users = [];

    onMount(async () => {
        try {
            const response = await fetch(`https://${host}:1024/users/all`);
            console.log(`https://${host}:1024/users/all`);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            if (!Array.isArray(data)) {
                throw new Error("Data is not an array");
            }

            users = data;
            users.sort((a, b) => a.username.localeCompare(b.username));
        } catch (error) {
            console.error("Fetch error: ", error);
        }
    });
</script>

<svelte:head>
	<title>CyberPong - Leaderboard</title>
	<meta
		name="description"
		content="Check the rankings and standings in our cyberpunk 3D Pong leaderboard. See where you stand among global players and strive to reach the top with your gaming skills."
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

<div class="d-flex justify-content-center align-items-center vh-100">
  <div class="card w-75 h-75 shadow-lg">
    <div class="card-body">
      <h1 class="card-title text-center font-xe">Ranking</h1>
      <div class="container text-center">
        <div class="row">
		<div class="col list-group-item"><h2>Rank</h2></div>
          <div class="col list-group-item"><h2>Username</h2></div>
          <div class="col list-group-item"><h2>Points</h2></div>
        </div>
          {#if users.length !== 0}
            {#each users as user}
              <div class="row">
                <div class="col list-group-item">{user.id}</div>
                <div class="col list-group-item">{user.username}</div>
                <div class="col list-group-item">{user.score}</div>
              </div>
            {/each}
          {/if}
      </div>
    </div>
  </div>
</div>

<style>
	@font-face {
		font-family: 'xenotron';
		src: url('/fonts/xenotron/XENOTRON.TTF') format('truetype');
	}

	.font-xe {
		font-family: 'xenotron', sans-serif;
	}

	.card {
		background-color: rgba(0,128,255,0.6);
		border: 2px solid #80d4ff;
		border-radius: 25px;
		box-shadow: 0 2px 10px #80d4ff;
	}

	.card::before {
		content: "";
		position: absolute;
		border-radius: 25px;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		background: linear-gradient(30deg, #ff0000, #00ff00, #0000ff);
		mix-blend-mode: soft-light;
		z-index: -1;
	}

	@media screen and (min-width: 992px){
		.card .card-title {
			font-size: 3rem;
		}
	}

	@media screen and (min-width: 992px){
		.card .list-group-item {
			font-size: 1.5rem;
		}
	}

	.list-group-item {
		background-color: #104693;
		border: 2px solid #80d4ff;
		box-shadow: 0 2px 10px #80d4ff;
	}

</style>