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

    export let data: PageData;
    const user = data.user;

    console.log("status", data.status)
    console.log("user", user)
    $: editing = false

    let selectedFile;
    let fileInput;
    let newEmail: string = '';
    let newPassword: string = '';
    let newUsername: string = '';

    async function uploadImage() {
        const formData = new FormData();
        formData.append('image', selectedFile[0]);

        const response = await fetch('http://localhost:8000/users/uploadImage', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const updatedUser = await response.json();
            user.image = updatedUser.image;
        }
    }

    function triggerFileInput() {
        fileInput.click();
    }



    async function changeUsername() {
        const response = await fetch(`http://localhost:8000/users/${user.username}/`, {
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
                newUsername = '';
                editing = !editing
            }
        }
    }
</script>
{#if user !== "404"}
<div class="wrapper">
    <div class="d-flex center h-70 w-70 cyberpunk-container">
        <div class="flex-column mt-5 mx-5">
            <div class="pfp-wrapper center">
                <img class="profile-image m-5" src={user.image || '/assets/blank_profile.jpg'} alt="Profile image" on:click={triggerFileInput}>
                <span class="change-image-text">Change image</span>
            </div>
            <input type="file" bind:files={selectedFile} bind:this={fileInput} style="display: none;" on:change={uploadImage} />
            <div class="edit-username-wrapper">
                <input class="placeholder p-2 m-2" value={user.username} readonly={!editing}/>
                <button on:click={editing ? changeUsername : () => editing = !editing} class="btn btn-primary">
                    {#if editing}
                        <span class="material-symbols-outlined">check</span>
                    {:else}
                        <span class="material-symbols-outlined">edit</span>
                    {/if}
                </button>
            </div>
            <p class="placeholder p-2 m-2">{user.score}</p>
        </div>
    </div>
</div>
{:else}
    <div class="center h-100">
        <h1>User 404</h1>
    </div>
{/if}

<style>



    .wrapper {
        height: 100vh;
        display: flex;
        justify-content: center;
        justify-items: center;
        align-items: center;
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
    }
</style>
