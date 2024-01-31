<svelte:head>
    <title>CyberPong</title>
    <meta
            name="description"
            content="Immerse yourself in a neon-lit cyberpunk world with our online 3D Pong app. Engage in intense matches, customize your profile, and climb the leaderboards in this futuristic gaming universe."
    />
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css"
            rel="stylesheet"
    />
    <link
            href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.16.0/css/mdb.min.css"
            rel="stylesheet"
    />
</svelte:head>

<div class="d-flex flex-center tournament">
    <div class="round">
        <div class="match">
            <div class="player">Player 1</div>
            <div class="player">Player 2</div>
        </div>
        <div class="match">
            <div class="player">Player 3</div>
            <div class="player">Player 4</div>
        </div>
    </div>
    <div class="round">
        <div class="match">
            <div class="player">Winner 1</div>
            <div class="player">Winner 2</div>
        </div>
    </div>
</div>

<style>
.tournament {
    display: flex;
    justify-content: space-between;
    width: 100%;
    color: #00ffff;
    background: linear-gradient(90deg, rgba(204,0,255,0.8) 35%, rgba(0,255,255,0.8) 100%);
    border: 1px solid #00ffff;
    box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
}

.round {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 45%;
}

.match {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid #00ffff;
    margin-bottom: 20px;
    background-color: rgba(0, 255, 255, 0.5);
    box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
}

.player {
    padding: 10px;
    border-bottom: 1px solid #00ffff;
    text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
}

.player:last-child {
    border-bottom: none;
}
</style>