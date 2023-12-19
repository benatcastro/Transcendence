<script lang="ts">
    import type {PageData} from './$types';
    import { page } from '$app/stores';
	import { onMount } from 'svelte';
    import { goto } from "$app/navigation";

    const code = $page.url.searchParams.get('code');
    let body;

    onMount( async() => {
        async function getToken() {
            try {
                const response = await fetch('http://localhost:8000/auth/42intra/', {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ "code": code }),
                });

                if (response.ok) {
                    data = await response.json();
                    console.log('Code posted successfully');
                    console.log(response.headers)
                    console.log(data);
                    goto('/')

                } else {
                    console.log(data)
                    console.error('Failed to post code');
                }
            } catch (error) {
                console.error('Error posting code:', error);
            }
        }
        getToken()
    })
    export let data: PageData;
</script>

<h1>42intra callback</h1>
<h3>code: {code}</h3>
<p>{body}</p>
