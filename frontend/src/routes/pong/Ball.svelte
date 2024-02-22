<script lang="ts">
	import { T } from '@threlte/core';
	import { useGltf } from '@threlte/extras';
	import { onMount } from 'svelte';
	import {ws, ball, isPlayer1, room} from './store';

	let ballX = 0;
	let ballZ = 0;

	export let interval = 50;
	let timer;

	const send_json = {"room": $room,
		"user": "ball",
		"value": "move",
	}


	onMount(() => {
		// Esta función se ejecuta cuando el componente se monta en el DOM
		timer = setInterval(() => {
			if ($ball && $ws)
			{
				if ($isPlayer1 == true)
				{
					$ws?.send(JSON.stringify(send_json))
					ballX = $ball.x;
					ballZ = $ball.z;
				}
				else
				{
					ballX = -$ball.x;
					ballZ = -$ball.z;
				}
			}
		}, interval);

		// También puedes ejecutar el comando una vez inmediatamente después de montar el componente
		console.log('Ejecutando el comando inicial...');
	});

	// Threlte.useFrame(() =>
	// {
	// 	if ($ball && $ws)
	// 	{
	// 		$ws?.send("ball_move:")
	// 		if ($isPlayer1 == true)
	// 		{
	// 			ballX = $ball.x;
	// 			ballZ = $ball.z;
	// 		}
	// 		else
	// 		{
	// 			ballX = -$ball.x;
	// 			ballZ = -$ball.z;
	// 		}
	// 	}
	// });
</script>

{#await useGltf('/ball.glb') then ball}
	<T is={ball.scene} position={[ballX, 1, ballZ]} scale={3} />
{/await}

