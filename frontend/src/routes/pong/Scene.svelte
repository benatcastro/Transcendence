<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
	import { DEG2RAD } from 'three/src/math/MathUtils.js'
	import { Text } from '@threlte/extras'
	import { useGltf } from '@threlte/extras'

	import { ws, user, rival } from './store';

	const setText = (): string => {
		if ($rival && $user)
			return $rival.name + " " + $rival.points.toString() + "\n\n\n\n\n" + $user.name + " " + $user.points.toString();
		else if ($rival && !$user)
			return $rival.name + " " + $rival.points.toString() + "\n\n\n\n\n" + "UserName --";
		else if (!$rival && $user)
			return "RivalName --" + "\n\n\n\n\n" + $user.name + " " + $user.points.toString();
		else
			return "RivalName --" + "\n\n\n\n\n" + "UserName --";
	}

	let PointText: string = "";
	Threlte.useFrame(() =>{
		PointText = setText();
		//console.log(PointText);
	});

</script>

<!-- WALL RIGHT -->
<T.Group
	position={[16, 1, 0]}
>
	<T.Mesh position={[0, 1, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, -1, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, 15.5]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.BoxGeometry args={[1, 1, 3]}/>
		<T.MeshStandardMaterial color="#000000"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, -15.5]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.BoxGeometry args={[1, 1, 3]}/>
		<T.MeshStandardMaterial color="#000000"/>
	</T.Mesh>
</T.Group>

<!-- WALL LEFT -->
<T.Group
	position={[-15, 1, 0]}
>
	<T.Mesh position={[0, 1, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, -1, 0]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.CylinderGeometry args={[0.2, 0.2, 31]}/>
		<T.MeshBasicMaterial color="#ffffff"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, 15.5]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.BoxGeometry args={[1, 1, 3]}/>
		<T.MeshStandardMaterial color="#000000"/>
	</T.Mesh>
	<T.Mesh position={[0, 0, -15.5]} rotation={[DEG2RAD * 90, 0, 0]}>
		<T.BoxGeometry args={[1, 1, 3]}/>
		<T.MeshStandardMaterial color="#000000"/>
	</T.Mesh>
</T.Group>
	

<!-- Ground -->
<!-- <T.Mesh position={[0, 0, 0]} rotation.x={DEG2RAD * 90 } receiveShadow>
	<T.PlaneGeometry args={[20, 30]} />
	<T.MeshStandardMaterial color="#ffffff" side={Three.DoubleSide} />
</T.Mesh> -->

<T.Group
	rotation={[DEG2RAD * -90, 0, 0]}
	position={[0, -1.9, 13]}
>
	<Text
		text={PointText}
		color="white"
		fontSize={4}
		anchorX="50%"
		anchorY="100%"
	/>
</T.Group>

<!-- SKYSCRAPER -->

{#await useGltf('/futuristic-tower/source/tower.glb') then tower}
	<T is={tower.scene} position={[0, -60, 0]} scale={1} />
{/await}
<!-- {#await useGltf('/city.glb') then city}
	<T is={city.scene} position={[40, -40, -40]} scale={[1, 1, 2]} />
{/await} -->
<!-- {#await useGltf('/oil_build.glb') then oil}
	<T is={oil.scene} position={[-40, -100, -40]} scale={0.3} />
{/await}
{#await useGltf('/build01.glb') then build01}
	<T is={build01.scene} position={[-35, -100, 0]} scale={10} />
{/await}
{#await useGltf('/city.glb') then city}
	<T is={city.scene} position={[-120, -100, 70]} scale={2} />
{/await} -->

