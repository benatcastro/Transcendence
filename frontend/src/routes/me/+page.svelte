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
    import {deleteFriends} from "$lib/utilities/utilities";
    import {modifyUser} from "$lib/utilities/utilities";

    export let data: PageData;


    let user = data.user;
    let friends = data.friends.friends;

    console.log("status", data.status)
    console.log("user", user)
    console.log("friends", data.friends.friends)
    $: editing = false

    let selectedFile: (string | Blob)[];
    let fileInput: HTMLInputElement;
    let newUsername: string = user.username;
    let searchInput = "";
    // let friends: any[] = []
    let searchingUsers = "";

    function formatImageData() {

        const formData = new FormData();
        formData.set("pfp", selectedFile[0])
        // formData.append(selectedFile[0]);
        // console.log(formData.);
        


        return formData
    }

    

    function triggerFileInput() {
        fileInput.click();
    }

    async function updateSearchedUserList() {
        if (searchInput === undefined)
            return

        let url = new URL("http://localhost:8000/users/?")
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


    async function modifyAndUpdate(userID: string, newValues: any) {
        const updatedUser = await modifyUser(userID, newValues);
        console.log("Update:", updatedUser)
        console.log("og:", user)
        user = updatedUser;
        console.log("after:", user)
    }

    async function addFriendWrapper(fromUser: string, toUser: any) {
        const updatedFriends = await  addFriends(fromUser, toUser)
        console.log("UpdateAddFriend:", updatedFriends)
        console.log("data:", updatedFriends)
    }

    async function deleteFriendWrapper(fromUser: string, toUser: any) {
        const updatedFriends = await  deleteFriends(fromUser, toUser)
        console.log("Updatedeleteriend:", updatedFriends)
        console.log("data:", updatedFriends)
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
            <input type="file" bind:files={selectedFile} bind:this={fileInput} style="display: none;" on:change={() => modifyAndUpdate(user.username, formatImageData())} />
            <div class="edit-username-wrapper">
                <input bind:value={newUsername} class="placeholder p-2 m-2" placeholder={user.username} readonly={!editing}/>
                <button on:click={editing ? () => modifyAndUpdate(user.username, JSON.stringify({username: newUsername})) : () => editing = !editing} class="btn btn-primary">
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
                <h1 class="cyber-text">Friends</h1>
                <div class="friend-list">
                    {#each friends as friend}
                        <div class="user-search">
                            <img class="user-search-pfp" src={friend.pfp} alt="pfp">
                            <a href={"http://localhost:5173/profile/" + friend.username}><h4>{friend.username}</h4></a>
                        </div>
                        <div class="center">
                            <h5>{friend.status}</h5>
                            <button type="button" class="btn btn-primary btn-sm" on:click={() => deleteFriendWrapper(user.username, search_username.username)}>Delete Friend</button>
                        </div>
                    {/each}
                </div>
                <input type="text"  placeholder="Search new Friends" bind:value={searchInput} on:input={updateSearchedUserList} class="placeholder p-2 m-2">
                {#each searchingUsers as search_user}
                    {#if user.username !== search_user.username}
                    <div>
                        <div class="user-search">
                            <img class="user-search-pfp" src={search_user.pfp} alt="pfp">
                            <a href={"http://localhost:5173/profile/" + search_user.username}><h4>{search_user.username}</h4></a>
                        </div>
                        <div class="user-search">
                            <h5>{search_user.status}</h5>
                            {#if !(user.friends.includes(search_user.id))}
                                <button type="button" class="btn btn-primary btn-sm" on:click={() => addFriendWrapper(user.username, search_user.username)}>Add Friend</button>
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
