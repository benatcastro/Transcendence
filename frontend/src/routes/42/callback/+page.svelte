<script>
  import { onMount } from "svelte";
  import { page } from '$app/stores';
  import { writable } from "svelte/store"; 
    import { constants } from "$lib/scripts/constants";

  let token;

  onMount(async () => {
    

    
    // console.log($page.url.searchParams.get('code'));
    const code  = $page.url.searchParams.get('code');
    const state  = $page.url.searchParams.get('state');

    const endpoint = "http://localhost:3000/auth/42/callback"
    const query_params = new URLSearchParams();

    if (code)
      query_params.set('code', code);
    if (state)
      query_params.set('state', state);

    console.log("url:", endpoint+ "?" + query_params);

    const response = await fetch(endpoint+ "?" + query_params)
    const data = await response.json();
    token = data.JWT;
    localStorage.setItem(constants.JWTkey, token);
  })
</script>

<h1>this is the callback</h1>
{#if token === undefined}
Loading token...
{:else}
<h1>JWT: {token}</h1>
{/if}