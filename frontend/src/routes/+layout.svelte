<script lang="ts">
    import { goto } from "$app/navigation";
    import "../app.css";
</script>

<div id="screen-container">
    <slot />
    <footer class="secondary-button fixed bottom-0 left-1/2 -translate-x-1/2">
        <a on:click={() => goto("/team")} href="/team">Meet the team</a>
    </footer>
</div>
