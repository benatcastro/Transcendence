<script lang="ts">
	import * as Threlte from '@threlte/core'

    import {ws, user, room, userName} from './store'
    //import {userName} from "$lib/stores/stores";

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
<Threlte.T.Group
    position={[playerX, 1, 15]}
>
    <Threlte.T.Mesh let:ref castShadow position={[0, 0, 0.5]} >
        <Threlte.T.BoxGeometry args={[5, 2, 1]} />
        <Threlte.T.MeshStandardMaterial color="#ffffff" />
    </Threlte.T.Mesh>
</Threlte.T.Group>