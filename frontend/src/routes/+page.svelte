<script lang="ts">
	import * as Threlte from '@threlte/core'
	import * as Three from 'three'
	import { T } from '@threlte/core'
	import { Grid, OrbitControls, TransformControls } from '@threlte/extras'
    import { DEG2RAD } from 'three/src/math/MathUtils.js'
	import type { Euler, Vector3 } from 'three'
	import { Debug } from '@threlte/rapier'
	import { World } from '@threlte/rapier'
	
    import Loop from './Loop.svelte'
    import Scene from './Scene.svelte'
    import Ball from './Ball.svelte'

	let ball_position = 6

	const getRandomRotation = (): Parameters<Euler['set']> =>
	{
		return [Math.random() * 10, Math.random() * 10, Math.random() * 10]
	}

	const onKeyDown = (e: KeyboardEvent) => {
		if (e.key === 'a')
		{
			e.preventDefault()
			console.log("a");
			ball_position -= 0.5
		}
		if (e.key === 'd')
		{
			e.preventDefault()
			console.log("d");
			ball_position += 0.5
		}
	}
</script>

<svelte:window on:keydown={onKeyDown}/>

<Threlte.Canvas>
	<World>
		<Scene />

		<Grid cellColor="#808080" sectionSize={0} />
		
		<T.PerspectiveCamera
		position={[20, 20, 20]}
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
		
		<T.Mesh position={[ball_position, 2, 0]} let:ref castShadow>
			<T.SphereGeometry args={[2, 32, 32]} />
			<T.MeshStandardMaterial color="#ffffff" />
		</T.Mesh>

		<T.Mesh position={[0, 0, 0]} rotation.x={DEG2RAD * 90 } receiveShadow>
			<T.PlaneGeometry args={[20, 20]} />
			<T.MeshStandardMaterial color="#ffffff" side={Three.DoubleSide} />
		</T.Mesh>

		<Ball position={[0, 1, 0]} rotation={getRandomRotation()}/>

		<Debug
			depthTest={false}
			depthWrite={false}
		/>
	</World>
</Threlte.Canvas>
