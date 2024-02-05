<svelte:head>
    <title>Profile</title>
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
            rel="stylesheet"
    />
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
            rel="stylesheet"
    />
    <link
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
          rel="stylesheet"
    />

    <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
        rel="stylesheet"
    />
</svelte:head>

<script lang="ts">
    import type {PageData} from './$types';
    import {addFriends} from "$lib/utilities/utilities";
    import {modifyUser} from "$lib/utilities/utilities";

    export let data: PageData;
    const user = data.user;

    console.log("status", data.status)
    console.log("user", user)
   
    $: editing = false

    let selectedFile;
    let fileInput;
    let newUsername: string = user.username;

    let searchInput = "";

    async function formatImageData() {

        const formData = new FormData();
        formData.append('pfp', selectedFile[0]);
        return formData
    }
console.log(selectedFile)
    function triggerFileInput() {
        fileInput.click();
    }

    let searchingUsers = "";
    async function updateSearchedUserList() {
        if (searchInput === undefined)
            return

        let url = new URL("http://8000:1024/users/?")
        let params = new URLSearchParams(url)
        params.append("search", searchInput)

        console.log(url + params)
        const response = await fetch(url + params, {
            method: 'GET',
            credentials: 'include',
        });

        if (response.ok) {
            searchingUsers = await response.json();
        }
        // console.log(response)
    }


    async function changeUsername() {
        console.log("new username: ", newUsername)
        const response = await fetch(`https://localhost:442/users/${user.username}/`, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: newUsername })
        });

        if (response.ok) {
            const updatedUser = await response.json();
            console.log(updatedUser)
            $: {
                user.username = updatedUser.username;
            }
        }
        editing = false
        console.log(response)
    }
</script>
{#if user !== "404"}
<div class="wrapper">
    <div class="d-flex center h-70 w-70 cyberpunk-container">
        <div class="flex-column mt-5 mx-5">

            <h1 class="cyber-text center">User Details</h1>
            <div class="pfp-wrapper center">
                
                    
                
                <img class="profile-image m-5" src={user.pfp} alt="Profile image" on:click={triggerFileInput}>
                <span class="change-image-text">Change image</span>
            </div>
            <input type="file" bind:files={selectedFile} bind:this={fileInput} style="display: none;" on:change={modifyUser(user.username, await formatImageData())} />
            <div class="edit-username-wrapper">
                <input bind:value={newUsername} class="placeholder p-2 m-2" placeholder={user.username} readonly={!editing}/>
                <button on:click={editing ? modifyUser(user.username, JSON.stringify({username: newUsername})) : () => editing = !editing} class="btn btn-primary">
                    {#if editing}
                        <span class="material-symbols-outlined">check</span>
                    {:else}
                        <span class="material-symbols-outlined">edit</span>
                    {/if}
                </button>
            </div>
            <p class="placeholder p-2 m-2">{user.email}</p>
            <p class="placeholder p-2 m-2">{user.score}</p>
        </div>
    </div>

    <div class="d-flex center h-70 w-70 cyberpunk-container">
        <div class="user-search">
            <div class="flex-column mt-5 mx-5">
                <h1 class="cyber-text">Search Users</h1>
                <input type="text"  placeholder="Search Friends" bind:value={searchInput} on:input={updateSearchedUserList} class="placeholder p-2 m-2">
                {#each searchingUsers as search_user}
                    {#if user.username !== search_user.username}
                    <div>
                        <div class="user-search">
                            <img class="user-search-pfp" src={search_user.pfp} alt="pfp">
                            <a href={"https://localhost/profile/" + search_user.username}><h4>{search_user.username}</h4></a>
                        </div>
                        <div class="user-search">
                            <h5>{search_user.status}</h5>
                            {#if !(user.friends.includes(search_user.id))}
                                <button type="button" class="btn btn-primary btn-sm" on:click={() => addFriends(user.username, search_user.username)}>Add Friend</button>
                            {:else}
                                <p>Already friends</p>
                            {/if}

                        </div>

                    </div>
                        {/if}
                {/each}

            </div>

        </div>
    </div>
    <div class="d-flex center h-70 w-70 cyberpunk-container">
        <div class="center mt-5 mx-5">
           <h1 class="cyber-text">Match History</h1>
       </div>
    </div>
</div>
{:else}
    <div class="center h-100">
        <h1 class="cyber-text">User 404</h1>
    </div>
{/if}

<style>

    .user-search {
        display: flex;
        gap: 1em;
        align-items: center;

    }

    .user-search-pfp {
        border-radius: 50%;
        width: 3em;
        height: 3em;
        object-fit: cover;

    }

    .cyber-text {
        color: #0ff;
        font-style: italic;
        padding: 10px;
        text-shadow: 0 0 10px #0ff, 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;

    }

    .wrapper {
        margin-top: 15em;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        justify-items: center;
        align-items: center;
        flex-direction: column;
        gap: 5em;
    }

    .center {
        display: flex;
        justify-content: center;
        justify-items: center;
        align-items: center;
    }

    .edit-username-wrapper {
        display: grid;
        grid-template-columns: auto 8em;
    }

    .placeholder {
        color: #0ff;
        font-style: italic;
        background: linear-gradient(90deg, rgba(255,0,255,0.7) 0%, rgba(0,255,255,0.7) 50%, rgba(255,0,255,0.7) 100%);
        border: 1px solid #0ff;
        padding: 10px;
        border-radius: 5px;
        text-shadow: 0 0 10px #0ff, 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;
    }
    .profile-image {
        border-radius: 50%;
        width: 10em;
        height: 10em;
        object-fit: cover;
    }

    .change-image-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        display: none;
    }

    .cyberpunk-container {
        background: linear-gradient(90deg, rgba(255,0,255,0.7) 0%, rgba(0,255,255,0.7) 50%, rgba(255,0,255,0.7) 100%);
        border: 7px solid;
        border-image: linear-gradient(90deg, rgb(146, 194, 208) 0%, rgb(69, 141, 210) 50%, rgb(137, 166, 175) 100%) 1;
        min-width: 30%;
    }
</style>
