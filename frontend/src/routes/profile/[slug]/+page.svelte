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

</script>

<div class="d-flex vh-100 flex-center">
    <div class="d-flex h-75 w-75 cyberpunk-container">
        <img class="profile-image m-5" src={user.image || '/assets/blank_profile.jpg'} alt="Profile image" on:click={triggerFileInput}>
        <span class="change-image-text">Change image</span>
        <input type="file" bind:files={selectedFile} bind:this={fileInput} style="display: none;" on:change={uploadImage} />
    </div>
</div>

<style>
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
        z-index: -1;
        border: 7px solid;
        border-image: linear-gradient(90deg, rgb(146, 194, 208) 0%, rgb(69, 141, 210) 50%, rgb(137, 166, 175) 100%) 1;
    }
</style>