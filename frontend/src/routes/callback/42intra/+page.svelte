<script lang="ts">
    import type { PageData} from './$types';
    import { page } from '$app/stores';
    import { loginStorage } from '$lib/stores/stores';
    import { goto } from "$app/navigation";
    import {onMount} from "svelte";

    export let data: PageData;

    onMount(async () => {
        const cookiePair = document.cookie.split("=")
        getToken(cookiePair[1]);

    })

    const code = $page.url.searchParams.get('code');
    async function getToken(csrf: string) {
        try {
            const response = await fetch('http://localhost:8000/auth/42intra/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "x-csrftoken": csrf,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "code": code }),
            });
            if (response.ok) {
                data = await response.json();
                //$loginStorage = data;
                console.log(data.user.email.split('@')[0]);
                await goto('/')
            } else {
                console.log(response.json());
                console.error('Failed to post code');
            }
        } catch (error) {
            console.error('Error posting code:', error);
        }
    }

</script>
