<script lang="ts">
    import type { PageData} from './$types';
    import { page } from '$app/stores';
    import { goto } from "$app/navigation";
    import {onMount} from "svelte";

    export let data: PageData;

    const code = $page.url.searchParams.get('code');

    async function getToken() {
        try {
            const response = await fetch('http://localhost:8000/auth/google/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "code": code }),
            });
            if (response.ok) {
                data = await response.json();
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
