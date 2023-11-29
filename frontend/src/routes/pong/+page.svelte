<script lang="ts">
	import * as Threlte from '@threlte/core';
	import { T } from '@threlte/core';
	import { Grid, OrbitControls, Environment } from '@threlte/extras';
	import { Debug } from '@threlte/rapier';
	import { World } from '@threlte/rapier';

	import Scene from './Scene.svelte';
	import Ball from './Ball.svelte';

	import Player1 from './Player1.svelte';
	import Player2 from './Player2.svelte';

	let path = './';
	let files: string | string[] = 'Skybox.png';
</script>

<svelte:head>
	<meta
		name="description"
		content="Experience the adrenaline of our online 3D Pong game set in a mesmerizing cyberpunk world. Engage in fast-paced, visually stunning matches against players from around the globe."
	/>
	<title>CyberPong - Play</title>
	<!-- <h1>Ander mariquita hihi</h1> -->
</svelte:head>

<Threlte.Canvas>
	<World>
		<Scene />
		<Player1 PlayerVelocity={10} />
		<Player2 PlayerVelocity={10} />
		<Ball />

		<Environment {path} {files} isBackground={true} />

		<Grid cellColor="#808080" sectionSize={0} />

		<T.PerspectiveCamera
			position={[0, 40, 20]}
			fov={50}
			makeDefault
			on:create={({ ref }) => {
				ref.lookAt(0, 1, 0);
			}}
		>
			<OrbitControls />
		</T.PerspectiveCamera>

		<T.AmbientLight color="#0B0B61" intensity={0.2} />

		<T.DirectionalLight
			color="#0B0B61"
			intensity={2}
			position={[10, 10, 0]}
			shadow.camera.top={8}
		/>

		<T.PointLight color="#75a1f9" intensity={8} position={[5, 7, 0]} />

		<Debug depthTest={false} depthWrite={false} />
	</World>
</Threlte.Canvas>
