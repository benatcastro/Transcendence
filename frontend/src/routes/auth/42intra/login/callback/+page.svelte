<script lang="ts">
    import type { PageData} from './$types';
    import { page } from '$app/stores';
    import { host } from '$lib/stores/stores';
    import { goto } from "$app/navigation";
    import {onMount} from "svelte";

    export let data: PageData;

    onMount(async () => {
        const code = $page.url.searchParams.get('code');

        const cookiePair = document.cookie.split("=")
        await getToken(cookiePair[1], code);

    })

    async function getToken(csrf: string, code: string) {
        try {
            const response = await fetch(`https://${host}:1024/auth/42intra/`, {
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
