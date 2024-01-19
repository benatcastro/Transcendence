<script lang="ts">
	import { goto } from '$app/navigation';
	import MDBBtn from 'mdbsvelte/src/MDBBtn.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';

	export let gradient: string = '',
		rounded: string = '';

	let isLoggedIn: boolean = false; // TODO This will be a store so all urls can access it
	let username: string = '';
	let optionType: string = '';
	let token;
	let usernameDjango;
  	let error;
	let socket;



	const login = async () => {
    try {
      const response = await fetch("http://localhost:8000/api-token-auth/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          usernameDjango: "test",
          password: "mypass123",
        }),
      });

      if (response.ok) {
        const data = await response.json();
        token = data.token;
        error = null;
        openWebSocket();
      } else {
        const data = await response.json();
        error = data.non_field_errors[0];
        token = null;
      }
    } catch (error) {
      console.error("Error al realizar la solicitud:", error);
      error = "Error al realizar la solicitud.";
      token = null;
    }
  };

  const openWebSocket = () => {
    if (token) {
	console.log("token " + token);
      const socketUrl = `wss://localhost/ws/matchmaking/?token=${token}`;
      socket = new WebSocket(socketUrl);

      //socket.onopen = handleSocketOpen;
      //socket.onmessage = handleSocketMessage;
      //socket.onclose = handleSocketClose;
    } else {
      console.error("No se ha encontrado un token válido.");
    }
  };

  onMount(() => {
    login();
  });
	//socket = new WebSocket('wss://localhost/ws/matchmaking/');

	if (socket) {
		socket.onopen = (event) => {
			console.log('Conexion abierta:', event);
		};

		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			console.log('Mensaje recibido:', data);

			username = data.user.toString();
			socket.close();
			goto(`/matchmaking?mode=${optionType}&user=${username}`);
		};

		socket.onclose = (event) => {
			console.log('Conexion cerrada:', event);
		};
	}

	async function getUser() {
		if (!isLoggedIn) {
			// Ejemplo de creacion de partida casual
			if (socket)
			{
				socket.send(JSON.stringify({
					action: 'create',
					mode: 'casual',
				}));
			}
		}
		else
			console.log("TEST2");
		return username;
	}

	async function handlePlayClick(option: string) {
		try {
			if (option !== 'ranked' || isLoggedIn) {
				optionType = option;
				await getUser();

				//await goto(`/matchmaking?mode=${option}&user=${username}`);
			}
			else
				console.log("TEST3");
		} catch (e) {
			console.error("error_aherrero_____" + option + "____" + isLoggedIn);
		}
	}
</script>

<Modal title="Play" {gradient} {rounded}>
	<div slot="modalBody">
		<MDBBtn on:click={() => handlePlayClick('casual')}>
			<p>Casual</p>
		</MDBBtn>
		<MDBBtn on:click={() => handlePlayClick('ranked')}>
			<p>Ranked</p>
		</MDBBtn>
	</div>
	<div slot="modalFooter">
		<MDBBtn color="secondary" on:click={() => MDBBtn.toggle()}>Close</MDBBtn>
	</div>
</Modal>
