import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const loginStorage: Writable<string | undefined> = writable('');
export const loginType: Writable<string | undefined> = writable('');
export const userName: Writable<string | undefined> = writable('');
export const host: Writable<string | undefined> = writable("192.168.1.52");
