<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'

    import {ws, user, room} from './store'
    import {userName} from "$lib/stores/stores";

    let playerX = 0;

	const send_json = {"room": $room,
		"user": $userName,
		"value": "",
	}

    const onKeyDown = (e: KeyboardEvent) => {
        e.preventDefault()

		if (e.key == 'a' && $ws && $user)
        {
            send_json.value = "left";
            $ws?.send(JSON.stringify(send_json))
        }
		if (e.key == 'd' && $ws && $user)
        {
            send_json.value = "right";
            $ws?.send(JSON.stringify(send_json))
        }
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