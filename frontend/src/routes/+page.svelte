<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
	import { Grid, OrbitControls, TransformControls } from '@threlte/extras'
	import type { Euler, Vector3 } from 'three'
	import { Debug } from '@threlte/rapier'
	import { World } from '@threlte/rapier'
	
    import Scene from './Scene.svelte'
    import Ball from './Ball.svelte'
    import Player1 from './Player1.svelte'
    import Player2 from './Player2.svelte'
    import { goto } from '$app/navigation';

	const getRandomRotation = (): Parameters<Euler['set']> =>
	{
		return [Math.random() * 10, Math.random() * 10, Math.random() * 10]
	}
</script>

<Threlte.Canvas>
	<World>
		<Scene />
		<Player1 PlayerVelocity={10}/>
		<Player2 PlayerVelocity={10}/>

		<Grid cellColor="#808080" sectionSize={0} />
		
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
		
		<T.AmbientLight color="#33476f" intensity={0.2} />
		
		<T.DirectionalLight
		color="#33476f"
		intensity={2}
		position={[10, 10, 0]}
		shadow.camera.top={8}
		/>
		
		<T.PointLight
		color="#75a1f9"
		intensity={8}
		position={[5, 7, 0]}
		/>

		<Ball position={[0, 1, 0]} rotation={getRandomRotation()}/>

		<Debug
			depthTest={false}
			depthWrite={false}
		/>
	</World>
</Threlte.Canvas>
