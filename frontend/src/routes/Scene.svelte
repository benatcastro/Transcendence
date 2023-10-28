<script lang="ts">
	import * as Threlte from '@threlte/core'
    import * as Three from 'three'
	import { T } from '@threlte/core'
    import { Collider, RigidBody, AutoColliders } from '@threlte/rapier'
    import { DEG2RAD } from 'three/src/math/MathUtils.js'

    let PlayerVelocity = 10;

    let player1X = 0;
    let player2X = 0;

    let WallRightPosition = [10, 2, 0];
    let WallLeftPosition = [-10, 2, 0];
    let Player1Position = [player1X, 1, 15];
    let Player2Position = [player2X, 1, -15];

    const onKeyDown = (e: KeyboardEvent) =>
    {
        console.log(e.key);
        e.preventDefault()

		if (e.key == 'a')
			player1X = -PlayerVelocity
		if (e.key == 'd')
			player1X = PlayerVelocity
		if (e.key == 'ArrowLeft')
			player2X = -PlayerVelocity
		if (e.key == 'ArrowRight')
			player2X = PlayerVelocity
	}
    const onKeyUp= (e: KeyboardEvent) =>
    {
        e.preventDefault()
        if (e.key == 'a')
			player1X = 0
		if (e.key == 'd')
			player1X = 0
		if (e.key == 'ArrowLeft')
			player2X = 0
		if (e.key == 'ArrowRight')
			player2X = 0
	}
</script>

<svelte:window on:keydown={onKeyDown} on:keyup={onKeyUp}/>

<T.Group
    position={WallRightPosition}
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        enabledTranslations={[false, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'Wall'}}
    >
        tag={'WallRight'}
        <AutoColliders shape={'cuboid'}>
            <T.Mesh position={[0, 0, 0]} let:ref castShadow>
                <T.BoxGeometry args={[1, 4, 31]}/>
                <T.MeshStandardMaterial color="#ffffff" />
            </T.Mesh>
        </AutoColliders>
    </RigidBody>
</T.Group>

<T.Group
    position={WallLeftPosition}
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        enabledTranslations={[false, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'Wall'}}
    >
        <AutoColliders shape={'cuboid'}>
            <T.Mesh position={[0, 0, 0]} let:ref castShadow>
                <T.BoxGeometry args={[1, 4, 31]}/>
                <T.MeshStandardMaterial color="#ffffff" />
            </T.Mesh>
        </AutoColliders>
    </RigidBody>
</T.Group>
    

<!-- Ground -->
<T.Mesh position={[0, 0, 0]} rotation.x={DEG2RAD * 90 } receiveShadow>
    <T.PlaneGeometry args={[20, 30]} />
    <T.MeshStandardMaterial color="#ffffff" side={Three.DoubleSide} />
</T.Mesh>

<!-- PLAYER 1 -->
<T.Group
    position={[0, 1, 15]}
>
    <RigidBody
        type={'static'}
        gravityScale={0}
        enabledTranslations={[true, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'player1'}}
        linearVelocity={[player1X, 0, 0]}
    >
        <AutoColliders shape={'cuboid'}>
            <T.Mesh let:ref castShadow>
                <T.BoxGeometry args={[5, 2, 1]}/>
                <T.MeshStandardMaterial color="#ffffff" />
            </T.Mesh>
        </AutoColliders>
    </RigidBody>
</T.Group>

<!-- PLAYER 2 -->
<T.Group
position={[0, 1, -15]}
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        enabledTranslations={[true, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'player2'}}
        linearVelocity={[player2X, 0, 0]}
    >
        <AutoColliders shape={'cuboid'} >
            <T.Mesh let:ref castShadow >
                <T.BoxGeometry args={[5, 2, 1]}/>
                <T.MeshStandardMaterial color="#ffffff" />
            </T.Mesh>
        </AutoColliders>
    </RigidBody>
</T.Group>