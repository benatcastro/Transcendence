<script lang="ts">
    import type {PageData} from './$types';
    import { page } from '$app/stores';

    const code = $page.url.searchParams.get('code');
    let body;
     async function getToken() {
         try {
             const response = await fetch('http://localhost:8000/auth/42intra/', {
                 method: 'POST',
                 headers: {
                     'Content-Type': 'application/json',
                 },
                 body: JSON.stringify({ "code": code }),
             });

             if (response.ok) {
                 body = await response.json();
                 console.log('Code posted successfully');
                 console.log(data);
             } else {
                 console.error('Failed to post code');
             }
         } catch (error) {
             console.error('Error posting code:', error);
         }
     }
    getToken()
    export let data: PageData;
</script>

<h1>42intra callback</h1>
<h3>code: {code}</h3>
<p>{body}</p>
