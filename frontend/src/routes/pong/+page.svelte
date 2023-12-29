<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T, useFrame } from '@threlte/core'
	import { Grid, OrbitControls, Environment } from '@threlte/extras'
	import { Debug } from '@threlte/rapier'
	import { World } from '@threlte/rapier'
	import Bloom from './bloom.svelte'
	import { onMount } from 'svelte';
    import { page } from '$app/stores';
	//import { ws } from './stores.js';
	
    import Scene from './Scene.svelte'
    import Ball from './Ball.svelte'

    import Player1 from './Player1.svelte'
    import Player2 from './Player2.svelte'
	import { esbuildVersion } from 'vite';

	let path = './'
	let files: string | string[] = 'Skybox.png'

	const user = $page.url.searchParams.get('user');
	const rival = $page.url.searchParams.get('rival');
	const room = $page.url.searchParams.get('room');

	//ws.set(new WebSocket('ws://localhost:8000/ws/game/?room_code=' + room))

	// ws.get().onopen = () => {
	// 	console.log('WebSocket connection opened');
	// };

	// ws.get().onmessage = (event) => {
	// 	console.log('WebSocket message received:', event.data);
	// };

	// ws.get().onclose = () => {
	// 	console.log('WebSocket connection closed');
	// };
	
</script>

<!-- <h1>Ander mariquita hihi</h1> -->

<Threlte.Canvas>
	<World>
		<Scene />
		<Player1 PlayerVelocity={10}/>
		<Player2 PlayerVelocity={10}/>
		<Ball />

		<!-- <StarsEmitter /> -->
		
		<Environment
			path={path}
			files={files}
			isBackground={true}
		/>

		<Bloom />

		<!-- <Grid cellColor="#808080" sectionSize={0} /> -->
		
		<T.PerspectiveCamera
			position={[0, 40, 20]}
			fov={50}
			makeDefault
			on:create={({ ref }) => {
				ref.lookAt(0, 1, 0)
			}}
		>
		<OrbitControls />
		</T.PerspectiveCamera>
		
		<T.AmbientLight color="#0B0B61" intensity={1} />
		
		<T.DirectionalLight
			color="#0B0B61"
			intensity={7}
			position={[10, 10, 0]}
			shadow.camera.top={8}
		/>
		
		<T.PointLight
			color="#75a1f9"
			intensity={500}
			position={[-1.75, 0, 1.75]}
		/>

		<T.FogExp2 color={'#dddddd'} density={100} />


		<Debug
			depthTest={false}
			depthWrite={false}
		/>
	</World>
</Threlte.Canvas>
