<script>
  import { goto } from "$app/navigation";


  function redirect () {
    goto("http://localhost:3000/auth/42/login")
  }
</script>

<button on:click={redirect}>Login 42</button>