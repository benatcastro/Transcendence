<script>
    import LoginForm from './Login_form.svelte'
</script>

<div class="h-screen flex items-center justify-center">
    <LoginForm></LoginForm>  
</div>

<style lang="postcss">
    :global(html) {
      background-color: theme(colors.gray.600);
    }
</style>