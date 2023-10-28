<script>
    import { userState } from "$lib/scripts/stores";
    import { get } from 'svelte/store'

    
    console.log("id: ", get(userState.id))
    console.log("username: ", get(userState.username))
</script>

<slot />