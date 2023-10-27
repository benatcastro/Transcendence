<script>
  import { isLogged } from "$lib/scripts/UserUtiliteis";
  import { constants } from "$lib/scripts/constants";
    import { onMount } from "svelte"; 

  let status;

  onMount( async () => {
     status = isLogged(localStorage.getItem(constants.JWTkey));

  })
</script>

<h1>this is the callback</h1>
{#if status === true}
  <h1>User is logged!</h1>
{:else}
<h1>User is not logged</h1>
{/if}