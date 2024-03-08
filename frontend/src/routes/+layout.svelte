<script lang="ts">
	import {goto} from "$app/navigation";

	const AUDIO_SRC = '/sound/Half_Mystery.mp3';
	const VOL_ON_IMAGE_SRC = '/assets/icons/volume-on.svg';
	const VOL_OFF_IMAGE_SRC = '/assets/icons/volume-off.svg';

	let volImageSrc = VOL_OFF_IMAGE_SRC;
	let musicPlayer;
	let isMusicOn = false;

	const toggleMusic = () => {
		isMusicOn = !isMusicOn;
		volImageSrc = isMusicOn ? VOL_ON_IMAGE_SRC : VOL_OFF_IMAGE_SRC;
		isMusicOn ? musicPlayer.play() : musicPlayer.pause();
	};
</script>

<audio
	bind:this={musicPlayer}
	on:ended={() => musicPlayer && musicPlayer.play()}
	src={AUDIO_SRC}
	preload="none"
/>

<div class="d-flex fixed-top">
	<button class="btn shadow-none mr-auto py-3" on:click={toggleMusic}>
		<img
			loading="lazy"
			src={volImageSrc}
			alt="Toggle music on/off button"
			class="w-header h-auto"
		/>
	</button>
	<button type="button" class="btn btn-link btn-extra-lg py-3 font-cr" on:click={() => goto('/')}>
		CYBERPONG
	</button>
	<div class="ml-auto">
		<button class="btn shadow-none px-0 py-3" on:click={() => goto('/me')}>
			<img
				loading="lazy"
				src={'/assets/icons/profile.svg'}
				alt="Log in/out button"
				class="w-header h-auto"
			/>
		</button>
		<button class="btn shadow-none px-0 py-3" on:click={() => goto('/settings')}>
			<!-- Change to dropdown when on game -->
			<img
				loading="lazy"
				src={'/assets/icons/settings.svg'}
				alt="Settings button"
				class="w-header h-auto"
			/>
		</button>
	</div>
</div>

<div class="vh-100">
	<slot />
</div>

<style>
	.btn-extra-lg {
		font-size: 2em;
		padding: 1em 2em;
	}
	footer a {
		color: #0ff;
		text-decoration: none;
	}

	footer a:hover {
		text-shadow: 0 0 5px #0ff,
		0 0 10px #0ff,
		0 0 15px #0ff,
		0 0 20px #0ff;
		animation: glow 1.5s infinite;
	}

	@keyframes glow {
		0%, 100% {
			text-shadow: none;
		}

		10%, 20% {
			text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 15px #0ff, 0 0 20px #0ff;
		}

		30% {
			text-shadow: none;
		}

		50%, 60% {
			text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 15px #0ff, 0 0 20px #0ff;
		}

		70%, 80% {
			text-shadow: none;
		}

		90% {
			text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 15px #0ff, 0 0 20px #0ff;
		}
	}

	:global(body) {
		background-image: url('/assets/backgrounds/light.webp');
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		background-attachment: fixed;
		overflow-x: hidden;
	}

	@font-face {
		font-family: 'Cyberway Riders';
		src: url('/fonts/cyberway_riders/Cyberway Riders.otf') format('opentype');
	}

	.font-cr {
		font-family: 'Cyberway Riders', sans-serif;
	}
</style>
