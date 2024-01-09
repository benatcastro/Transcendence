<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core';
	import { useGltf } from '@threlte/extras';
	import { ws, ball, isPlayer1 } from './store';

	let ballX = 0;
	let ballZ = 0;
	
	Threlte.useFrame(() =>
	{
		if ($ball && $ws)
		{
			$ws?.send("ball_move:")
			if ($isPlayer1 == true)
			{
				ballX = $ball.x;
				ballZ = $ball.z;
			}
			else
			{
				ballX = -$ball.x;
				ballZ = -$ball.z;
			}
		}
	});
</script>

{#await useGltf('/ball.glb') then ball}
	<T is={ball.scene} position={[ballX, 1, ballZ]} scale={3} />
{/await}

