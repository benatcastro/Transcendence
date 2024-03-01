<script lang="ts">
	import * as Threlte from '@threlte/core'
	import { T } from '@threlte/core'
	import { OrbitControls, Environment } from '@threlte/extras'
	import Bloom from './bloom.svelte'
	import { onMount } from 'svelte';
    import { page } from '$app/stores';
	import { ws, userName, rivalName, room, ball, user, rival, isPlayer1    } from './store';
    import { host, userName as user_name, room as room_name, rival as rival_name, mode } from '$lib/stores/stores';

    import Scene from './Scene.svelte'
    import Ball from './Ball.svelte'

    import Player1 from './Player1.svelte'
    import Player2 from './Player2.svelte'
	import {goto} from "$app/navigation";
    import {tournamentName,  ws as tournament } from "../tournament/tournament";

	$userName = $user_name;
	$rivalName = $rival_name;
	$room = $room_name;
	$user = null;
	$rival = null;
	$ball = null;

	console.log('user: ' + $userName);
	console.log('rival: ' + $rivalName);
	console.log('room: ' + $room);

	let isWsInit: boolean = false;
	let status: number = -1;
    try {
        // Crea tu WebSocket
        ws.set(new WebSocket("wss://" + $host + ":443/ws/game/?room_code=" + $room + "&username=" + $user_name));

        if ($ws) {
            $ws.onopen = () => {
                console.log('WebSocket connection opened');
                isWsInit = true;
                deleteMatchmaking();
            };
            $ws.onmessage = async (event) => {
                //console.log('WebSocket message received:', event.data);
                if (($user && $user["winner"] == true) || ($rival && $rival["winner"] == true)) {
                    //await $ws?.close()
                    const send_json = {"room": $room,
                        "user": "disconnect",
                        "code": "disconnect",
                    }
                    $ws?.send(JSON.stringify(send_json))

                    $ws = undefined;

                    if ($user && $user["winner"] == true) {
                        status = 0;
                        console.log("ha ganado el usuario " + $user["name"]);
                        if ($mode != 'casual') {
                            // const send_json = {"type": "set_status",
                            //     "user": $userName,
                            //     "t_name": $tournamentName,
                            //     "value": 0,
                            // }
                            // await $tournament?.send(JSON.stringify(send_json));
                            goBack();
                        }
                    }
                    else if ($rival && $rival["winner"] == true) {
                        status = 1;
                        console.log("ha ganado el usuario " + $rival["name"]);
                        if ($tournament)
                        {
                            const send_json = {"type": "leave_tournament",
                                "user": $userName,
                                "t_name": $tournamentName,
                                "value": -1,
                            }
                            await $tournament?.send(JSON.stringify(send_json));
                            goBack();
                            // send_json.type = "leave_tournament"
                            // await $tournament?.send(JSON.stringify(send_json));
                            //$tournamentName = undefined;
                        }
                    }
                }
                if ($userName == JSON.parse(event.data.split('_')[0]).name) {
                    $user = JSON.parse(event.data.split('_')[0]);
                    $rival = JSON.parse(event.data.split('_')[1]);
                    $isPlayer1 = true;
                } else {
                    $rival = JSON.parse(event.data.split('_')[0]);
                    $user = JSON.parse(event.data.split('_')[1]);
                    $isPlayer1 = false;
                }
                $ball = JSON.parse(event.data.split('_')[2]);
            };
            $ws.onclose = () => {
                $ws = null;
                console.log('WebSocket connection closed');
            };
        }
    }
    catch
    {
        console.log('Buen intento manin');
    }


    onMount(async () => {
        //$host = "192.168.1.52";
        //$tournament?.close();
        deleteMatchmaking();
        await fetch(`https://${$host}:1024/matchmaking/delete?mode=casual&user=${$userName}`);
    });

    async function deleteMatchmaking() {
		const res = await fetch(`https://${$host}:1024/matchmaking/delete?mode=casual&user=${$userName}`);
		if (res.ok) {
			//console.log("Deleted from matchmaking");
		}
		else {
			console.error("fetch request didn't resolve");
		}
	}

    async function goBack() {
        if ($mode === 'casual') {
            await goto("/");
        }
        else {
            if (status == 0)
                await goto("/tournament");
            else
                await goto("/");
        }
	}

</script>

{#if (status == -1)}
    {#if (isWsInit)}
        <Threlte.Canvas>
            <Scene />
            <Player1 />
            <Player2 />
            <Ball />

            <!-- <StarsEmitter /> -->

            <Environment
                path={'/'}
                files={'Skybox.png'}
                isBackground={true}
            />

            <Bloom />

    <!--         <T.Grid cellColor="#808080" sectionSize={0} />-->

            <T.PerspectiveCamera
                position={[0, 40, 20]}
                fov={50}
                makeDefault
                on:create={({ ref }) => {
                    ref.lookAt(0, 1, 0)
                }}
            >
                <OrbitControls />
            </T.PerspectiveCamera>

            <T.AmbientLight color="#0B0B61" intensity={1} />

            <T.DirectionalLight
                color="#0B0B61"
                intensity={7}
                position={[10, 10, 0]}
                shadow.camera.top={8}
            />

            <T.PointLight
                color="#75a1f9"
                intensity={500}
                position={[-1.75, 0, 1.75]}
            />

            <T.FogExp2 color={'#dddddd'} density={100} />
        </Threlte.Canvas>
    {:else}
        <h1>Ander mariquita hihi</h1>
    {/if}
{:else if (status == 0)}
    <div class="modal-background">
		<div class="modal-content" on:click|stopPropagation>
			<h1 class="modal-title">YOU WIN :)</h1>
			<button type="button" class="btn btn-secondary" on:click={() => goBack()}>Continue</button>
		</div>
	</div>
{:else if (status == 1)}
    <div class="modal-background">
		<div class="modal-content" on:click|stopPropagation>
			<h1 class="modal-title">YOU LOSE :(</h1>
			<button type="button" class="btn btn-secondary" on:click={() => goBack()}>Go Back</button>
		</div>
	</div>
{/if}

<style>

    .modal-background {
        background: white;
		margin: 1%;
		margin-top: 80px;
		font-family: 'xenotron', sans-serif;
    }

    .modal-content {
		align-items: center;
		justify-content: center;
    }

    div.btn:hover {
        background-color: rgba(0, 255, 255, 0.5);
        border-color: #00ffff;
        box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff;
    }

    div.btn button:hover {
        background-color: transparent;
        border-color: transparent;
        box-shadow: none;
    }

	.btn {
		background-color: transparent;
		border: 1px solid #00ffff;
		color: #00ffff;
		text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
	}

	main {
		text-align: center;
		margin-top: 50px;
	}

	@font-face {
		font-family: 'xenotron';
		src: url('/fonts/xenotron/XENOTRON.TTF') format('truetype');
	}

	.font-xe {
		font-family: 'xenotron', sans-serif;
	}
</style>