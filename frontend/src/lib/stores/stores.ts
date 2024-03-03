import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const loginStorage: Writable<string | undefined> = writable('');
export const loginType: Writable<string | undefined> = writable('');
export const userName: Writable<string | undefined> = writable('');
export const rival: Writable<string | undefined> = writable('');
export const room: Writable<string | undefined> = writable('');
export const host: string = "10.14.6.5";
export const mode: Writable<string | undefined> = writable("casual");
