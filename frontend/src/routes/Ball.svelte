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

    let xPower = 8;
    let zPower = 3;
    let linearVelocity = [xPower, 0, zPower];

    export let position: Parameters<Vector3['set']>
    export let rotation: Parameters<Euler['set']>

    const ChangeDirection = (e: ContactEvent) =>
    {
        console.log("ChangeDirection");
        xPower *= -1;
        zPower *= -1;

        linearVelocity = [xPower, 0, zPower];
    }
    
</script>

<T.Group
    position={position}
>
    <RigidBody
        type={'dynamic'}
        gravityScale={0}
        bind:linearVelocity={linearVelocity}
        enabledTranslations={[true, false, true]}
        enabledRotations={[false, false, false]}
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
