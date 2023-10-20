<script lang="ts">
	import * as Threlte from '@threlte/core'
	import * as Three from 'three'
	import { T } from '@threlte/core'
	import { Grid, OrbitControls, TransformControls } from '@threlte/extras'
    import { DEG2RAD } from 'three/src/math/MathUtils'
</script>

<Threlte.Canvas>

	<Grid cellColor="#808080" sectionSize={0} />

	<T.PerspectiveCamera position={[20, 20, 20]} fov={50} makeDefault>
		<OrbitControls enableDamping />
	</T.PerspectiveCamera>

	<T.AmbientLight color="#ffffff" intensity={0.2} />
	
	<T.DirectionalLight
		color="#ffffff"
		intensity={2}
		position={[10, 10, 0]}
		shadow={{
			camera: {top: 8},
		}}
	/>

	<T.Mesh position={[0, 4, 0]} let:ref castShadow>
		<T.SphereGeometry args={[4, 64, 64]} />
		<T.MeshStandardMaterial color="#ffffff" />
	</T.Mesh>
	<T.Mesh rotation.x={DEG2RAD * 90 } receiveShadow>
		<T.PlaneGeometry args={[20, 20]} />
		<T.MeshStandardMaterial color="#ffffff" side={Three.DoubleSide} />
	</T.Mesh>
</Threlte.Canvas>