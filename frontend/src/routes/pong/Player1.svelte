<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
    import { Collider, RigidBody } from '@threlte/rapier'

    import { ws, user} from './store';

    //let PlayerVelocity = 10;
    export let PlayerVelocity = 0;

    let playerX = 0;

    let Left = false;
    let Right = false;

    const onKeyDown = (e: KeyboardEvent) =>
    {
        //console.log(e.key);
        e.preventDefault()

		if (e.key == 'a')
        {
            Left = true;
            $ws?.send($user + "_move:left1")
        }
		if (e.key == 'd')
        {
            Right = true;
            $ws?.send($user + "_move:right1")
        }
	}
    const onKeyUp = (e: KeyboardEvent) =>
    {
        e.preventDefault()
        if (e.key == 'a')
        {
            Left = false;
            $ws?.send($user + "_move:left0")
        }
		if (e.key == 'd')
        {
            Right = false;
            $ws?.send($user + "_move:right0")
        }
	}

    Threlte.useFrame(() =>
    {
		if (Left && Right)
            playerX = 0;
        else if (Left)
            playerX = -PlayerVelocity;
        else if (Right)
            playerX = PlayerVelocity;
        else
            playerX = 0;
	})
</script>

<svelte:window on:keydown={onKeyDown} on:keyup={onKeyUp}/>

<!-- PLAYER 1 -->
<T.Group
    position={[0, 1, 15]}
>
    <RigidBody
        gravityScale={0}
        enabledTranslations={[false, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'player1'}}
        linearVelocity={[playerX, 0, 0]}
    >
    <Collider
      shape={'cuboid'}
      args={[2.5, 1, 0.01]}
    />
    <T.Mesh let:ref castShadow position={[0, 0, 0.5]} >
        <T.BoxGeometry args={[5, 2, 1]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>

    <!-- <AutoColliders shape={'cuboid'}>
        <T.Mesh let:ref castShadow>
            <T.BoxGeometry args={[5, 2, 1]}/>
            <T.MeshStandardMaterial color="#ffffff" />
        </T.Mesh>
    </AutoColliders> -->
    </RigidBody>
</T.Group>