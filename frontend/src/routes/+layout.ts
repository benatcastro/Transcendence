import { isLogged } from "$lib/scripts/UserUtiliteis";
import { userLogged } from "$lib/scripts/stores";

export const ssr = false;

/** @type {import('./$types').LayoutServerLoad} */
export async function load() {
   if (isLogged())
      userLogged.set(true);
}