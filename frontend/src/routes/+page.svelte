<script lang="ts">
    import * as Threlte from '@threlte/core'
    import * as Three from 'three'
    import * as Utils from 'three/src/math/MathUtils'
</script>

<Threlte.Canvas>

    <Threlte.PerspectiveCamera position={{x: 20, y: 20, z:20}} fov={50}>
        <Threlte.OrbitControls />
    </Threlte.PerspectiveCamera>
            
    <Threlte.AmbientLight color = "white" intensity={0.2} />
            
    <Threlte.Mesh
        geometry = {new Three.SphereGeometry(4, 64, 64)}
        material = {new Three.MeshStandardMaterial({color: 'white'})}
    />

</Threlte.Canvas>
