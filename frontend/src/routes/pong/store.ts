// store.ts

import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

// Define el tipo para el WebSocket
type WebSocketType = WebSocket | null;

// Crea un store writable para el WebSocket
export const ws: Writable<WebSocketType> = writable(null);

export const user: Writable<string | undefined> = writable('UserName');
export const rival: Writable<string | undefined> = writable('RivalName');
export const room: Writable<string | undefined> = writable('RoomName');

export const user_points: Writable<number> = writable(0);
export const rival_points: Writable<number> = writable(0);

