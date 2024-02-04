<script lang="ts">
    import type {PageData} from './$types';
    import { page } from '$app/stores';
	import { onMount } from 'svelte';
    import { loginStorage } from '$lib/stores/stores';
    import { goto } from "$app/navigation";

    export let data: PageData;

    const code = $page.url.searchParams.get('code');
    let body;

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
                $loginStorage = data;
                await goto('/')

            } else {
                console.error('Failed to post code');
            }
        } catch (error) {
            console.error('Error posting code:', error);
        }
    }

    onMount(() => {
        getToken();
    })
</script>
