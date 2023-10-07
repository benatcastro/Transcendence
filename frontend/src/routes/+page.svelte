<script lang="ts">
    import { goto } from "$app/navigation";

    let navOpts: string[][];
    let isLogged: boolean = true;
    $: {
        isLogged ? navOpts = [["Play", "/play"], ["Profile", "/profile"], ["Ranking", "/ranking"], ["Log out", "/logout"]]
                 : navOpts = [["Play", "/play"], ["Log in", "/"]];
    }
</script>

<nav class="primary-menu w-[30%] h-[65%] m-auto">
    <ul class="space-y-[80%]">
        {#each navOpts as opt}
            <li class="primary-button"><a on:click={() => goto(opt[1])} href="{opt[1]}">{opt[0]}</a></li>
        {/each}
    </ul>
</nav>