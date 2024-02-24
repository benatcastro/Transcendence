<script lang="ts">
	import * as Threlte from '@threlte/core'

	import { rival} from './store';

	let playerX = 0;

	Threlte.useFrame(() =>
	{
		if ($rival)
			playerX = -$rival.x;

	})
</script>


<!-- PLAYER 2 -->
<Threlte.T.Group
	position={[playerX, 1, -15]}
>
	<Threlte.T.Mesh let:ref castShadow position={[0, 0, -0.5]} >
		<Threlte.T.BoxGeometry args={[5, 2, 1]} />
		<Threlte.T.MeshStandardMaterial color="#ffffff" />
	</Threlte.T.Mesh>
</Threlte.T.Group>