import { isLogged } from "$lib/scripts/UserUtiliteis";
import { userState } from "$lib/scripts/stores";
import { browser } from "$app/environment";
export const ssr = false;

/** @type {import('./$types').LayoutServerLoad} */
export async function load() {
   if (browser) {
      console.log("logged: ", isLogged());
      userState.init({id: 1, username: 'test'});

   }


   return {replace: 1};


}