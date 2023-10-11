<script lang="ts">
    import { goto } from "$app/navigation";

    let navOpts: string[][];
    let isLogged: boolean = true;
    $: {
        isLogged ? navOpts = [["Play", "/play"], ["Profile", "/profile"], ["Ranking", "/ranking"], ["Log out", "/logout"]]
                 : navOpts = [["Play", "/play"], ["Log in", "/"]];
    }
</script>

<h1 id="main-title">CyberPong</h1>
<nav class="primary-menu w-[30%] h-[65%] m-auto opacity-0 animate-fade-in animation-delay-9000">
    <ul class="flex flex-col justify-evenly h-full">
        {#each navOpts as opt}
            <li class="primary-button"><a on:click={() => goto(opt[1])} href="{opt[1]}">{opt[0]}</a></li>
        {/each}
    </ul>
</nav>