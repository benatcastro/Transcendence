<script lang="ts">
	const AUDIO_SRC = '/sound/Half_Mystery.mp3';
	const IMAGE_SRC = '/assets/icons/speaker.webp';

	let musicPlayer;

	const playMusic = () => {
		if (musicPlayer) {
			musicPlayer.play();
		}
	};
</script>

<audio
	bind:this={musicPlayer}
	on:ended={() => musicPlayer && musicPlayer.play()}
	src={AUDIO_SRC}
	preload="none"
/>

<div class="fixed-top text-left">
	<button class="btn btn-outline- shadow-none p-0" on:click={playMusic}>
		<img loading="lazy" src={IMAGE_SRC} alt="Toggle music on/off button" class="w-header h-auto" />
	</button>
</div>

<slot />

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
