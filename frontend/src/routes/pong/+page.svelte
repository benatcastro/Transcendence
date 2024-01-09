<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
	import { OrbitControls, Environment } from '@threlte/extras'
	import { Debug } from '@threlte/rapier'
	import { World } from '@threlte/rapier'
	import Bloom from './bloom.svelte'
	import { onMount } from 'svelte';
    import { page } from '$app/stores';
	import { ws, userName, rivalName, room, ball, user, rival, isPlayer1 } from './store';
	
    import Scene from './Scene.svelte'
    import Ball from './Ball.svelte'

    import Player1 from './Player1.svelte'
    import Player2 from './Player2.svelte'
	//import { esbuildVersion } from 'vite';

	let path = './'
	let files: string | string[] = 'Skybox.png'

	//ws.set(new WebSocket('ws://localhost:8000/ws/game/?room_code=' + room))
	onMount(() => {
		userName.set($page.url.searchParams.get('user')?.toString());
		rivalName.set($page.url.searchParams.get('rival')?.toString());
		room.set($page.url.searchParams.get('room')?.toString());

		console.log('user: ' + $page.url.searchParams.get('user')?.toString());
		console.log('rival: ' + $page.url.searchParams.get('rival')?.toString());
		console.log('room: ' + $room);

		// Crea tu WebSocket
		ws.set(new WebSocket('ws://localhost:8000/ws/game/?room_code=' + $room + '&username=' + $page.url.searchParams.get('user')?.toString()));
		
		if ($ws) {
			$ws.onopen = () => {
				console.log('WebSocket connection opened');
			};
			$ws.onmessage = (event) => {
				//console.log('WebSocket message received:', event.data);
				if ($userName == JSON.parse(event.data.split('_')[0]).name)
				{
					$user = JSON.parse(event.data.split('_')[0]);
					$rival = JSON.parse(event.data.split('_')[1]);
					$isPlayer1 = true;
				}
				else
				{
					$rival = JSON.parse(event.data.split('_')[0]);
					$user = JSON.parse(event.data.split('_')[1]);
					$isPlayer1 = false;
				}
				$ball = JSON.parse(event.data.split('_')[2]);
			};
			$ws.onclose = () => {
				console.log('WebSocket connection closed');
			};
		}
	});

</script>

<!-- <h1>Ander mariquita hihi</h1> -->

<Threlte.Canvas>
	<World>
		<Scene />
		<Player1 />
		<Player2 />
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
	</World>
</Threlte.Canvas>
