<script lang="ts">
    import "../app.css"
</script>

<slot />

<div class="scene">
    <slot />
</div>div>

<style>
    .scene
    {
        width: 100%;
        height: 100%;
        position: absolute;
        inset: 0;
        background: radial-gradient(hsl(220 14% 20%), hsl(220 20% 10%));
        background-attachment: fixed;
    }
</style>