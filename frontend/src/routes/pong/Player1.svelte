<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'

    import { ws, user} from './store'

    let playerX = 0;


    const onKeyDown = (e: KeyboardEvent) => {
        e.preventDefault()

		if (e.key == 'a' && $ws && $user)
            $ws?.send($user.name + "_move:left")
		if (e.key == 'd' && $ws && $user)
            $ws?.send($user.name + "_move:right")
	}

    Threlte.useFrame(() => {
		if ($user)
		    playerX = $user.x;
	})
</script>

<svelte:window on:keydown={onKeyDown} />

<!-- PLAYER 1 -->
<T.Group
    position={[playerX, 1, 15]}
>
    <T.Mesh let:ref castShadow position={[0, 0, 0.5]} >
        <T.BoxGeometry args={[5, 2, 1]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>
</T.Group>