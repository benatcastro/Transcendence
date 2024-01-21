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
    import { loginStorage } from '$lib/stores/stores';

    let showModal: boolean = false;
    let isLoggedIn: boolean = false;
    let username: string = '';

    loginStorage.subscribe((loginSelection) => {
        if (browser && loginSelection) {
            goto(`http://localhost:8000/auth/${loginSelection}/login`);
        }
    });

    function toggleModal() {
        showModal = !showModal;
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
			if (option !== 'ranked' || isLoggedIn) {
				await getUser();
				await goto(`/matchmaking?mode=${option}&user=${username}`);
			}
		} catch (e) {
			console.error(e.message);
		}
	}
</script>

<div class="d-flex flex-column flex-center">
    <nav>
        <ul class="list-unstyled d-flex flex-column align-items-center">
            <li class="font-xe btn-lg w-100">
                <div class="card mb-3 p-5 m-3 btn cyberpunk-background" role="button" on:click={toggleModal}>
                    <button class="btn btn-link border-0"><span>Play</span></button>
                </div>
                {#if showModal}
                    <div class="modal-background" on:click={toggleModal}>
                        <div class="modal-content" on:click|stopPropagation>
                            <p class="modal-title">Select Mode</p>
                            <button type="button" class="btn btn-primary" on:click={() => handlePlayClick('casual')}>Casual</button>
                            <button type="button" class="btn btn-secondary" on:click={() => handlePlayClick('ranked')}>Ranked</button>
                        </div>
                    </div>
                {/if}I
            </li>
            <li class="font-xe d-flex justify-content-around w-100">
                <div class="card mb-3 p-5 m-3 btn cyberpunk-background" role="button" on:click={() => goto('/profile')}>
                    <button class="btn btn-link border-0"><span>Profile</span></button>
                </div>
                <div class="card mb-3 p-5 m-3 btn cyberpunk-background" role="button" on:click={() => goto('/rank')}>
                    <button class="btn btn-link border-0"><span>Leaderboard</span></button>
                </div>
            </li>
        </ul>
    </nav>
</div>

<style>
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
    }

    .modal-content {
        background: white;
        padding: 1em;
        max-width: 300px;
        margin: 0 auto;
        z-index: 2;
    }

	.cyberpunk-background {
		background: linear-gradient(90deg, rgba(204,0,255,0.8) 35%, rgba(0,255,255,0.8) 100%);
		border: 1px solid #00ffff;
		box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
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
