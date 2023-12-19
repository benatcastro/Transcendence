<script>
  import { onMount } from 'svelte';

  let audio;

  // Función para iniciar la reproducción
  function playAudio() {
    audio.play();
  }

  // Función para manejar el final de la pista
  function onAudioEnd() {
    audio.currentTime = 0;
    playAudio();
  }

  // Iniciar la reproducción automáticamente al montar el componente
  onMount(() => {
    playAudio();
  });
</script>

<audio bind:this={audio} on:ended={onAudioEnd} src="/test.mp3"></audio>

