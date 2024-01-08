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

<div class="d-flex justify-content-between fixed-top">
	<button class="btn shadow-none p-0" on:click={toggleMusic}>
		<img
			loading="lazy"
			src={volImageSrc}
			alt="Toggle music on/off button"
			class="w-header h-auto"
		/>
	</button>
	<div>
		<button class="btn shadow-none p-0" on:click={() => goto('/profile')}>
			<img
				loading="lazy"
				src={'/assets/icons/profile.svg'}
				alt="Log in/out button"
				class="w-header h-auto"
			/>
		</button>
		<button class="btn shadow-none p-0" on:click={() => goto('/settings')}>
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

<footer class="fixed-bottom text-center py-3">
	<a href="/meet">Meet the team</a>
</footer>

<style>
	:global(body) {
		background-image: url('/assets/backgrounds/light.webp');
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
	}
</style>
