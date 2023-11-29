<script lang="ts">
	import { page } from '$app/stores';
	import { onDestroy } from 'svelte';
	import { randInt } from 'three/src/math/MathUtils';
	const mode = $page.url.searchParams.get('mode');
	const phrases: Array<string> = [
		"Sharpening Cristian's dark humour",
		"Training Ander's pet rock to protest for better rights than humans",
		"Teaching Toño's cat to hack into the catnip black market",
		"Finding Beñat's secret stash of expired fortune cookies for life advice",
		"Plotting Cristian's journey to become the world's first professional procrastinator",
		"Coaching Aingeru's plants to plan a rebellion against overwatering",
		"Designing Toño's hoverboard programmed to dodge responsibilities",
		"Building Ander's time machine. It only goes back to awkward moments",
		"Creating Beñat's ultimate playlist for summoning ghosts at midnight",
		"Organizing Cristian's library of forbidden puns",
		"Drafting Aingeru's guide to deciphering the existential crisis of goldfish",
		"Training Ander's pet rock to breakdance",
		"Teaching Toño's cat to speak JavaScript",
		"Finding Beñat's secret stash of unicorn tears",
		"Plotting Cristian's journey to become a professional meme",
		"Coaching Aingeru's plants for a stand-up comedy routine",
		"Designing Toño's hoverboard for commuting to Mars",
		"Building Ander's time machine, just for laughs",
		"Creating Beñat's ultimate playlist for coding marathons",
		"Organizing Cristian's library of dad jokes",
		"Drafting Aingeru's guide to translating dog barks",
		'Hunting for unicorns in a forest of reality',
		'Programming a dance routine for binary code',
		"Tattooing 'Ctrl+Z' on your wrist for life mistakes",
		'Attempting to teach a cat quantum physics',
		'Creating a manual for speaking fluent sarcasm',
		'Polishing the wit and charm in your DNA',
		'Asking Siri for relationship advice',
		'Brewing potions to summon WiFi everywhere',
		'Searching for the lost socks in the Bermuda Triangle',
		'Designing a roadmap to navigate through Monday mornings',
		"Teaching Toño's cat to write poetry in HTML",
		"Training Aingeru's plants to perform interpretative dance",
		'Designing a supercomputer for decoding dolphin conversations',
		"Crafting Beñat's ultimate playlist for serenading aliens",
		"Plotting Cristian's journey to become a ninja warrior in pajamas",
		"Coaching Ander's pet rock to host a late-night talk show",
		'Building a robot chef to cook meals based on mood swings',
		"Organizing a library of conspiracy theories for Aingeru's goldfish",
		'Drafting a guide on how to negotiate with stubborn vending machines',
		'Hunting for buried treasure in a sandbox',
		'Programming a GPS for finding the nearest bubble tea shop',
		'Creating a machine to translate baby gibberish into Shakespearean language',
		'Polishing a sarcasm detector for self-improvement purposes',
		'Asking Alexa for fashion advice for time travelers',
		'Brewing potions to turn rainbows into tangible bridges',
		'Searching for the perfect meme in a haystack of internet content',
		'Designing a coffee mug that refills itself magically',
		'Crafting a recipe book for cooking with emotions',
		"Plotting a cat's journey to become a master illusionist",
		'Coaching a squirrel to break the world record in acorn gathering',
		"Building a pillow fort that's earthquake-proof",
		'Organizing a symphony of alarm clocks for waking up the entire neighborhood',
		'Drafting a survival guide for navigating through a maze of bureaucracy',
		'Hunting for the rarest pizza topping in the universe',
		'Programming a robot to make perfect paper airplanes',
		'Creating a weather forecast for imaginary lands',
		'Polishing a crystal ball for predicting spontaneous dance parties',
		'Asking Google Assistant for advice on parallel universe travel',
		'Brewing a potion to turn Monday mornings into Saturday evenings'
	];

	async function startMatchmaking() {}
	let randPhrase: string = phrases[randInt(0, phrases.length - 1)];
	const interval = setInterval(() => {
		randPhrase = phrases[randInt(0, phrases.length - 1)];
	}, 5000);
	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<svelte:head>
    <title>CyberPong - Leaderboard</title>
</svelte:head>
<div class="spinner-border" role="status">
	<span class="visually-hidden">Loading...</span>
</div>
<p>{randPhrase}</p>
