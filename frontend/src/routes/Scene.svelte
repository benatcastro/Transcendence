<script lang="ts">
	import * as Threlte from '@threlte/core'
    import * as Three from 'three'
	import { T } from '@threlte/core'
    import { Collider, RigidBody, AutoColliders } from '@threlte/rapier'
    import { DEG2RAD } from 'three/src/math/MathUtils.js'

    let Player1Points = 0;
	let Player2Points = 0;

</script>

<!-- WALL RIGHT -->
<T.Group
    position={[10, 2, 0]}
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

<!-- WALL LEFT -->
<T.Group
    position={[-10, 2, 0]}
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

<!-- POINT TRIGGERS -->
<T.Group
    position={[0, 2, 17.5]}
>
    <Collider
        sensor
        shape={'cuboid'}
        args={[20, 4, 1]}
        on:sensorenter={() => {
            console.log("Player 1 scored!");
            Player1Points += 1;
        }}
    />
</T.Group>

<!-- <T.Group>
    <Text
        {Player1Points.toString()}
        color="white"
        {20}
        anchorX="50%"
        anchorY="100%"
    />
</T.Group> -->

<h1>{Player1Points}</h1>
<h1>{Player2Points}</h1>