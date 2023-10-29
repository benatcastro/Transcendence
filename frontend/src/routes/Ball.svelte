<script lang="ts" context="module">
    const geometry = new SphereGeometry(1)
	const material = new MeshStandardMaterial({ color: '#ffffff' });
</script>

<script lang="ts">
    import * as Threlte from '@threlte/core'
    import { T } from '@threlte/core'
	import { MeshStandardMaterial, SphereGeometry, Vector3, BoxGeometry} from 'three';
	import { Collider, RigidBody } from '@threlte/rapier'
    import type { Euler } from 'three'

    let xPower = 9.5;
    let zPower = 6.5;
    let linearVelocity: [number, number, number] = [xPower, 0, zPower];

    export let position: Parameters<Vector3['set']>
    export let rotation: Parameters<Euler['set']>

    const ChangeDirection = (e: RigidBody) =>
    {
        // console.log(e.other.parent.tag.toString());
        if (e.targetRigidBody.userData['tag'] == "player1" || e.targetRigidBody.userData['tag'] == "player2")
        {
            console.log("ChangeYDirection");
            zPower *= -1.05;
            linearVelocity = [xPower, 0, zPower];
        }
        else
        {
            console.log("ChangeXDirection");
            xPower *= -1.05;
            linearVelocity = [xPower, 0, zPower];
        }
    }
</script>

<T.Group
    position={position}
    tag="ball"
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        linearVelocity={linearVelocity}
        enabledTranslations={[true, false, true]}
        enabledRotations={rotation}
        on:contact={ChangeDirection}
    >
        <Collider
            shape={'ball'}
            args={[1]}
        />
        <T.Mesh
            castShadow
            receiveShadow
            {geometry}
            {material}
        />
    </RigidBody>
</T.Group>
