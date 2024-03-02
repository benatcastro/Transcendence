import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const loginStorage: Writable<string | undefined> = writable('');
export const loginType: Writable<string | undefined> = writable('');
export const userName: Writable<string | undefined> = writable('');
export const rival: Writable<string | undefined> = writable('');
export const room: Writable<string | undefined> = writable('');
export const host: Writable<string | undefined> = writable("10.14.4.3");
export const mode: Writable<string | undefined> = writable("");
export const hostmanual: string = "10.14.4.3";
