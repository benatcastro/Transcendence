import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

// Define el tipo para el WebSocket
type WebSocketType = WebSocket | null;

// Crea un store writable para el WebSocket
export const ws: Writable<WebSocketType> = writable(null);
export const tournamentName: Writable<string | undefined> = writable("");
export const inGame: Writable<boolean> = writable(false);