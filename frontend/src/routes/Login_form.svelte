<script>
	import { goto } from "$app/navigation";

    function buttonTest() {
        goto ('http://localhost:3000/auth/login');
    }
</script>

<div class="pixel-border h-96 w-80 bg-white box">
    <h1 class="text-center font-pixel font-bold text-6xl m-4">LOGIN</h1>
    <button class="pixel-button" on:click={buttonTest}>Test</button>
</div>