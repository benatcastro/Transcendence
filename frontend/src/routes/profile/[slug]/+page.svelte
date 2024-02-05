<svelte:head>
    <title>{data.user}'s profile</title>
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
            rel="stylesheet"
    />
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
            rel="stylesheet"
    />
</svelte:head>

<script lang="ts">
    import type {PageData} from './$types';
   
    export let data: PageData;
    const user = data.user;

    console.log("status", data.status)
    console.log("user", user)

    let selectedFile;
    let fileInput;
    let newEmail: string = '';
    let newPassword: string = '';
    let newUsername: string = '';

   

    async function uploadImage() {
    const cookiePair = document.cookie.split("=");
    const csrfToken = cookiePair ? cookiePair[1] : null;
    const formData = new FormData();

    formData.append('pfp', selectedFile[0]);

    const response = await fetch('https://localhost:442/upload/', {
        method: 'POST',
        credentials: 'include',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData,
    });

    if (response.ok) {
        const updatedUser = await response.json();
        user.pfp = updatedUser.pfp;
    }
}


    function triggerFileInput() {
        fileInput.click();
    }

    async function changeEmail() {
        const response = await fetch(`http://localhost:8000/api/users/${user.id}/`, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: newEmail })
        });

        if (response.ok) {
            const updatedUser = await response.json();
            $: {
                user.email = updatedUser.email;
                newEmail = '';
            }
        }
    }

    async function changePassword() {
        const response = await fetch(`http://localhost:8000/api/users/${user.id}/`, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: newPassword })
        });

        if (response.ok) {
            const updatedUser = await response.json();
            $: {
                user.password = updatedUser.password;
                newPassword = '';
            }
        }
    }

    async function changeUsername() {
        const cookiePair = document.cookie.split("=")
        const csrfToken = cookiePair ? cookiePair[1] : null;
        const response = await fetch(`http://localhost:8000/api/users/${user.id}/`, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ username: newUsername })
        });

        if (response.ok) {
            const updatedUser = await response.json();
            $: {
                user.username = updatedUser.username;
                newUsername = '';
            }
        }
    }
</script>

<div class="d-flex vh-100 flex-center">
    <div class="d-flex h-75 w-75 cyberpunk-container">
        <div class="d-flex flex-column mt-5 mx-5">
            <img class="profile-image m-5" src={user.pfp || '/assets/blank_profile.jpg'} alt="Profile image" on:click={triggerFileInput}>
            <span class="change-image-text">Change image</span>
            <input type="file" bind:files={selectedFile} bind:this={fileInput} style="display: none;" on:change={uploadImage} />
            <p class="placeholder p-2 m-2">{user.username}</p>
            <p class="placeholder p-2 m-2">{user.score}</p>
        </div>
        <div class="d-flex flex-column mt-5 mx-5">
            <input type="email" bind:value={newEmail} placeholder="New Email" class="form-control" />
            <button on:click={changeEmail} class="btn btn-primary">Change Email</button>
            <input type="password" bind:value={newPassword} placeholder="New Password" class="form-control mt-3" />
            <button on:click={changePassword} class="btn btn-primary">Change Password</button>
        </div>
        <div class="d-flex flex-column mt-5 mx-5">
            <input type="text" bind:value={newUsername} placeholder="New Username" class="form-control" />
            <button on:click={changeUsername} class="btn btn-primary">Change Username</button>
        </div>
    </div>
</div>

<style>
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
        width: 100px;
        height: 100px;
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