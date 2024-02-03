import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const loginStorage: Writable<string | undefined> = writable('');
