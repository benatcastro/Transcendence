import { isLogged } from "$lib/scripts/UserUtiliteis";
import { userState } from "$lib/scripts/stores";
import { browser } from "$app/environment";
import { constants } from "$lib/scripts/constants";
export const ssr = false;

/** @type {import('./$types').LayoutServerLoad} */
export async function load() {

   if (browser) {
      const status = isLogged();
      console.log("logged: ", status);

      if (status) {
         console.log("token ->", localStorage.getItem(constants.JWTkey))
         const apiURL = "http://localhost:3000/auth/jwt";

         const reqBody = {
            jwt: "patata"
         }

         const response =  await fetch(apiURL, {
            method: "POST",
            headers: {
               "Authorization": "Bearer " + localStorage.getItem(constants.JWTkey)
            },
            body: JSON.stringify(reqBody)
         })
         const data = await response.json();
         console.log(data);
         userState.init({id: data?.id, username: data?.username});
         console.log("user initiated");
      }

   }


   return {replace: 1};


}