
<script lang="ts">
	import { goto } from '$app/navigation';

	let menuOpts: string[] = ['Volume', 'Graphics', 'Game'];

//audio script 

let lines: NodeListOf<SVGLineElement>;

function init() {
  lines = document.querySelectorAll('#bg line') as NodeListOf<SVGLineElement>;
  renderFrame();
}

function updateLines() {
  const time = Date.now();
  const frequency = 0.005; // Ajusta la frecuencia de movimiento
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    let phase = (i / lines.length) * 12 * Math.PI; // Asegura que cada línea tiene una fase única
    let value = Math.sin(frequency * time + phase);
    let y1 = 300 - value * 300; // Escala el valor al rango de y de tu SVG
    let y2 = 300 + value * 300; // Escala el valor al rango de y de tu SVG
    line.setAttribute('y1', y1.toString());
    line.setAttribute('y2', y2.toString());
  }
}

function renderFrame() {
  requestAnimationFrame(renderFrame);
  updateLines();
}

if (typeof window !== 'undefined') {
  window.onload = init;
}

function getRandomNeonColor() {
    const colors = ['#39ff14', '#fb56c1', '#01cdfe', '#b967ff', '#ff5e5e']; // Colores de neón
    return colors[Math.floor(Math.random() * colors.length)]; // Devuelve un color aleatorio de la lista
  }

  function highlightLines() {
    let color = getRandomNeonColor(); // Obtiene un color de neón aleatorio
    let lines = document.querySelectorAll('line'); // Obtiene todas las líneas en el documento
    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];
      line.style.stroke = color; // Aplica el color a todas las líneas
    }
  }

  function resetLines() {
    let lines = document.querySelectorAll('line'); // Obtiene todas las líneas en el documento
    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];
      line.style.stroke = null; // Restablece el color de las líneas
    }
  }
</script>
<body>
	<div class="waveform">
		<h2>Settings</h2>
		<menu>
			<!-- Volume on click opens sub-menu for music and sound effects -->
			<!-- Graphics click opens sub-menu for animations and effects, as well as general graphics -->
			<!-- Game click opens sub-menu for skins and personalization -->
			{#each menuOpts as opt}
				<button>{opt}</button>
			{/each}
		</menu>
	  <svg on:mouseover={highlightLines} on:mouseout={resetLines} on:focus={highlightLines} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
		<defs>
		  <linearGradient id="grad1" x1="393.05" y1="400" x2="393.05" y2="200" gradientUnits="userSpaceOnUse">
			<stop offset="0" stop-color="#4147d5"/>
			<stop offset="1" stop-color="#4147d5"/>
		  </linearGradient>
		</defs>
	  
		<g id="bg" fill="none" stroke="url(#grad1)" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
		  <line x1="580.5" y1="390" x2="580.32" y2="210"/>
		  <line x1="565.5" y1="415" x2="565.28" y2="185"/>
		  <line x1="550.5" y1="434" x2="550.24" y2="166"/>
		  <line x1="535.5" y1="449" x2="535.22" y2="151"/>
		  <line x1="520.5" y1="462" x2="520.2" y2="138"/>
		  <line x1="505.5" y1="472" x2="505.18" y2="128"/>
		  <line x1="490.5" y1="480" x2="490.16" y2="120"/>
		  <line x1="475.5" y1="487" x2="475.14" y2="113"/>
		  <line x1="460.5" y1="492" x2="460.14" y2="108"/>
		  <line x1="445.5" y1="496" x2="445.12" y2="104"/>
		  <line x1="430.5" y1="499" x2="430.12" y2="101"/>
		  <line x1="415.5" y1="501" x2="415.12" y2="99"/>
		  <line x1="400.5" y1="501" x2="400.12" y2="99"/>
		  <line x1="385.5" y1="501" x2="385.12" y2="99"/>
		  <line x1="370.5" y1="499" x2="370.12" y2="101"/>
		  <line x1="355.5" y1="496" x2="355.12" y2="104"/>
		  <line x1="340.5" y1="492" x2="340.14" y2="108"/>
		  <line x1="325.5" y1="487" x2="325.14" y2="113"/>
		  <line x1="310.5" y1="480" x2="310.16" y2="120"/>
		  <line x1="295.5" y1="472" x2="295.18" y2="128"/>
		  <line x1="280.5" y1="462" x2="280.2" y2="138"/>
		  <line x1="265.5" y1="449" x2="265.22" y2="151"/>
		  <line x1="250.5" y1="434" x2="250.24" y2="166"/>
		  <line x1="235.5" y1="415" x2="235.28" y2="185"/>
		  <line x1="220.5" y1="390" x2="220.32" y2="210"/>
		  <line x1="205.5" y1="370" x2="205.32" y2="230"/>
		  <line x1="190.5" y1="355" x2="190.28" y2="245"/>
		  <line x1="175.5" y1="334" x2="175.24" y2="266"/>
		  <line x1="160.5" y1="319" x2="160.22" y2="281"/>
		  <line x1="145.5" y1="304" x2="145.2" y2="296"/>
		  <line x1="130.5" y1="294" x2="130.18" y2="306"/>
		  <line x1="115.5" y1="282" x2="115.16" y2="318"/>
		  <line x1="100.5" y1="271" x2="100.14" y2="329"/>
		  <line x1="85.5" y1="261" x2="85.12" y2="339"/>
		  <line x1="70.5" y1="254" x2="70.12" y2="346"/>
		  <line x1="55.5" y1="248" x2="55.12" y2="352"/>
		  <line x1="40.5" y1="244" x2="40.12" y2="356"/>
		  <line x1="25.5" y1="242" x2="25.12" y2="358"/>
		  <line x1="10.5" y1="241" x2="10.12" y2="359"/>
		</g>
	  </svg>
	  
	</div>
</body>
<svelte:head>
	<title>CyberPong - Settings</title>
</svelte:head>


<a on:click={() => goto('/')} href="/">&lt;</a>

<style>
menu {
  position: fixed;
  top: 10%;
  left: 5%;
  width: 100%;
  padding: 10px; 
  z-index: 2; 
}

.waveform {
  position: relative;
  z-index: 1;
}



svg {
  position: relative; 
  margin:0, auto;
  width: 20%;
  height: 20%;
  z-index: 1; /* Disminuye el z-index del SVG */
  rotate: 180deg;
}

		line {
	stroke: rgb(255, 0, 255); /* Cambia esto a un color rosa neón */
	stroke-width: 10;
	stroke-opacity: 0.8;
	mix-blend-mode: screen;
	filter: drop-shadow(0 0 10px rgba(255, 0, 255, 0.8)); /* Añade un resplandor */
	transition: stroke-opacity 0.3s ease;
	animation: pulse 1s ease infinite alternate; /* Hace que las líneas pulsen */
	}

	@keyframes pulse {
	to {
		stroke-opacity: 1;
	}
	}
	/*
        Not decided yet, probably will try to simulate some electronic components
        and reflect how the electronics change as the settings do.

        I.E. You turn up the volume, and a bar connected to a sound system in the
        background goes up and changes on a gradient. Similar to electronic music
        components.
    */

	/* P.S.: Do not fucking touch my styles or I will eat your god damn eyeballs */
</style>
