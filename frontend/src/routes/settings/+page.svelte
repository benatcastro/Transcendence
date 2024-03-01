<script lang="ts">
	import { goto } from '$app/navigation';
	import {onMount} from "svelte";

	let volume: number = 1;

	function handleVolumeChange(e: Event) {
		volume = (e.target as HTMLInputElement).valueAsNumber / 100;
		let audio = document.querySelector('audio');

		audio.volume = volume;
	}

	onMount(() => {
		handleVolumeChange({
			target: {
				valueAsNumber: volume * 100
			} as any
		} as Event);
	});
</script>

<svelte:head>
	<title>CyberPong - Settings</title>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
			rel="stylesheet"
	/>
	<link
			href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
			rel="stylesheet"
	/>
</svelte:head>

<div class="d-flex flex-column flex-center">
 <h2>Settings</h2>
 <menu class="d-flex flex-column p-2">
   <div class="setting-container">
    <h3>Volume</h3>
     <label for="volume">Volume</label>
     <input id="volume" type="range" class="form-range" min="0" max="100" step="1" on:input={handleVolumeChange} />
   </div>
 </menu>
</div>
<a on:click={() => goto('/')} href="/">&lt;</a>

<style>
.form-range {
  -webkit-appearance: none !important;
  width: 100% !important;
  background: #000000 !important; /* Black background */
  border-radius: 10px !important;
  overflow: hidden !important;
}

.form-range::-webkit-slider-thumb {
  -webkit-appearance: none !important;
  height: 20px !important;
  width: 20px !important;
  background: #f0f !important; /* Neon pink slider */
  border-radius: 50% !important;
  cursor: pointer !important;
  box-shadow: 0 0 10px #f0f, 0 0 20px #f0f, 0 0 30px #f0f, 0 0 40px #f0f !important; /* Neon pink glow */
}

.form-range::-webkit-slider-runnable-track {
  width: 100% !important;
  height: 10px !important;
  cursor: pointer !important;
  background: #000000 !important; /* Black track */
  border-radius: 10px !important;
  border: 0 !important;
}

.form-range::-webkit-slider-runnable-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  background: #FFB6C1; /* Light pink track */
  border-radius: 10px;
  border: 0;
}

.form-range::-webkit-slider-runnable-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  background: #333;
  border-radius: 10px;
  border: 0;
}

.setting-container {
  border: 1px solid #80d4ff; /* Bright cyan border */
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  background: rgba(0,128,255,0.8); /* Less transparent blue background */
  color: #0ff; /* Neon blue text */
  box-shadow: 0 0 10px #f0f; /* Neon pink glow */
}

.setting-container h3 {
  margin-bottom: 10px;
  text-shadow: 0 0 10px #f0f; /* Neon pink text shadow */
}

.form-range::-webkit-slider-runnable-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  background: rgba(0,128,255,0.8); /* Less transparent blue track */
  border-radius: 10px;
  border: 0;
}

</style>
