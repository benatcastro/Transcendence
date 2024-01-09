// store.ts

import type { Float } from '@threlte/extras';
import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

// Define el tipo para el WebSocket
type WebSocketType = WebSocket | null;

// Crea un store writable para el WebSocket
export const ws: Writable<WebSocketType> = writable(null);

export const userName: Writable<string | undefined> = writable('UserName');
export const rivalName: Writable<string | undefined> = writable('RivalName');
export const room: Writable<string | undefined> = writable('RoomName');
export const isPlayer1: Writable<Boolean> = writable(false);

export const user: Writable<JSON | null> = writable(null)
export const rival: Writable<JSON | null> = writable(null)
export const ball: Writable<JSON | null> = writable(null)
