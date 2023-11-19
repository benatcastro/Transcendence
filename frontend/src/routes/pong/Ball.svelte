<script lang="ts" context="module">
	const geometry = new SphereGeometry(1)
	const material = new MeshStandardMaterial({ color: '#ffffff' });
</script>

<script lang="ts">
	import * as Threlte from '@threlte/core';
	import { T } from '@threlte/core';
	import { MeshStandardMaterial, SphereGeometry, Vector3, BoxGeometry, Object3D, Group, type Euler} from 'three';
	import { Collider, RigidBody } from '@threlte/rapier';

	let xPower = getRandomNumber();
	let zPower = 7;
	let linearVelocity: number[] = [xPower, 0, zPower];
	
	let unique = {}; // every {} is unique, {} === {} evaluates to false

	const ChangeDirection = (e: ContactEvent) =>
	{
		if (e.targetRigidBody.userData['tag'] == "player1" || e.targetRigidBody.userData['tag'] == "player2")
			zPower *= -1.2;
		else if (e.targetRigidBody.userData['tag'] == "Point")
			unique = {};
		else
			xPower *= -1;
		linearVelocity = [xPower, 0, zPower];
	}

	const getRandomRotation = (): Parameters<Euler['set']> =>
	{
		return [Math.random() * 10, Math.random() * 10, Math.random() * 10];
	}

	function getRandomNumber()
	{
		let numeroAleatorio;
		do {
			numeroAleatorio = Math.floor(Math.random() * 21) - 10; // Genera un número entre -10 y 10
		} while (numeroAleatorio === 0); // Repite si el número es 0

		return numeroAleatorio;
	}
	
</script>

{#key unique}
	<T.Object3D
		position={[0, 1, 0]}
		rotation={getRandomRotation()}
	>
		<RigidBody
			type={'dynamic'}
			gravityScale={0}
			linearVelocity={linearVelocity}
			enabledTranslations={[true, false, true]}
			enabledRotations={[false, false, false]}
			on:contact={ChangeDirection}
		>
			<Collider
				shape={'ball'}
				args={[1]}
				on:sensorenter={() => {
					xPower = getRandomNumber();
					zPower = 7;
					unique = {};
				}}
			/>
			<T.Mesh
				castShadow
				receiveShadow
				{geometry}
				{material}
			/>
		</RigidBody>
	</T.Object3D>
{/key}

