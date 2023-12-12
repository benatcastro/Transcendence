<script lang="ts">
    import type {PageData} from './$types';

    export let data: PageData;
    // console.log(data)
    const user = data.user;
    console.log("status", data.status)
    console.log("user", user)

</script>

{#if data.status !== 'ok'}
    <h1>Can't find {data.user}</h1>
{:else}
    <h1>{user.username} profile</h1>
    <h2>email:{user.email}</h2>
    <button>Sent friend request</button>

{/if}