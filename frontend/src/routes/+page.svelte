<script lang="ts">
    import App from '$lib/components/App.svelte'
    import { isLogged } from '$lib/scripts/UserUtiliteis';
    import { constants } from '$lib/scripts/constants';
    import { onMount } from 'svelte';

    import { userState } from '$lib/scripts/stores';
  console.log("user " + userState)
</script>
  
  <div class="h-screen w-screen">
    <h1>Hello {userState.getUsername()}</h1> 
    <h2>your id is {userState.getId()}</h2> 
    <App />
  </div>
  