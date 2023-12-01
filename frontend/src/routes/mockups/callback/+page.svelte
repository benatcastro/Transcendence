<script lang="ts">
    import { onMount } from "svelte";
    import { page } from '$app/stores';

    onMount(async () => {
        const code  = $page.url.searchParams.get('code');
        const endpoint = "http://localhost:80/auth/42";
        const queryParams = new URLSearchParams();

        if (code)
            queryParams.set('code', code);

        const response = await fetch(endpoint+ "?" + queryParams, {method: "POST"});
        const data = await response.json();

        console.log("callback post data: ", data);
    })

</script>

<h1>hey this is a callback</h1>