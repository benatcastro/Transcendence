<script lang="ts">
    import { onMount } from "svelte";
    import { page } from '$app/stores';
    let data
    onMount(async () => {
        const code  = $page.url.searchParams.get('code');
        const endpoint = "http://localhost:80/auth/42";
        const queryParams = new URLSearchParams();

        if (code)
            queryParams.set('code', code);

        const response = await fetch(endpoint+ "?" + queryParams, {method: "POST"});
        console.log("response status ->", response.status)
        data = await response.json();

        console.log("callback post data: ", data);
    })

</script>

<h1>hey this is a callback</h1>
<h1>{data?.email}</h1>