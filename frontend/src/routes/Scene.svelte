<script lang="ts">
	import * as Threlte from '@threlte/core'
    import * as Three from 'three'
	import { T } from '@threlte/core'
    import { Collider, RigidBody, AutoColliders } from '@threlte/rapier'
    import { DEG2RAD } from 'three/src/math/MathUtils.js'
    import { Text } from '@threlte/extras'

    export let Player1Points: number = 0;
	export let Player2Points: number = 0;

	let PointText: string = "Player2 " + Player2Points.toString() + "\nPlayer1 " + Player1Points.toString();

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
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        enabledTranslations={[false, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'Point'}}
    >
        <Collider
            sensor
            shape={'cuboid'}
            args={[20, 4, 1]}
            on:sensorenter={() => {
                console.log("Player 1 scored!");
                Player2Points += 1;
                PointText = "Player2 " + Player2Points.toString() + "\nPlayer1 " + Player1Points.toString();
            }}
        />
    </RigidBody>
</T.Group>

<!-- POINT TRIGGERS -->
<T.Group
    position={[0, 2, -17.5]}
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        enabledTranslations={[false, false, false]}
        enabledRotations={[false, false, false]}
        userData={{tag: 'Point'}}
    >
        <Collider
            sensor
            shape={'cuboid'}
            args={[20, 4, 1]}
            on:sensorenter={() => {
                console.log("Player 1 scored!");
                Player1Points += 1;
                PointText = "Player2 " + Player2Points.toString() + "\nPlayer1 " + Player1Points.toString();
            }}
        />
    </RigidBody>
</T.Group>

<T.Group
    rotation={[-1.5, 0, 0]}
>
    <Text
        text={PointText}
        color="white"
        fontSize={4}
        anchorX="50%"
        anchorY="100%"
    />
</T.Group>

<h1>{Player1Points}</h1>
<h1>{Player2Points}</h1>