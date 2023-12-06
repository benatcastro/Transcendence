<script lang="ts">
    import * as Threlte from '@threlte/core'

    // your script goes here

    import { Instance } from '@threlte/extras'
    import { Color } from 'three'

    let positionX = Math.random() * 100 - 50
    let positionY = Math.random() * 100 - 50
    let positionZ = 0


    const colors = ['#FFF09E', '#B8DFFF', '#CADBFF', '#FFEBBE']

    // random element from array
    const color = new Color(colors[Math.floor(Math.random() * colors.length)])

    Threlte.useFrame((delta) =>
    {
        const f = 1 / 60 / delta
        positionY -= 10 * f
    })
</script>
  
<Instance
    {color}
    position.x={positionX}
    position.y={positionY}
    position.z={positionZ}
/>