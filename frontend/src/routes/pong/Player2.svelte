<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'

	import { rival} from './store';

	let playerX = 0;

	Threlte.useFrame(() =>
	{
		if ($rival)
			playerX = -$rival.x;

	})
</script>


<!-- PLAYER 2 -->
<T.Group
	position={[playerX, 1, -15]}
>
	<T.Mesh let:ref castShadow position={[0, 0, -0.5]} >
		<T.BoxGeometry args={[5, 2, 1]} />
		<T.MeshStandardMaterial color="#ffffff" />
	</T.Mesh>
</T.Group>