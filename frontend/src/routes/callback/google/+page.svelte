<script lang="ts">
    import type {PageData} from './$types';
    import { page } from '$app/stores';

    const code = $page.url.searchParams.get('code');
     async function getToken() {
         try {
             const response = await fetch('http://localhost:8000/auth/google/', {
                 method: 'POST',
                 headers: {
                     'Content-Type': 'application/json',
                 },
                 body: JSON.stringify({ "code": code }),
             });

             if (response.ok) {
                 data = await response.json();
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

<h1>Google callback</h1>
<h3>code: {code}</h3>
