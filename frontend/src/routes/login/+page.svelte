<script lang="ts">
  import { goto } from "$app/navigation";
  function redirect42() {
    goto("http://localhost:8000/auth/42intra/login")
  }

  function redirectGoogle() {
      goto("http://localhost:8000/auth/google/login")
  }
</script>

<button on:click={redirect42}>Login with 42</button>
<button on:click={redirectGoogle}>Login with Google</button>
