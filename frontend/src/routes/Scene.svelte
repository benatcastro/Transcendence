<script>
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
    import { AutoColliders } from '@threlte/rapier'
</script>

<AutoColliders shape={'cuboid'}>
    <T.Mesh position={[10, 2, 0]} let:ref castShadow>
        <T.BoxGeometry args={[1, 4, 21]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>
</AutoColliders>

<AutoColliders shape={'cuboid'}>
    <T.Mesh position={[-10, 2, 0]} let:ref castShadow>
        <T.BoxGeometry args={[1, 4, 21]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>
</AutoColliders>

<AutoColliders shape={'cuboid'}>
    <T.Mesh position={[0, 2, 10]} let:ref castShadow>
        <T.BoxGeometry args={[21, 4, 1]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>
</AutoColliders>

<AutoColliders shape={'cuboid'}>
    <T.Mesh position={[0, 2, -10]} let:ref castShadow>
        <T.BoxGeometry args={[21, 4, 1]} />
        <T.MeshStandardMaterial color="#ffffff" />
    </T.Mesh>
</AutoColliders>